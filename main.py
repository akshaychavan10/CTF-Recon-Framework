import argparse
import os
import sys
from modules.project_manager import config_manager, task_manager
from modules.subdomain_enumeration import subdomain_finder
#from modules.port_scanner import scanner as port_scanner
#from modules.web_crawler import crawler
#from modules.vulnerability_scanner import scanner as vulnerability_scanner
#from modules.scheduler import scheduler
#from modules.stats_visualization import visualizer

# Global constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def setup_parser():
    parser = argparse.ArgumentParser(
        description="Multi-functional Cybersecurity Tool - CLI"
    )
    
    subparsers = parser.add_subparsers(
        title="Modules",
        description="Available Modules",
        dest="module"
    )

    # Project Manager
    project_parser = subparsers.add_parser("project", help="Manage projects")
    project_parser.add_argument("action", choices=["create", "list", "delete"], help="Project actions")
    project_parser.add_argument("--name", help="Project name")
    project_parser.set_defaults(func=handle_project)

    # Subdomain Enumeration
    subdomain_parser = subparsers.add_parser("subdomain", help="Find subdomains")
    subdomain_parser.add_argument("domain", help="Target domain")
    subdomain_parser.set_defaults(func=handle_subdomain)

    # Port Scanner
    port_parser = subparsers.add_parser("portscan", help="Scan ports")
    port_parser.add_argument("target", help="Target IP or range")
    port_parser.set_defaults(func=handle_port_scan)

    # Web Crawler
    crawler_parser = subparsers.add_parser("crawl", help="Web crawler")
    crawler_parser.add_argument("url", help="Target URL")
    crawler_parser.set_defaults(func=handle_crawl)

    # Vulnerability Scanner
    vuln_parser = subparsers.add_parser("vulnscan", help="Vulnerability scanner")
    vuln_parser.add_argument("--input", required=True, help="Input file or directory")
    vuln_parser.set_defaults(func=handle_vulnerability_scan)

    # Scheduler
    scheduler_parser = subparsers.add_parser("schedule", help="Manage scan schedules")
    scheduler_parser.add_argument("action", choices=["add", "remove", "list"], help="Scheduler actions")
    scheduler_parser.add_argument("--task", help="Task to schedule")
    scheduler_parser.add_argument("--interval", choices=["daily", "weekly", "monthly"], help="Schedule interval")
    scheduler_parser.set_defaults(func=handle_schedule)

    # Statistics & Visualization
    stats_parser = subparsers.add_parser("visualize", help="Visualize results")
    stats_parser.add_argument("--input", required=True, help="Input data file")
    stats_parser.add_argument("--type", choices=["chart", "graph", "summary"], help="Visualization type")
    stats_parser.set_defaults(func=handle_visualization)

    return parser

# Handlers for CLI commands
def handle_project(args):
    if args.action == "create":
        task_manager.create_project(args.name)
    elif args.action == "list":
        task_manager.list_projects()
    elif args.action == "delete":
        task_manager.delete_project(args.name)

def handle_subdomain(args):
    subdomain_finder.find_subdomains(args.domain)

def handle_port_scan(args):
    port_scanner.scan_ports(args.target)

def handle_crawl(args):
    crawler.start_crawl(args.url)

def handle_vulnerability_scan(args):
    vulnerability_scanner.scan(args.input)

def handle_schedule(args):
    if args.action == "add":
        scheduler.add_task(args.task, args.interval)
    elif args.action == "remove":
        scheduler.remove_task(args.task)
    elif args.action == "list":
        scheduler.list_tasks()

def handle_visualization(args):
    visualizer.visualize_data(args.input, args.type)

# Entry point
if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
