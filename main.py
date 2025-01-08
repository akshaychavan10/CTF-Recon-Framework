import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from modules.project_manager import project_management

def main():
    while True:
        print("\n--- Cybersecurity Tool ---")
        print("1. Create New Project")
        print("2. Existing Projects")
        print("3. Delete Project")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            project_management.create_project()
        elif choice == '2':
            project_management.list_projects()
        elif choice == '3':
            project_management.delete_project()
        elif choice == '4':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()