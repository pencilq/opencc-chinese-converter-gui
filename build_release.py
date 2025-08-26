#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local Release Builder for OpenCC Chinese Converter GUI
本地发布构建器 - OpenCC 中文转换器 GUI

This script builds executables locally for manual upload to GitHub Releases.
此脚本在本地构建可执行文件，用于手动上传到 GitHub Releases。

Usage / 使用方法:
    python build_release.py

Requirements / 依赖:
    pip install pyinstaller
"""

import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path

def print_step(message):
    """打印步骤信息"""
    print(f"\n{'='*50}")
    print(f"🔧 {message}")
    print(f"{'='*50}")

def run_command(cmd, description):
    """运行命令并显示结果"""
    print(f"\n▶️ {description}")
    print(f"💻 执行命令: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True, encoding='utf-8')
        print(f"✅ 成功: {description}")
        if result.stdout:
            print(f"📄 输出: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 失败: {description}")
        print(f"🚨 错误: {e}")
        if e.stdout:
            print(f"📄 标准输出: {e.stdout}")
        if e.stderr:
            print(f"📄 错误输出: {e.stderr}")
        return False

def check_dependencies():
    """检查依赖项"""
    print_step("检查依赖项")
    
    # 检查 Python 版本
    python_version = sys.version_info
    print(f"🐍 Python 版本: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 7):
        print("❌ 需要 Python 3.7 或更高版本")
        return False
    
    # 检查必要的包
    required_packages = [
        ('opencc', 'opencc'),
        ('pandas', 'pandas'), 
        ('openpyxl', 'openpyxl'),
        ('docx', 'docx'),
        ('PyInstaller', 'PyInstaller')
    ]
    
    for display_name, import_name in required_packages:
        try:
            __import__(import_name.lower().replace('-', '_'))
            print(f"✅ {display_name}: 已安装")
        except ImportError:
            print(f"❌ {display_name}: 未安装")
            print(f"💡 请运行: pip install {display_name}")
            return False
    
    return True

def build_executable():
    """构建可执行文件"""
    print_step("构建可执行文件")
    
    # 清理之前的构建
    if os.path.exists('dist'):
        print("🧹 清理旧的构建文件...")
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    
    # 获取系统信息
    system = platform.system()
    arch = platform.machine()
    print(f"🖥️ 系统: {system} {arch}")
    
    # 根据系统选择构建命令
    if system == "Windows":
        separator = ";"
        exe_name = "OpenCC中文转换器.exe"
    else:
        separator = ":"
        exe_name = "OpenCC中文转换器"
    
    # PyInstaller 命令
    cmd = f"""pyinstaller --onefile --noconsole --name "OpenCC中文转换器" \
--add-data "sample_text.txt{separator}." \
--add-data "sample_data.csv{separator}." \
--add-data "README.md{separator}." \
--add-data "LICENSE{separator}." \
opencc-py-gui.py"""
    
    if not run_command(cmd, "运行 PyInstaller"):
        return False
    
    # 检查生成的文件
    exe_path = Path("dist") / exe_name
    if exe_path.exists():
        size = exe_path.stat().st_size / (1024 * 1024)  # MB
        print(f"✅ 可执行文件已生成: {exe_path}")
        print(f"📏 文件大小: {size:.1f} MB")
        return True
    else:
        print(f"❌ 可执行文件未找到: {exe_path}")
        return False

def create_release_package():
    """创建发布包"""
    print_step("创建发布包")
    
    system = platform.system()
    arch = platform.machine()
    
    if system == "Windows":
        package_name = f"OpenCC中文转换器-Windows-{arch}"
        exe_name = "OpenCC中文转换器.exe"
    elif system == "Darwin":
        package_name = f"OpenCC中文转换器-macOS-{arch}"
        exe_name = "OpenCC中文转换器"
    else:
        package_name = f"OpenCC中文转换器-Linux-{arch}"
        exe_name = "OpenCC中文转换器"
    
    # 创建包目录
    package_dir = Path(package_name)
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir()
    
    # 复制文件
    files_to_copy = [
        (f"dist/{exe_name}", exe_name),
        ("README.md", "README.md"),
        ("LICENSE", "LICENSE"),
        ("sample_text.txt", "sample_text.txt"),
        ("sample_data.csv", "sample_data.csv"),
        ("CHANGELOG.md", "CHANGELOG.md")
    ]
    
    for src, dst in files_to_copy:
        src_path = Path(src)
        if src_path.exists():
            shutil.copy2(src_path, package_dir / dst)
            print(f"📄 复制: {src} -> {package_dir / dst}")
    
    # 创建说明文件
    readme_content = f"""OpenCC 中文转换器 - {system} 版

使用方法：
1. 双击 {exe_name} 启动程序
2. 选择要转换的文件或直接输入文本
3. 配置转换设置
4. 点击转换按钮开始处理

支持的文件格式：
- Excel文件 (.xlsx, .xls)
- Word文档 (.docx)
- 文本文件 (.txt)

技术支持：
- 项目主页: https://github.com/pencilq/opencc-chinese-converter-gui
- 问题反馈: https://github.com/pencilq/opencc-chinese-converter-gui/issues

版本信息：
- 系统: {system} {arch}
- 构建时间: {subprocess.check_output(['git', 'log', '-1', '--format=%ci'], encoding='utf-8').strip() if shutil.which('git') else '未知'}
"""
    
    with open(package_dir / "使用说明.txt", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    # 创建压缩包
    if system == "Windows":
        archive_name = f"{package_name}.zip"
        run_command(f'powershell Compress-Archive -Path "{package_name}" -DestinationPath "{archive_name}"', "创建 ZIP 压缩包")
    else:
        archive_name = f"{package_name}.tar.gz"
        run_command(f'tar -czf "{archive_name}" "{package_name}"', "创建 TAR.GZ 压缩包")
    
    if Path(archive_name).exists():
        size = Path(archive_name).stat().st_size / (1024 * 1024)  # MB
        print(f"✅ 发布包已创建: {archive_name}")
        print(f"📏 压缩包大小: {size:.1f} MB")
        return archive_name
    else:
        print(f"❌ 发布包创建失败: {archive_name}")
        return None

def main():
    """主函数"""
    print("🚀 OpenCC 中文转换器 - 本地构建器")
    print("=" * 60)
    
    # 检查是否在正确的目录
    if not Path("opencc-py-gui.py").exists():
        print("❌ 错误: 未找到 opencc-py-gui.py")
        print("💡 请在项目根目录运行此脚本")
        return False
    
    # 执行构建步骤
    steps = [
        ("检查依赖项", check_dependencies),
        ("构建可执行文件", build_executable),
        ("创建发布包", create_release_package)
    ]
    
    for step_name, step_func in steps:
        if not step_func():
            print(f"\n❌ 构建失败于步骤: {step_name}")
            return False
    
    print_step("构建完成")
    print("🎉 所有步骤完成!")
    print("\n📋 下一步操作:")
    print("1. 在 GitHub 上创建新的 Release")
    print("2. 上传生成的压缩包文件")
    print("3. 填写 Release 说明")
    print("4. 发布 Release")
    
    # 显示生成的文件
    print(f"\n📁 生成的文件:")
    for item in Path(".").iterdir():
        if item.name.startswith("OpenCC中文转换器") and (item.suffix in ['.zip', '.tar.gz'] or item.is_dir()):
            print(f"  📦 {item.name}")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if success:
            input("\n按 Enter 键退出...")
        else:
            input("\n构建失败，按 Enter 键退出...")
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断构建")
    except Exception as e:
        print(f"\n❌ 意外错误: {e}")
        input("\n按 Enter 键退出...")