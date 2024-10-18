import os
import subprocess
import venv

# Directory of the virtual environment
venv_dir = os.path.join(os.getcwd(), 'venv')

def create_virtual_environment(venv_dir):
    """Create a virtual environment."""
    print("Creating virtual environment...")
    venv.create(venv_dir, with_pip=True)

def install_dependencies(venv_dir):
    """Install dependencies in the virtual environment."""
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_dir, 'Scripts', 'activate.bat')
    else:  # Linux/Mac
        activate_script = os.path.join(venv_dir, 'bin', 'activate')

    # Install dependencies
    print("Installing dependencies...")
    subprocess.run(f"{activate_script} && pip install -r requirements.txt", shell=True)

def run_main_script(venv_dir):
    """Run the main script."""
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_dir, 'Scripts', 'activate.bat')
    else:  # Linux/Mac
        activate_script = os.path.join(venv_dir, 'bin', 'activate')

    print("Running the main script...")
    subprocess.run(f"{activate_script} && python split_pdf.py", shell=True)

def main():
    if not os.path.exists(venv_dir):
        create_virtual_environment(venv_dir)

    install_dependencies(venv_dir)
    run_main_script(venv_dir)

if __name__ == "__main__":
    main()
