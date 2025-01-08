import os
import xmltodict  # Make sure to install this library: pip install xmltodict

def process_xml_files(directory):
    """
    Process all XML files in a given directory.

    :param directory: Path to the directory containing XML files.
    """
    if not os.path.exists(directory):
        print(f"[-] Directory does not exist: {directory}")
        return

    # List all files in the directory
    files = os.listdir(directory)
    xml_files = [file for file in files if file.endswith(".xml")]

    if not xml_files:
        print("[-] No XML files found in the directory.")
        return

    print(f"[+] Found {len(xml_files)} XML files in the directory: {directory}")

    # Dictionary to store parsed data
    port_data = {}

    # Iterate through each XML file
    for xml_file in xml_files:
        file_path = os.path.join(directory, xml_file)
        try:
            # Open and read the XML file
            with open(file_path, "r") as f:
                xml_data = f.read()
                data = xmltodict.parse(xml_data)

                # Ensure hosts are handled properly
                hosts = data.get("nmaprun", {}).get("host", [])
                if not isinstance(hosts, list):  # Handle single host case
                    hosts = [hosts]

                for host in hosts:
                    ports = host.get("ports", {}).get("port", [])
                    if not isinstance(ports, list):  # Handle single port case
                        ports = [ports]

                    for port in ports:
                        port_id = port.get("@portid")
                        service = port.get("service", {}).get("@name")
                        if service:
                            port_data[service] = port_data.get(service, 0) + 1

        except Exception as e:
            print(f"[-] Error processing file {xml_file}: {e}")

    print("[+] Port Data:", port_data)
    return port_data

# Replace this with the path to your directory
xml_directory = "./"  # Set your folder path here
process_xml_files(xml_directory)
