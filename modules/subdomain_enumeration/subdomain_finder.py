import os
import subprocess
from modules.subdomain_enumeration.utils import brute_force_subdomains
from modules.project_manager.config_manager import load_config

def find_subdomains(domain):
    """Find subdomains for a given domain using sublist3r and a custom brute-force approach."""
    print(f"Starting subdomain enumeration for: {domain}")
    
    # Load the project name from the current configuration
    project_name = domain.split('.')[0]
    try:
        project_config = load_config(project_name)
    except FileNotFoundError:
        print(f"Error: Project '{project_name}' does not exist. Please create the project first.")
        return

    # Define the output folder
    project_dir = os.path.join("data/projects", project_name)
    output_file = os.path.join(project_dir, "subdomain_results", f"{domain}_subdomains.txt")

    # Step 1: Use Sublist3r (Ensure sublist3r is installed: `pip install sublist3r`)
    try:
        print("Running Sublist3r...")
        result = subprocess.run(
            ["sublist3r", "-d", domain, "-o", output_file],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"Error running Sublist3r: {e}")
    
    # Step 2: Brute-force subdomains
    print("Running brute-force enumeration...")
    brute_force_results = brute_force_subdomains(domain)
    
    # Save brute-force results to the file
    with open(output_file, "a") as f:
        for subdomain in brute_force_results:
            f.write(f"{subdomain}\n")
    
    print(f"Subdomain enumeration completed. Results saved to: {output_file}")
