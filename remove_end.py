import os
import shutil

# Directory of the virtual environment
venv_dir = os.path.join(os.getcwd(), 'venv')

def remove_virtual_environment(venv_dir):
    """Remove the virtual environment."""
    if os.path.exists(venv_dir):
        print("Removing virtual environment...")
        shutil.rmtree(venv_dir)
        print("Virtual environment removed successfully.")
    else:
        print("The virtual environment does not exist or has already been removed.")

if __name__ == "__main__":
    remove_virtual_environment(venv_dir)
