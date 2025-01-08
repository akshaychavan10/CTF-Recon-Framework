import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from config import PROJECTS_DIR

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# File to store scheduled tasks
SCHEDULED_TASKS_FILE = os.path.join(PROJECTS_DIR, "scheduled_tasks.txt")

def schedule_scan(project_name, scan_type, interval, domain=None):
    """
    Schedule a recurring scan for the given project.
    """
    # Define the task ID
    task_id = f"{project_name}_{scan_type}_{interval}"

    # Define the cron trigger based on the interval
    if interval == "daily":
        trigger = CronTrigger(hour=0, minute=0)  # Run daily at midnight
    elif interval == "weekly":
        trigger = CronTrigger(day_of_week="sun", hour=0, minute=0)  # Run weekly on Sunday at midnight
    elif interval == "monthly":
        trigger = CronTrigger(day=1, hour=0, minute=0)  # Run monthly on the 1st at midnight
    else:
        print("[-] Invalid interval. Choose 'daily', 'weekly', or 'monthly'.")
        return

    # Define the task function
    def task():
        print(f"[+] Running {scan_type} scan for {project_name}...")
        if scan_type == "port_scan":
            from modules.port_scanning.port_scanner import scan_ports
            scan_ports(project_name, [domain])
        elif scan_type == "subdomain_enum":
            from modules.subdomain_enumeration.subdomain_enum import enumerate_subdomains
            enumerate_subdomains(project_name, domain, mode="osint")
        elif scan_type == "web_crawl":
            from modules.web_crawler.web_crawler import web_crawl
            web_crawl(project_name, domain)
        elif scan_type == "vulnerability scanner":
            # vulnerability scanner code here`
            print("vulnerability scanner feature is comming soon")
        else:
            print("[-] Invalid scan type.")

    # Add the task to the scheduler
    scheduler.add_job(task, trigger=trigger, id=task_id)

    # Save the task to the scheduled tasks file
    with open(SCHEDULED_TASKS_FILE, "a") as f:
        f.write(f"{task_id},{project_name},{scan_type},{interval},{domain}\n")

    print(f"[+] Scheduled {scan_type} scan for {project_name} ({interval}).")

def list_scheduled_tasks():
    """
    List all scheduled tasks.
    """
    if not os.path.exists(SCHEDULED_TASKS_FILE):
        print("[-] No scheduled tasks found.")
        return

    with open(SCHEDULED_TASKS_FILE, "r") as f:
        tasks = f.readlines()

    if not tasks:
        print("[-] No scheduled tasks found.")
        return

    print("\n--- Scheduled Tasks ---")
    for task in tasks:
        task_id, project_name, scan_type, interval, domain = task.strip().split(",")
        print(f"Task ID: {task_id}")
        print(f"Project: {project_name}")
        print(f"Scan Type: {scan_type}")
        print(f"Interval: {interval}")
        print(f"Domain: {domain}")
        print("-" * 30)

def remove_scheduled_task(task_id):
    """
    Remove a scheduled task by its ID.
    """
    if not os.path.exists(SCHEDULED_TASKS_FILE):
        print("[-] No scheduled tasks found.")
        return

    # Read all tasks and filter out the one to remove
    with open(SCHEDULED_TASKS_FILE, "r") as f:
        tasks = f.readlines()

    updated_tasks = [task for task in tasks if not task.startswith(task_id)]

    # Write the updated tasks back to the file
    with open(SCHEDULED_TASKS_FILE, "w") as f:
        f.writelines(updated_tasks)

    # Remove the task from the scheduler
    scheduler.remove_job(task_id)
    print(f"[+] Removed scheduled task: {task_id}")