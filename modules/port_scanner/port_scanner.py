import os
import subprocess
import datetime

def scan_ports(project_name, targets):
    port_scanning_dir = os.path.join('data', 'projects', project_name, 'port_scanning')
    if not os.path.exists(port_scanning_dir):
        os.makedirs(port_scanning_dir)
    
    for target in targets:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        output_file = os.path.join(port_scanning_dir, f'{current_time}_{target}.xml')
        try:
            subprocess.run(['nmap', '-sV', '-oX', output_file, target], check=True)
            print(f"Scan completed for {target}. Output saved to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error scanning {target}: {e}")
        except FileNotFoundError:
            print("Nmap not found. Please install Nmap and ensure it's in your system's PATH.")