import subprocess
import sys
import importlib.util
from importlib.metadata import version, PackageNotFoundError
import urllib.request
import platform
import os
import tempfile

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
    'pyautogui': None,
    'discord.ext': None,
    'mouse': None,
    'easyocr': None,
    'keyboard': None,
}

def install_visual_c_redistributable():
    """Download and install Microsoft Visual C++ Redistributable based on system architecture."""
    # Define download links
    vc_redist_links = {
        "ARM64": "https://aka.ms/vs/17/release/vc_redist.arm64.exe",
        "X86": "https://aka.ms/vs/17/release/vc_redist.x86.exe",
        "X64": "https://aka.ms/vs/17/release/vc_redist.x64.exe",
    }

    needs_restart = False  # Flag to indicate if a system restart is needed

    if sys.platform == "win32":
        # Determine system architecture
        machine = platform.machine()
        if machine in ["AMD64", "x86_64"]:
            architecture = "X64"
        elif machine == "ARM64":
            architecture = "ARM64"
        elif machine in ["i386", "i686"]:
            architecture = "X86"
        else:
            print(f"Unsupported architecture: {machine}")
            return

        download_url = vc_redist_links.get(architecture)
        if not download_url:
            print(f"Unsupported architecture: {architecture}")
            return

        # Save the installer to a temporary directory
        temp_dir = tempfile.gettempdir()
        installer_path = os.path.join(temp_dir, f"vc_redist_{architecture}.exe")
        
        try:
            print(f"Downloading Visual C++ Redistributable for {architecture}...")
            urllib.request.urlretrieve(download_url, installer_path)
            print(f"Downloaded to {installer_path}")

            # Run the installer
            print("Running the installer...")
            subprocess.check_call([installer_path, "/quiet", "/norestart"])
            print("Visual C++ Redistributable installed successfully.")
        except subprocess.CalledProcessError as e:
            if e.returncode == 3010:  # Exit code for "successful but restart required"
                print("Installation successful, but a system reboot is required to complete the process.")
                needs_restart = True
            else:
                print(f"An error occurred: {e}")
                print("Please manually download and install it from:")
                for arch, link in vc_redist_links.items():
                    print(f"{arch}: {link}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Clean up downloaded file
            if os.path.exists(installer_path):
                os.remove(installer_path)
            return needs_restart 
    else:
        print("This script is only compatible with Windows.")
    return needs_restart 

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
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "--no-cache-dir", package])
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
    needs_restart = False  # Initialize the variable
    # Ensure pip and setuptools are upgraded
    try:
        print("Upgrading pip and setuptools...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools"])
        print("Pip and setuptools upgraded successfully.")
    except subprocess.CalledProcessError:
        print("Failed to upgrade pip and setuptools.")

    # Install Visual C++ Redistributables if on Windows
    needs_restart = install_visual_c_redistributable()

    # Check and fix libraries
    check_libraries(required_libraries)

    print("All libraries checked, uninstalled, and reinstalled if necessary.")
    # Inform the user if a restart is needed
    if needs_restart:
        print("\nIMPORTANT: A system restart is required to complete the installation.")
    else:
        print("\nInstallation of C++ Redistributables does not require a restart.")
    input("Press Enter to close...")

if __name__ == "__main__":
    main()

