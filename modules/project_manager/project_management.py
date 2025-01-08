import os
import shutil
from config import PROJECTS_DIR
from ..port_scanner.port_scanner import scan_ports
from ..subdomain_enumeration.subdomain_enum import enumerate_subdomains
from ..web_crawler.web_crawler import web_crawl  
from ..scheduler.scheduler import schedule_scan, list_scheduled_tasks, remove_scheduled_task 
from ..vulnerability_scanner.vulnerability_scanning import vulnerability_scan
from ..stats_visualization.stats_visualization import visualize_project_stats 

#PROJECTS_DIR = "data/projects"

def create_project():
    if not os.path.exists(PROJECTS_DIR):
        os.makedirs(PROJECTS_DIR)
    
    project_name = input("Enter the project name: ").strip()
    if not project_name:
        print("Project name cannot be empty.")
        return
    
    project_path = os.path.join(PROJECTS_DIR, project_name)
    if os.path.exists(project_path):
        print(f"Project '{project_name}' already exists.")
    else:
        os.makedirs(project_path)
        print(f"Project '{project_name}' created successfully.")

def list_projects():
    if not os.path.exists(PROJECTS_DIR) or not os.listdir(PROJECTS_DIR):
        print("No projects available.")
        return
    
    projects = os.listdir(PROJECTS_DIR)
    print("\n--- Projects ---")
    for idx, project in enumerate(projects, 1):
        print(f"{idx}. {project}")
    
    choice = input("Enter the number to select a project or 'b' to go back: ")
    if choice.lower() == 'b':
        return
    elif choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(projects):
            selected_project = projects[choice - 1]
            project_path = os.path.join(PROJECTS_DIR, selected_project)
            project_specific_menu(selected_project, project_path)
        else:
            print("Invalid project number.")
    else:
        print("Invalid input. Please enter a number or 'b'.")

def project_specific_menu(project_name, project_path):
    while True:
        print(f"\n--- Project: {project_name} ---")
        print("1. View Details")
        print("2. Work on Project")
        print("b. Back")
        action = input("Select an action or 'b' to go back: ")
        
        if action == '1':
            view_project_details(project_path)
        elif action == '2':
            work_on_project(project_path)
        elif action.lower() == 'b':
            break
        else:
            print("Invalid action. Please select a valid option.")

def view_project_details(project_path):
    files = os.listdir(project_path)
    if not files:
        print("No data available for this project.")
    else:
        print("Files in project:")
        for file in files:
            print(f"- {file}")

def work_on_project(project_path):
    project_name = os.path.basename(project_path)
    while True:
        print("\n--- Work on Project: {project_name} ---")
        print("1. Port Scanning")
        print("2. Subdomain Enumeration")
        print("3. Web Crawling")
        print("4. Vulnerability Scanning")
        print("5. Scan Schedulers")
        print("6. Visualize Statistics")
        print("b. Back")
        choice = input("Select an option or 'b' to go back: ")
        
        if choice == '1':
            option = input("Do you want to scan a single domain or provide a list of domains? (single/list): ")
            if option.lower() == 'single':
                domain = input("Enter the domain to scan: ")
                scan_ports(project_name, [domain])
            elif option.lower() == 'list':
                file_path = input("Enter the file path containing the list of domains: ")
                try:
                    with open(file_path, 'r') as f:
                        domains = [line.strip() for line in f.readlines()]
                    scan_ports(project_name, domains)
                except FileNotFoundError:
                    print("File not found. Please provide a valid file path.")
                except IOError:
                    print("Error reading the file. Please check the file permissions.")
            else:
                print("Invalid option.")
        elif choice == '2':
            domain = input("Enter the domain to enumerate subdomains: ")
            mode = input("Choose mode (osint/bruteforce): ").strip().lower()
            enumerate_subdomains(project_name, domain, mode)
        elif choice == '3':
            domain = input("Enter the domain to crawl: ")
            web_crawl(project_name, domain)
        elif choice == '4':
            print(f"[+] Starting vulnerability scan for project: {project_name}...")
            vulnerability_scan(project_name)
        elif choice == '5':
            print("\n--- Scan Schedulers ---")
            print("1. Schedule a New Scan")
            print("2. List Scheduled Scans")
            print("3. Remove a Scheduled Scan")
            print("b. Back")
            scheduler_choice = input("Select an option or 'b' to go back: ")
            if scheduler_choice == '1':
                scan_type = input("Enter the scan type (port_scan/subdomain_enum/web_crawl): ")
                interval = input("Enter the interval (daily/weekly/monthly): ")
                domain = input("Enter the domain: ")
                schedule_scan(project_name, scan_type, interval, domain)
            elif scheduler_choice == '2':
                list_scheduled_tasks()
            elif scheduler_choice == '3':
                task_id = input("Enter the task ID to remove: ")
                remove_scheduled_task(task_id)
            elif scheduler_choice.lower() == 'b':
                continue
            else:
                print("Invalid choice.")
        elif choice == '6':
            print(f"[+] Visualizing statistics for project: {project_name}...")
            visualize_project_stats(project_name)
        elif choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def delete_project():
    if not os.path.exists(PROJECTS_DIR) or not os.listdir(PROJECTS_DIR):
        print("No projects available to delete.")
        return
    
    projects = os.listdir(PROJECTS_DIR)
    print("\n--- Projects ---")
    for idx, project in enumerate(projects, 1):
        print(f"{idx}. {project}")
    
    choice = input("Enter the number of the project to delete or 'b' to go back: ")
    if choice.lower() == 'b':
        return
    elif choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(projects):
            selected_project = projects[choice - 1]
            project_path = os.path.join(PROJECTS_DIR, selected_project)
            confirm = input(f"Are you sure you want to delete '{selected_project}'? (y/n): ").strip().lower()
            if confirm == 'y':
                shutil.rmtree(project_path)
                print(f"Project '{selected_project}' deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid project number.")
    else:
        print("Invalid input. Please enter a number or 'b'.")