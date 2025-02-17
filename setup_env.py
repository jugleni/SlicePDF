import os
import subprocess
import venv

# Directory of the virtual environment
venv_dir = os.path.join(os.getcwd(), 'venv')
requirements_file = os.path.join(os.getcwd(), 'requirements.txt')
main_script = os.path.join(os.getcwd(), 'app.py')

def create_virtual_environment(venv_dir):
    """Create a virtual environment."""
    print("Creating virtual environment...")
    venv.create(venv_dir, with_pip=True)

def install_dependencies(venv_dir, requirements_file):
    """Install dependencies in the virtual environment."""
    if not os.path.exists(requirements_file):
        print(f"Error: Requirements file not found at '{requirements_file}'. Please check the path.")
        return
    
    pip_executable = os.path.join(venv_dir, 'bin', 'pip') if os.name != 'nt' else os.path.join(venv_dir, 'Scripts', 'pip.exe')
    
    # Install dependencies
    print("Installing dependencies...")
    subprocess.run([pip_executable, "install", "-r", requirements_file])

def run_main_script(venv_dir, main_script):
    """Run the main script."""
    if not os.path.exists(main_script):
        print(f"Error: Main script not found at '{main_script}'. Please check the path.")
        return
    
    python_executable = os.path.join(venv_dir, 'bin', 'python') if os.name != 'nt' else os.path.join(venv_dir, 'Scripts', 'python.exe')
    
    print("Running the main script...")
    subprocess.run([python_executable, main_script])

def main():
    if not os.path.exists(venv_dir):
        create_virtual_environment(venv_dir)

    install_dependencies(venv_dir, requirements_file)
    run_main_script(venv_dir, main_script)

if __name__ == "__main__":
    main()
