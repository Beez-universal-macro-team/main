import subprocess
import sys
import importlib.util
from importlib.metadata import version, PackageNotFoundError

# Define required libraries and their optional minimum versions
required_libraries = {
    'pynput': None,
    'Pillow': '9.0.0',
    'mss': None,
    'discord.py': None,
    'discord': None,
    'psutil': None,
    'customtkinter': None,
    'requests': '2.25.0',
    'fonttools': None,
    'ultralytics': None,
    'matplotlib': '3.4.0',
    'opencv-python': None,
    'numpy': '1.21.0',
    'colorama': None,
    'ImageHash': None,
    'pyautogui': None
}

def uninstall_package(package):
    """Uninstall a package using pip."""
    try:
        print(f"Uninstalling {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "--yes", package])
        print(f"{package} uninstalled successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to uninstall {package}. It might not be installed.")

def install_package(package):
    """Install a package using pip."""
    try:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])
        print(f"{package} installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}.")

def reinstall_package(package):
    """Uninstall and reinstall a package."""
    try:
        uninstall_package(package)
        install_package(package)
    except Exception as e:
        print(f"Failed to reinstall {package}: {e}")

def check_libraries(libraries):
    """Check each library and attempt to fix issues."""
    for library, min_version in libraries.items():
        print(f"Checking {library}...")
        try:
            # Check if the library is installed
            if importlib.util.find_spec(library) is None:
                print(f"{library} is not installed.")
                install_package(library)
            else:
                print(f"{library} is installed.")
                if min_version:
                    try:
                        # Check library version
                        installed_version = version(library)
                        if installed_version < min_version:
                            print(f"Updating {library} (Installed: {installed_version}, Required: {min_version})...")
                            reinstall_package(f"{library}>={min_version}")
                        else:
                            print(f"{library} is up to date (Version: {installed_version}).")
                    except PackageNotFoundError:
                        print(f"Failed to retrieve version for {library}.")
        except Exception as e:
            print(f"An error occurred while checking {library}: {e}")
            reinstall_package(library)

def main():
    # Ensure pip and setuptools are upgraded
    try:
        print("Upgrading pip and setuptools...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools"])
        print("Pip and setuptools upgraded successfully.")
    except subprocess.CalledProcessError:
        print("Failed to upgrade pip and setuptools.")

    # Check and fix libraries
    check_libraries(required_libraries)

    print("All libraries checked, uninstalled, and reinstalled if necessary.")
    input("Press Enter to close...")

if __name__ == "__main__":
    main()
