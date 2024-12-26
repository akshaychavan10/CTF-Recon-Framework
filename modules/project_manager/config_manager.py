import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECTS_DIR = os.path.join(BASE_DIR, "../../data/projects/")

def load_config(project_name):
    """Load the configuration for a specific project."""
    config_file = os.path.join(PROJECTS_DIR, project_name, "config.json")
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file not found for project: {project_name}")
    with open(config_file, "r") as f:
        return json.load(f)

def save_config(project_name, config):
    """Save the configuration for a specific project."""
    project_dir = os.path.join(PROJECTS_DIR, project_name)
    os.makedirs(project_dir, exist_ok=True)
    config_file = os.path.join(project_dir, "config.json")
    with open(config_file, "w") as f:
        json.dump(config, f, indent=4)

def initialize_project_config(project_name):
    """Create an initial configuration for a new project."""
    default_config = {
        "project_name": project_name,
        "created_at": os.path.getctime(os.path.join(PROJECTS_DIR, project_name)),
        "modules": {
            "subdomain_enumeration": {},
            "port_scanner": {},
            "web_crawler": {},
            "vulnerability_scanner": {},
            "scheduler": {},
            "stats_visualization": {}
        }
    }
    save_config(project_name, default_config)
