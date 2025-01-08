import os
import xmltodict
import matplotlib.pyplot as plt
from matplotlib import rcParams
from config import PROJECTS_DIR

# Set the font to a compatible one
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Times New Roman']

def parse_port_scan_results(project_name):
    """
    Parse port scan results from XML files.
    """
    port_scan_dir = os.path.join(PROJECTS_DIR, project_name, "port_scanning")
    if not os.path.exists(port_scan_dir):
        print("[-] No port scan results found.")
        return {}

    port_data = {}
    for file in os.listdir(port_scan_dir):
        if file.endswith(".xml"):
            file_path = os.path.join(port_scan_dir, file)
            with open(file_path, "r") as f:
                xml_data = f.read()
                data = xmltodict.parse(xml_data)

                # Handle cases where 'host' is a list or a single dictionary
                hosts = data["nmaprun"].get("host", [])
                if not isinstance(hosts, list):
                    hosts = [hosts]  # Convert single host to a list

                for host in hosts:
                    if "ports" in host and host["ports"] is not None:
                        ports = host["ports"].get("port", [])
                        if not isinstance(ports, list):
                            ports = [ports]  # Convert single port to a list

                        for port in ports:
                            port_id = port["@portid"]
                            service = port.get("service", {}).get("@name", "unknown")
                            if service in port_data:
                                port_data[service] += 1
                            else:
                                port_data[service] = 1
    return port_data

def parse_subdomain_results(project_name):
    """
    Parse subdomain enumeration results from TXT files.
    """
    subdomain_dir = os.path.join(PROJECTS_DIR, project_name, "subdomain_enumeration")
    if not os.path.exists(subdomain_dir):
        print("[-] No subdomain enumeration results found.")
        return {}

    subdomain_data = {}
    for file in os.listdir(subdomain_dir):
        if file.endswith(".txt"):
            file_path = os.path.join(subdomain_dir, file)
            with open(file_path, "r") as f:
                for line in f:
                    subdomain = line.strip()
                    if subdomain in subdomain_data:
                        subdomain_data[subdomain] += 1
                    else:
                        subdomain_data[subdomain] = 1
    return subdomain_data

def parse_web_crawl_results(project_name):
    """
    Parse web crawling results from TXT files.
    """
    web_crawl_dir = os.path.join(PROJECTS_DIR, project_name, "web_crawling")
    if not os.path.exists(web_crawl_dir):
        print("[-] No web crawling results found.")
        return {}

    url_data = {}
    for file in os.listdir(web_crawl_dir):
        if file.endswith(".txt"):
            file_path = os.path.join(web_crawl_dir, file)
            with open(file_path, "r") as f:
                for line in f:
                    url = line.strip()
                    if url in url_data:
                        url_data[url] += 1
                    else:
                        url_data[url] = 1
    return url_data

def parse_vulnerability_results(project_name):
    """
    Parse vulnerability scan results from TXT files.
    """
    vuln_dir = os.path.join(PROJECTS_DIR, project_name, "vulnerability_scanning")
    if not os.path.exists(vuln_dir):
        print("[-] No vulnerability scan results found.")
        return {}

    vuln_data = {}
    for file in os.listdir(vuln_dir):
        if file.endswith(".txt"):
            file_path = os.path.join(vuln_dir, file)
            with open(file_path, "r") as f:
                for line in f:
                    if "OSVDB" in line:  # Example: Look for OSVDB entries in Nikto reports
                        vuln_type = line.split(":")[0].strip()
                        if vuln_type in vuln_data:
                            vuln_data[vuln_type] += 1
                        else:
                            vuln_data[vuln_type] = 1
    return vuln_data

def plot_bar_chart(data, title, xlabel, ylabel, project_name):
    """
    Generate a bar chart from the given data and save it as an image.
    """
    plt.figure(figsize=(12, 8))  # Increase figure size
    plt.bar(data.keys(), data.values())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")
    plt.subplots_adjust(bottom=0.3)  # Adjust bottom margin
    plt.tight_layout()

    # Save the plot as an image
    output_dir = os.path.join(PROJECTS_DIR, project_name, "stats_visualization")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, f"{title.replace(' ', '_').lower()}_bar_chart.png")
    plt.savefig(output_file)
    plt.close()
    print(f"[+] Bar chart saved to {output_file}")

def plot_pie_chart(data, title, project_name):
    """
    Generate a pie chart from the given data and save it as an image.
    """
    plt.figure(figsize=(10, 10))  # Increase figure size
    plt.pie(data.values(), labels=data.keys(), autopct="%1.1f%%", startangle=140)
    plt.title(title)
    plt.subplots_adjust(bottom=0.1)  # Adjust bottom margin
    plt.tight_layout()

    # Save the plot as an image
    output_dir = os.path.join(PROJECTS_DIR, project_name, "stats_visualization")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, f"{title.replace(' ', '_').lower()}_pie_chart.png")
    plt.savefig(output_file)
    plt.close()
    print(f"[+] Pie chart saved to {output_file}")

def visualize_project_stats(project_name):
    """
    Visualize statistics for the given project.
    """
    # Parse data
    port_data = parse_port_scan_results(project_name)
    subdomain_data = parse_subdomain_results(project_name)
    web_crawl_data = parse_web_crawl_results(project_name)
    vuln_data = parse_vulnerability_results(project_name)

    # Generate visualizations
    if port_data:
        plot_bar_chart(port_data, "Port Scan Results", "Service", "Count", project_name)
        plot_pie_chart(port_data, "Port Scan Results", project_name)

    if subdomain_data:
        plot_bar_chart(subdomain_data, "Subdomain Enumeration Results", "Subdomain", "Count", project_name)
        plot_pie_chart(subdomain_data, "Subdomain Enumeration Results", project_name)

    if web_crawl_data:
        plot_bar_chart(web_crawl_data, "Web Crawling Results", "URL", "Count", project_name)
        plot_pie_chart(web_crawl_data, "Web Crawling Results", project_name)

    if vuln_data:
        plot_bar_chart(vuln_data, "Vulnerability Scan Results", "Vulnerability Type", "Count", project_name)
        plot_pie_chart(vuln_data, "Vulnerability Scan Results", project_name)