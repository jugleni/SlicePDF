# Virtual Environment Setup and Management

This repository contains two Python scripts to manage and set up virtual environments for Python projects.

## Scripts

1. **remove_end_en.py**: A script to remove the virtual environment from the current directory.
2. **setup_env_en.py**: A script to create a virtual environment, install dependencies from a requirements file, and execute the main Python script.

### Features

- **remove_end_en.py**: Removes the virtual environment.
- **setup_env_en.py**:
  - Creates a new virtual environment if it doesn't exist.
  - Installs dependencies from `requirements.txt`.
  - Executes the main script (currently, `split_pdf.py` is mentioned, but the main script for execution is defined in the repository; adjust as needed).

### Requirements

- Python 3.x
- `PyPDF2` (specified in `requirements.txt`)

### Usage

1. **Clone the repository.**

2. **Setting up and activating the virtual environment:**

   - **Create the virtual environment:**
     From the repository root, run:
     ```sh
     python3 -m venv venv
     ```
     > Note: If you encounter issues with symlinking (for example, "Unable to symlink '/usr/bin/python3'..."), you might need to resolve system-specific constraints or use the system package manager to adjust your Python installation.

   - **Activate the virtual environment:**
     On Linux/Mac:
     ```sh
     source venv/bin/activate
     ```
     On Windows:
     ```cmd
     venv\Scripts\activate
     ```

   - **Install dependencies:**
     With the virtual environment activated, run:
     ```sh
     pip install -r requirements.txt
     ```

3. **Running the application:**

   - You can run the main script directly:
     ```sh
     python app.py
     ```
   - Alternatively, running the environment setup script will also execute the main script:
     ```sh
     python setup_env_en.py
     ```
     This script will check for the existence of the virtual environment, create it if necessary, install the dependencies, and then run the main script.

4. **Removing the virtual environment:**

   - To remove the virtual environment, simply run:
     ```sh
     python remove_end_en.py
     ```
     This will delete the [venv](http://_vscodecontentref_/0) directory from the project.

5. **Deactivating the virtual environment:**

   - When you're done working in the virtual environment, you can deactivate it by running:
     ```sh
     deactivate
     ```

## License

This project is licensed under the MIT License.

## Author

Created by Jugleni Krinski
