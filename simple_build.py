#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple build script for OpenCC-Py-GUI
This script creates a standalone executable using PyInstaller
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import PyInstaller
        print("✓ PyInstaller is installed")
    except ImportError:
        print("✗ PyInstaller is not installed")
        print("Please install it with: pip install pyinstaller")
        return False
    
    try:
        import opencc
        print("✓ OpenCC is installed")
    except ImportError:
        print("✗ OpenCC is not installed")
        print("Please install it with: pip install opencc-python-reimplemented")
        return False
    
    return True

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable...")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",  # Hide console window
        "--name", "OpenCC-GUI",
        "--icon", "NONE",  # No icon for now
        "opencc-py-gui.py"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("✓ Build completed successfully")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("✗ Build failed")
        print("Error output:")
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("✗ PyInstaller not found. Please install it with: pip install pyinstaller")
        return False

def copy_to_dist():
    """Copy the built executable to a dist folder"""
    dist_path = Path("dist")
    dist_path.mkdir(exist_ok=True)
    
    # Look for the built executable
    build_path = Path("dist") / "OpenCC-GUI.exe"  # Windows
    if build_path.exists():
        shutil.copy2(build_path, dist_path / "OpenCC-Chinese-Converter.exe")
        print(f"✓ Executable copied to {dist_path / 'OpenCC-Chinese-Converter.exe'}")
        return True
    else:
        print("✗ Built executable not found")
        return False

def main():
    """Main function"""
    print("OpenCC-Py-GUI Simple Build Script")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Clean previous builds
    print("Cleaning previous builds...")
    for folder in ["build", "dist"]:
        if Path(folder).exists():
            shutil.rmtree(folder)
            print(f"✓ Removed {folder} folder")
    
    # Build executable
    if not build_executable():
        sys.exit(1)
    
    # Copy to dist
    if not copy_to_dist():
        sys.exit(1)
    
    print("\n" + "=" * 40)
    print("Build completed successfully!")
    print("Executable location: dist/OpenCC-Chinese-Converter.exe")
    print("=" * 40)

if __name__ == "__main__":
    main()