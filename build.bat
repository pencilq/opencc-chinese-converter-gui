@echo off
echo ==========================================
echo OpenCC 中文转换器 - 本地构建脚本
echo ==========================================
echo.

echo [1/5] 检查 Python 环境...
python --version
if %errorlevel% neq 0 (
    echo 错误：未找到 Python，请确保已安装 Python 3.7+
    pause
    exit /b 1
)
echo.

echo [2/5] 安装依赖包...
pip install -r requirements.txt
pip install pyinstaller
if %errorlevel% neq 0 (
    echo 错误：依赖安装失败
    pause
    exit /b 1
)
echo.

echo [3/5] 清理旧的构建文件...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
echo.

echo [4/5] 构建可执行文件...
echo 使用 PyInstaller 构建，这可能需要几分钟...
pyinstaller --clean opencc-gui.spec
if %errorlevel% neq 0 (
    echo 错误：构建失败
    pause
    exit /b 1
)
echo.

echo [5/5] 创建发布包...
mkdir "OpenCC中文转换器-Windows" 2>nul
copy "dist\OpenCC中文转换器.exe" "OpenCC中文转换器-Windows\"
copy "README.md" "OpenCC中文转换器-Windows\"
copy "LICENSE" "OpenCC中文转换器-Windows\"
copy "sample_text.txt" "OpenCC中文转换器-Windows\"
copy "sample_data.csv" "OpenCC中文转换器-Windows\"

echo OpenCC 中文转换器 - Windows 便携版 > "OpenCC中文转换器-Windows\使用说明.txt"
echo. >> "OpenCC中文转换器-Windows\使用说明.txt"
echo 使用方法： >> "OpenCC中文转换器-Windows\使用说明.txt"
echo 1. 双击 OpenCC中文转换器.exe 启动程序 >> "OpenCC中文转换器-Windows\使用说明.txt"
echo 2. 选择要转换的文件或直接输入文本 >> "OpenCC中文转换器-Windows\使用说明.txt"
echo 3. 配置转换设置（简体/繁体、地区标准等） >> "OpenCC中文转换器-Windows\使用说明.txt"
echo 4. 点击转换按钮开始处理 >> "OpenCC中文转换器-Windows\使用说明.txt"
echo. >> "OpenCC中文转换器-Windows\使用说明.txt"
echo 支持的文件格式： >> "OpenCC中文转换器-Windows\使用说明.txt"
echo - Excel文件 (.xlsx, .xls) >> "OpenCC中文转换器-Windows\使用说明.txt"
echo - Word文档 (.docx) >> "OpenCC中文转换器-Windows\使用说明.txt"
echo - 文本文件 (.txt) >> "OpenCC中文转换器-Windows\使用说明.txt"
echo. >> "OpenCC中文转换器-Windows\使用说明.txt"
echo 更多信息请查看 README.md 文件。 >> "OpenCC中文转换器-Windows\使用说明.txt"

echo.
echo ==========================================
echo 构建完成！
echo ==========================================
echo.
echo 生成的文件：
echo - 可执行文件：dist\OpenCC中文转换器.exe
echo - 发布包文件夹：OpenCC中文转换器-Windows\
echo.
echo 现在可以测试运行 dist\OpenCC中文转换器.exe
echo.
pause