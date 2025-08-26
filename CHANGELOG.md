# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release preparation
- GitHub-ready documentation
- Professional README with badges and comprehensive documentation
- LICENSE file (Apache 2.0)
- .gitignore for Python projects

## [1.0.0] - 2024-08-26

### Added
- **Core Features**
  - GUI application for OpenCC Chinese text conversion
  - Support for Excel (.xlsx, .xls), Word (.docx), and Text (.txt) files
  - Multi-layer conversion settings (source/target language, character variants, vocabulary)
  - Real-time preview functionality
  - Progress tracking for large files
  - Multi-column selection for Excel files
  - Direct text input and conversion
  - Automatic console window hiding on Windows

- **User Interface**
  - Two-column layout design
  - Chinese language interface
  - Cascadia Code font with 黑体 fallback
  - Responsive design with proper grid layout
  - Visual separator between input and preview areas

- **Technical Implementation**
  - Threading for non-blocking file conversion
  - Comprehensive error handling and validation
  - Automatic file type detection
  - Cross-platform compatibility
  - Memory-efficient file processing

- **Conversion Modes**
  - Basic: Simplified ⟷ Traditional Chinese
  - Regional: Taiwan Standard, Hong Kong Standard
  - Advanced: Phrase conversion support
  - Character variant normalization

- **File Processing**
  - Excel: Column-specific conversion with format preservation
  - Word: Paragraph and table text conversion
  - Text: Full content conversion with UTF-8 support
  - Automatic output file naming with conversion mode suffix

- **Documentation**
  - Comprehensive README with usage instructions
  - Layout documentation (LAYOUT.md)
  - Sample files for testing
  - Installation and troubleshooting guides

### Technical Details
- Python 3.7+ compatibility
- Dependencies: opencc-python-reimplemented, pandas, openpyxl, python-docx
- GUI framework: tkinter (cross-platform)
- Console management for Windows systems
- Error-safe API calls with graceful fallbacks

### Known Issues
- None reported in initial release

---

**Note**: This changelog will be updated with each release. For the complete list of changes, see the [commit history](https://github.com/yourusername/opencc-chinese-converter-gui/commits/).