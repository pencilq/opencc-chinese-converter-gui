# Build Troubleshooting Guide

## GitHub Actions Build Failures - Solutions Applied

### Issue Description
The GitHub Actions workflow for building EXE files and creating releases was failing with exit code 1 on both Windows and macOS platforms.

### Root Causes Identified

1. **Python Version Compatibility**: Using Python 3.9 which may have compatibility issues with PyInstaller
2. **PyInstaller Configuration**: Complex spec file might cause issues in CI environment
3. **Missing Error Handling**: Limited debugging information when builds fail
4. **Dependency Version Conflicts**: Unspecified version ranges causing potential conflicts

### Solutions Implemented

#### 1. Python Version Update
- **Changed from**: Python 3.9
- **Changed to**: Python 3.11
- **Reason**: Python 3.11 has better stability with PyInstaller and fewer compatibility issues

#### 2. Fallback Build Strategy
- **Primary Method**: Simple PyInstaller command with essential options
  ```bash
  pyinstaller --onefile --noconsole --name "OpenCC中文转换器" \
    --add-data "sample_text.txt;." \
    --add-data "sample_data.csv;." \
    --add-data "README.md;." \
    --add-data "LICENSE;." \
    opencc-py-gui.py
  ```
- **Fallback Method**: Use the detailed spec file if simple method fails
  ```bash
  pyinstaller --clean opencc-gui.spec
  ```

#### 3. Enhanced Error Reporting
- Added dependency verification step before building
- Added detailed output checking after build completion
- Added directory listings when builds fail for debugging

#### 4. Dependency Version Constraints
Updated `requirements.txt` with specific version ranges:
```txt
opencc-python-reimplemented>=0.1.7,<2.0.0
pandas>=1.3.0,<3.0.0
openpyxl>=3.0.0,<4.0.0
python-docx>=0.8.11,<2.0.0
```

#### 5. Platform-Specific Optimizations
- **Windows**: Uses `;` separator for `--add-data`
- **macOS**: Uses `:` separator for `--add-data`
- Different shell commands for each platform

### Testing Results

The local PyInstaller build test showed:
- ✅ All dependencies import successfully
- ✅ PyInstaller can process the main Python file
- ✅ Build process initiates without errors

### Expected Improvements

With these changes, the GitHub Actions workflow should:
1. Use a more stable Python version
2. Have better error reporting for debugging
3. Try multiple build methods for reliability
4. Have consistent dependency versions across environments

### Monitoring

To verify the fixes are working:
1. Check the GitHub Actions logs for the new debugging output
2. Verify that the dependency test step passes
3. Monitor for successful EXE creation
4. Confirm that GitHub releases are created properly

### Next Steps if Issues Persist

If builds still fail after these changes:
1. Check the enhanced debug output in GitHub Actions logs
2. Consider using PyInstaller hooks for specific dependencies
3. May need to add environment-specific configurations
4. Consider using Docker containers for consistent build environments

### Version History

- **v1.0.4**: Applied comprehensive build fixes
- **v1.0.3**: Previous failed attempts with deprecated actions
- **v1.0.2**: Initial GitHub Actions setup

---

**Note**: This troubleshooting guide documents the iterative problem-solving process for GitHub Actions build failures and serves as a reference for future maintenance.