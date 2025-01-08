# CTF-Recon-Framework

A Python-based multi-function cybersecurity tool to perform recon on CTF machines.

## Features

- **Port Scanning**: Scan open ports and services on a target host.
- **Subdomain Enumeration**: Discover subdomains using OSINT or bruteforce.
- **Web Crawling**: Crawl a website to collect links and extract useful data.
- **Vulnerability Scanning**: Scan for vulnerabilities using Nikto.
- **Scan Schedulers**: Schedule recurring scans (daily, weekly, monthly).
- **Statistics Visualization**: Generate and display intuitive data visualizations (bar charts, pie charts).

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/cybersecurity-tool.git
cd "CTF-Recon-Framework"
```

2. **Install the required dependencies:**
```bash
pip install -r requirements.txt
```

3. **Install additional tools:**
	1. **Nikto** : Install Nikto for vulnerability scanning.
	2. **Nmap** : Install Nmap for port scanning.
4. **Run the tool:**
```bash
python3 main.py
```

## Usage

1. **Create a New Project**:
    - Use the `Create New Project` option to start a new project.
2. **Perform Scans**:
    - Use the `Port Scanning`, `Subdomain Enumeration`, `Web Crawling`, and `Vulnerability Scanning` options to perform scans.
3. **Schedule Scans**:
    - Use the `Scan Schedulers` option to schedule recurring scans.    
4. **Visualize Statistics**:
    - Use the `Visualize Statistics` option to generate and view data visualizations.

## Project Structure

```
CTF-Recon-Framework/
  config.py
  main.py
  modules/
    __init__.py
    project_manager/
      __init__.py
      project_management.py
    port_scanning/
      __init__.py
      port_scanner.py
    subdomain_enumeration/
      __init__.py
      subdomain_enum.py
    web_crawler/
      __init__.py
      web_crawler.py
    vulnerability_scanning/
      __init__.py
      vulnerability_scanner.py
    stats_visualization/
      __init__.py
      stats_visualization.py
  data/
    projects/
      project1/
        subdomain_enumeration/
        web_crawling/
        port_scanning/
        vulnerability_scanning/
        stats_visualization/
```

## Dependencies

- Python 3.x
- External Tools: Nikto, Nmap

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Author

Akshay Chavan
GitHub: [akshaychavan10](https://github.com/akshaychavan10)  
Email: [akschavan100@gmail.com](mailto:akschavan100@gmail.com)