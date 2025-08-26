# OpenCC Chinese Converter GUI

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

A modern, user-friendly graphical interface for converting Chinese text between Simplified and Traditional Chinese using OpenCC (Open Chinese Convert). This application provides comprehensive file format support with an intuitive GUI for batch text conversion.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Guide](#usage-guide)
- [Supported File Formats](#supported-file-formats)
- [Conversion Modes](#conversion-modes)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Features

### Core Functionality
- **Multi-format Support**: Excel (.xlsx, .xls), Word (.docx), and Text (.txt) files
- **Column-level Control**: Select specific Excel columns for conversion
- **Real-time Preview**: Preview conversion results before processing
- **Batch Processing**: Convert entire documents while preserving formatting
- **Progress Tracking**: Real-time progress updates for large files

### User Experience
- **Intuitive Interface**: Clean two-column layout with logical workflow
- **Auto-detection**: Automatic file type detection and output naming
- **Multi-layer Settings**: Granular control over conversion parameters
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Console-free**: Automatic console window hiding on Windows

### Advanced Features
- **Multi-column Selection**: Convert multiple Excel columns simultaneously
- **Format Preservation**: Maintains document structure and formatting
- **Error Handling**: Comprehensive validation and user feedback
- **Direct Text Input**: Convert text without file operations
- **Threaded Processing**: Non-blocking conversion for large files

## Installation

### System Requirements

- Python 3.7 or higher
- Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- 100MB free disk space

### Method 1: Clone from GitHub (Recommended)

```bash
# Clone the repository
git clone https://github.com/pencilq/opencc-chinese-converter-gui.git
cd opencc-chinese-converter-gui

# Install dependencies
pip install -r requirements.txt

# Run the application
python opencc-py-gui.py
```

### Method 2: Manual Installation

1. **Download the source code**
   - Download and extract the ZIP file from GitHub
   - Or clone using Git as shown above

2. **Install Python dependencies**
   ```bash
   pip install opencc-python-reimplemented pandas openpyxl python-docx
   ```

3. **Verify installation**
   ```bash
   python -c "import opencc, pandas, openpyxl, docx; print('All dependencies installed successfully')"
   ```

### Troubleshooting Installation

If you encounter issues, try installing dependencies individually:

```bash
pip install opencc-python-reimplemented
pip install pandas
pip install openpyxl
pip install python-docx
```

For Python environment issues, consider using virtual environments:

```bash
python -m venv opencc-env
source opencc-env/bin/activate  # On Windows: opencc-env\Scripts\activate
pip install -r requirements.txt
```

## Quick Start

1. **Launch the application**
   ```bash
   python opencc-py-gui.py
   ```

2. **Convert a file**
   - Click "Browse" to select your input file
   - Choose conversion settings (source/target language)
   - Preview the conversion result
   - Click "Convert File" to process

3. **Convert text directly**
   - Enter text in the "Direct Text Input" area
   - Select conversion mode
   - View results in the preview area
   - Copy the converted text

## Usage Guide

### Interface Overview

The application features a clean two-column layout:
- **Left Column**: File selection, conversion settings, and controls
- **Right Column**: Preview area and progress tracking

### Step-by-Step Workflow

#### File-based Conversion

1. **Select Input File**
   - Click "Browse" next to "Input File"
   - Choose your Excel, Word, or text file
   - The application auto-detects file type

2. **Configure Conversion Settings**
   - **Source Language**: Choose "Simplified" or "Traditional"
   - **Target Language**: Choose "Simplified" or "Traditional" 
   - **Character Variant**: Select standard (OpenCC, Hong Kong, Taiwan)
   - **Local Vocabulary**: Enable/disable phrase conversion

3. **Column Selection (Excel only)**
   - Select which columns contain Chinese text
   - Use "Select All" or "Deselect All" for convenience
   - Preview shows selected column count

4. **Preview and Convert**
   - Review conversion results in the preview area
   - Click "Convert File" to process the entire document
   - Monitor progress with the progress bar

#### Direct Text Conversion

1. **Enter Text**
   - Type or paste Chinese text in the input area
   - Text automatically triggers preview

2. **Select Conversion Mode**
   - Choose appropriate source and target settings
   - View real-time conversion results

3. **Copy Results**
   - Click "Copy" to copy converted text to clipboard
   - No file operations needed

## Supported File Formats

### Excel Files (.xlsx, .xls)
- **Column Selection**: Choose specific columns for conversion
- **Format Preservation**: Maintains cell formatting, formulas, and structure
- **Multi-column Support**: Convert multiple columns simultaneously
- **Output**: Excel format (.xlsx) with UTF-8 encoding

### Word Documents (.docx)
- **Comprehensive Conversion**: Processes paragraphs and table content
- **Structure Preservation**: Maintains document formatting and layout
- **Table Support**: Converts text within tables
- **Output**: Word format (.docx) with original formatting

### Text Files (.txt)
- **Full Content Conversion**: Processes entire file content
- **Encoding Support**: UTF-8 input and output
- **Line Break Preservation**: Maintains original text structure
- **Output**: Plain text (.txt) with UTF-8 encoding

## Conversion Modes

### Basic Conversions
| Mode | Description | Example |
|------|-------------|----------|
| `s2t` | Simplified to Traditional Chinese | 简体 → 繁體 |
| `t2s` | Traditional to Simplified Chinese | 繁體 → 简体 |

### Regional Standards
| Mode | Description | Use Case |
|------|-------------|----------|
| `s2tw` | Simplified to Traditional (Taiwan) | Mainland → Taiwan |
| `tw2s` | Traditional (Taiwan) to Simplified | Taiwan → Mainland |
| `s2hk` | Simplified to Traditional (Hong Kong) | Mainland → Hong Kong |
| `hk2s` | Traditional (Hong Kong) to Simplified | Hong Kong → Mainland |

### Advanced Conversions
| Mode | Description | Features |
|------|-------------|----------|
| `s2twp` | Simplified to Traditional (Taiwan + Phrases) | Includes vocabulary conversion |
| `tw2sp` | Traditional (Taiwan) to Simplified + Phrases | Includes vocabulary conversion |
| `t2tw` | Traditional to Traditional (Taiwan) | Character variant normalization |
| `t2hk` | Traditional to Traditional (Hong Kong) | Character variant normalization |

## Screenshots

### Main Interface
The application features a clean, professional interface with logical workflow:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           OpenCC Chinese Converter                       │
├─────────────────────────────┬───┬─────────────────────────────────────────┤
│         LEFT COLUMN         │ │ │            RIGHT COLUMN                 │
│      (Input & Controls)     │ │ │        (Preview & Output)               │
│                             │ │ │                                         │
│ • File Selection            │ │ │ • Real-time Preview                     │
│ • Conversion Settings       │ │ │ • Progress Tracking                     │
│ • Column Selection          │ │ │ • Copy Functionality                    │
│ • Action Buttons            │ │ │                                         │
└─────────────────────────────┴───┴─────────────────────────────────────────┘
```

### Key Features Demonstration
- **Two-column Layout**: Organized workflow from left to right
- **Real-time Preview**: Immediate feedback on conversion results
- **Progress Tracking**: Visual progress bar for large file operations
- **Professional Appearance**: Clean interface without console windows

## Contributing

We welcome contributions to improve this project! Here's how you can help:

### Reporting Issues

1. **Check existing issues** before creating a new one
2. **Use the issue template** and provide detailed information:
   - Operating system and Python version
   - Steps to reproduce the problem
   - Expected vs actual behavior
   - Error messages or screenshots

### Submitting Pull Requests

1. **Fork the repository** and create a feature branch
2. **Make your changes** with clear, descriptive commits
3. **Add tests** for new functionality
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description

### Development Setup

```bash
# Clone your fork
git clone https://github.com/pencilq/opencc-chinese-converter-gui.git
cd opencc-chinese-converter-gui

# Create development environment
python -m venv dev-env
source dev-env/bin/activate  # On Windows: dev-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest
```

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings for new functions and classes
- Keep functions focused and modular

## Troubleshooting

### Common Issues

#### Installation Problems

**Issue**: `ImportError: No module named 'opencc'`
```bash
# Solution: Install the correct OpenCC package
pip uninstall opencc
pip install opencc-python-reimplemented
```

**Issue**: Excel files not opening
```bash
# Solution: Install Excel support
pip install openpyxl
```

**Issue**: Word documents not processing
```bash
# Solution: Install Word document support
pip install python-docx
```

#### Runtime Issues

**Issue**: Application crashes on startup
- Verify Python version (3.7+ required)
- Check all dependencies are installed
- Try running from command line to see error messages

**Issue**: Console window appears on Windows
- This is expected behavior when running from command line
- The console automatically hides when launched normally

**Issue**: Conversion results are incorrect
- Verify input text contains Chinese characters
- Try different conversion modes
- Check if source/target languages are set correctly

#### File Processing Issues

**Issue**: "File encoding error"
- Ensure text files are UTF-8 encoded
- Try opening the file in a text editor and saving as UTF-8

**Issue**: "Permission denied" error
- Check file/folder permissions
- Ensure output directory is writable
- Close the output file if it's open in another application

**Issue**: Excel column selection not working
- Verify the Excel file has actual data
- Check if columns contain Chinese text
- Try selecting different columns

### Getting Help

If you're still experiencing issues:

1. **Check the [Issues](https://github.com/pencilq/opencc-chinese-converter-gui/issues) ** page
2. **Create a new issue** with detailed information
3. **Include error messages** and system information

## Technical Documentation

### Architecture Overview

- **GUI Framework**: Tkinter (cross-platform, included with Python)
- **Conversion Engine**: OpenCC (Open Chinese Convert)
- **File Processing**: Pandas (Excel), python-docx (Word)
- **Threading**: Background processing for large files
- **Error Handling**: Comprehensive validation and user feedback

### Project Structure

```
opencc-chinese-converter-gui/
├── opencc-py-gui.py          # Main application file
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── LAYOUT.md                 # GUI layout documentation
├── sample_text.txt           # Sample files for testing
├── sample_data.xlsx          # 
└── sample_document.docx      # 
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|----------|
| opencc-python-reimplemented | ≥0.1.7 | Chinese text conversion engine |
| pandas | ≥1.3.0 | Excel file processing and data manipulation |
| openpyxl | ≥3.0.0 | Excel file read/write operations |
| python-docx | ≥0.8.11 | Word document processing |
| tkinter | Built-in | GUI framework (included with Python) |

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

### Third-party Licenses

- **OpenCC**: Licensed under Apache License 2.0
- **Pandas**: Licensed under BSD 3-Clause License
- **openpyxl**: Licensed under MIT License
- **python-docx**: Licensed under MIT License

## Acknowledgments

- **OpenCC Project**: BYVoid and contributors for the excellent Chinese conversion library
- **Python Community**: For the amazing ecosystem of libraries
- **Contributors**: Everyone who has helped improve this project

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

---

**Made with ❤️ for the Chinese text processing community**