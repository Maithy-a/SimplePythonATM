# SimplePythonATM

This is a simple ATM simulation script written in Python (`atm.py`). It authenticates users with a PIN, allows withdrawals and deposits, and checks the account balance. This README explains how to set up the project and convert `atm.py` into a standalone executable using PyInstaller.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/downloads/) if needed.
- **Git**: Required to clone the repository.
- **PyInstaller**: Used to convert the script into an executable.

## Setup Instructions

### 1. Extract the Code
Follow these steps to get the project files onto your system:

#### Option 1: Clone the Repository
If you’re using Git:
```bash
git clone https://github.com/Maithy-a/SimplePythonATM.git
cd SimplePythonATM
```

### 2. Test the Script
Before converting to an executable, test the script to ensure it works:
```bash
python atm.py
```

## Converting atm.py to an Executable with PyInstaller

### Step 1: Install PyInstaller
If you don’t already have PyInstaller installed, run:
```bash
pip install pyinstaller
```

### Step 2: Generate the Executable
In the project directory, run the following command to create a standalone executable:
```bash
pyinstaller --onefile atm.py
```
- `--onefile`: Bundles everything into a single `.exe` file.
- Output will be in the `dist/` folder (e.g., `dist/atm.exe`).

### Step 3: Run the Executable
- Navigate to the `dist/` folder:
```bash
cd dist
```
- Run the executable:
  - On Windows: Double-click `atm.exe` or run `atm.exe` from the command prompt.
  - On macOS/Linux: `./atm` (you may need to make it executable with `chmod +x atm`).

## Notes
- The `build/` and `dist/` folders, along with the `.spec` file, are generated by PyInstaller and ignored by Git (see `.gitignore`).
- If you encounter issues, ensure your Python environment is correctly set up and all dependencies are installed.

## Files in This Repository
- `atm.py`: The main ATM script.
- `requirements.txt`: List of Python dependencies (if any).
- `.gitignore`: Ignores unnecessary files like PyInstaller outputs and IDE settings.
- `README.md`: This file.

## Troubleshooting
- If the executable doesn’t work, try running PyInstaller without `--onefile` to debug:
```bash
pyinstaller atm.py
```
- Check the terminal output for errors during the PyInstaller process.

Enjoy your ATM simulation!
```
