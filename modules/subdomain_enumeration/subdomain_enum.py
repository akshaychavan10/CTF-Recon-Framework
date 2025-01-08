import os
import sublist3r
#from modules.project_manager.project_management import PROJECTS_DIR
from config import PROJECTS_DIR
from datetime import datetime
import subprocess

def enumerate_subdomains(project_name, domain, mode="osint"):
    """
    Enumerate subdomains using Sublist3r (OSINT) or bruteforce (placeholder).
    """
    # Define the output directory
    output_dir = os.path.join(PROJECTS_DIR, project_name, "subdomain_enumeration")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the output file path
    #output_file = os.path.join(output_dir, f"{domain}_subdomains.txt")
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
    #output_file = os.path.join(output_dir, f"{current_time}_{domain}_subdomains.txt")

    if mode == "osint":
        print(f"[+] Enumerating subdomains for {domain} using OSINT (Sublist3r)...")
        try:
            # Parameters for Sublist3r
            threads = 30
            ports = None  # Specify ports if needed
            silent = False  # Whether to suppress output
            verbose = True  # Enable detailed output
            enable_bruteforce = False  # Disable bruteforce
            engines = None  # Use default engines

            ## output file name 
            output_file = os.path.join(output_dir, f"osint_{current_time}_{domain}_subdomains.txt")
            # Call Sublist3r and get the list of subdomains
            subdomains = sublist3r.main(
                domain=domain,
                threads=threads,
                savefile=output_file,
                ports=ports,
                silent=silent,
                verbose=verbose,
                enable_bruteforce=enable_bruteforce,
                engines=engines
            )

            print(f"[+] Subdomain enumeration completed. Found {len(subdomains)} subdomains.")
            print(f"[+] Results saved to {output_file}")
        except Exception as e:
            print(f"[-] An error occurred while running Sublist3r: {e}")
    elif mode == "bruteforce":
        print(f"[+] Enumerating subdomains for {domain} using bruteforce (ffuf)...")
        bruteforce_file = input("Enter the path to the bruteforce wordlist file: ").strip()
        if not os.path.isfile(bruteforce_file):
            print("[-] Invalid file path. Please provide a valid wordlist file.")
            return

        try:
            # output file
            output_file = os.path.join(output_dir, f"bruteforce_{current_time}_{domain}_subdomains.md")
            # Run ffuf command
            ffuf_command = [
                "ffuf",
                "-w", bruteforce_file,  # Wordlist file
                "-u", f"http://{domain}",  # Target URL
                "-H", f"Host: FUZZ.{domain}",  # Host header for subdomain enumeration
                "-o", output_file,  # Output file
                "-of", "md"  # Output format (JSON)
            ]

            print(f"[+] Running ffuf command: {' '.join(ffuf_command)}")
            subprocess.run(ffuf_command, check=True)
            print(f"[+] Bruteforce enumeration completed. Results saved to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"[-] Error running ffuf: {e}")
        except FileNotFoundError:
            print("[-] ffuf not found. Please ensure ffuf is installed and in your system's PATH.")
    else:
        print("[-] Invalid mode selected. Choose 'osint' or 'bruteforce'.")
