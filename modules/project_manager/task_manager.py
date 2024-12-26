import os
from modules.project_manager import config_manager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECTS_DIR = os.path.join(BASE_DIR, "../../data/projects/")

FOLDER_STRUCTURE = [
    "subdomain_results",
    "port_scanner_results",
    "web_crawler_results",
    "vulnerability_scanner_results",
    "reports"
]

def create_project(project_name):
    """Create a new web app testing project."""
    if not project_name:
        print("Error: Project name is required.")
        return

    project_path = os.path.join(PROJECTS_DIR, project_name)
    if os.path.exists(project_path):
        print(f"Error: Project '{project_name}' already exists.")
        return

    try:
        # Create the main project folder
        os.makedirs(project_path)

        # Create subfolders
        for folder in FOLDER_STRUCTURE:
            os.makedirs(os.path.join(project_path, folder))
        
        # Initialize project configuration
        config_manager.initialize_project_config(project_name)

        print(f"Project '{project_name}' created successfully at {project_path}.")
    except Exception as e:
        print(f"Error: Failed to create project '{project_name}'. Reason: {e}")

def list_projects():
    """List all existing projects."""
    if not os.path.exists(PROJECTS_DIR):
        print("No projects found.")
        return

    projects = os.listdir(PROJECTS_DIR)
    if not projects:
        print("No projects found.")
    else:
        print("Existing Projects:")
        for project in projects:
            print(f"- {project}")

def delete_project(project_name):
    """Delete an existing project."""
    project_path = os.path.join(PROJECTS_DIR, project_name)
    if not os.path.exists(project_path):
        print(f"Error: Project '{project_name}' does not exist.")
        return

    try:
        import shutil
        shutil.rmtree(project_path)
        print(f"Project '{project_name}' deleted successfully.")
    except Exception as e:
        print(f"Error: Failed to delete project '{project_name}'. Reason: {e}")
