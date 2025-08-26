#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub CLI Release Creator for OpenCC Chinese Converter GUI
GitHub CLI 发布创建器 - OpenCC 中文转换器 GUI

This script builds executables locally and creates GitHub releases using GitHub CLI.
此脚本在本地构建可执行文件并使用 GitHub CLI 创建 GitHub 发布。

Prerequisites / 先决条件:
1. Install GitHub CLI: https://cli.github.com/
2. Login to GitHub: gh auth login
3. Install PyInstaller: pip install pyinstaller

Usage / 使用方法:
    python release_with_gh_cli.py v1.0.5

Requirements / 依赖:
    pip install pyinstaller
    GitHub CLI installed and authenticated
"""

import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path
import argparse

def print_step(message):
    """打印步骤信息"""
    print(f"\n{'='*50}")
    print(f"🔧 {message}")
    print(f"{'='*50}")

def run_command(cmd, description, capture=True):
    """运行命令并显示结果"""
    print(f"\n▶️ {description}")
    print(f"💻 执行命令: {cmd}")
    
    try:
        if capture:
            result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True, encoding='utf-8')
            if result.stdout:
                print(f"📄 输出: {result.stdout.strip()}")
        else:
            result = subprocess.run(cmd, shell=True, check=True)
        
        print(f"✅ 成功: {description}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 失败: {description}")
        print(f"🚨 错误: {e}")
        if hasattr(e, 'stdout') and e.stdout:
            print(f"📄 标准输出: {e.stdout}")
        if hasattr(e, 'stderr') and e.stderr:
            print(f"📄 错误输出: {e.stderr}")
        return False

def check_prerequisites():
    """检查先决条件"""
    print_step("检查先决条件")
    
    # 检查 GitHub CLI
    if not shutil.which('gh'):
        print("❌ 未找到 GitHub CLI")
        print("💡 请安装 GitHub CLI: https://cli.github.com/")
        return False
    
    # 检查 GitHub CLI 认证状态
    try:
        result = subprocess.run(['gh', 'auth', 'status'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ GitHub CLI 未认证")
            print("💡 请运行: gh auth login")
            return False
        print("✅ GitHub CLI 已认证")
    except Exception as e:
        print(f"❌ 检查 GitHub CLI 认证失败: {e}")
        return False
    
    # 检查 PyInstaller
    try:
        import PyInstaller
        print("✅ PyInstaller 已安装")
    except ImportError:
        print("❌ PyInstaller 未安装")
        print("💡 请运行: pip install pyinstaller")
        return False
    
    # 检查必要文件
    required_files = ['opencc-py-gui.py', 'requirements.txt', 'README.md', 'LICENSE']
    for file in required_files:
        if not Path(file).exists():
            print(f"❌ 缺少必要文件: {file}")
            return False
        print(f"✅ 找到文件: {file}")
    
    return True

def build_executables():
    """构建可执行文件"""
    print_step("构建可执行文件")
    
    # 清理之前的构建
    for dir_name in ['dist', 'build']:
        if os.path.exists(dir_name):
            print(f"🧹 清理 {dir_name} 目录...")
            shutil.rmtree(dir_name)
    
    # 构建可执行文件
    system = platform.system()
    if system == "Windows":
        separator = ";"
        exe_name = "OpenCC中文转换器.exe"
    else:
        separator = ":"
        exe_name = "OpenCC中文转换器"
    
    cmd = f"""pyinstaller --onefile --noconsole --name "OpenCC中文转换器" \
--add-data "sample_text.txt{separator}." \
--add-data "sample_data.csv{separator}." \
--add-data "README.md{separator}." \
--add-data "LICENSE{separator}." \
opencc-py-gui.py"""
    
    if not run_command(cmd, "构建可执行文件"):
        return False
    
    # 验证输出
    exe_path = Path("dist") / exe_name
    if exe_path.exists():
        size = exe_path.stat().st_size / (1024 * 1024)  # MB
        print(f"✅ 可执行文件已生成: {exe_path}")
        print(f"📏 文件大小: {size:.1f} MB")
        return exe_path
    else:
        print(f"❌ 可执行文件未找到: {exe_path}")
        return False

def create_release_notes(version):
    """生成发布说明"""
    notes = f"""## OpenCC 中文转换器 {version}

### 📥 下载说明

#### Windows 用户
- 下载 `OpenCC中文转换器.exe`
- 双击运行，无需安装

#### macOS 用户  
- 下载 `OpenCC中文转换器`
- 首次运行可能需要在系统偏好设置中允许运行未签名应用

### ✨ 主要功能

- 🔄 支持简体/繁体中文互转
- 📊 支持 Excel、Word、文本文件批量转换
- 🎯 Excel 多列选择转换
- 👀 实时预览转换结果
- 🚀 快速直接文本转换
- 🎨 清晰的两栏式界面设计

### 📋 系统要求

- **Windows**: Windows 10/11 (64位)
- **macOS**: macOS 10.14+ (64位)
- **内存**: 建议 4GB 以上
- **磁盘空间**: 100MB 可用空间

### 🐛 问题反馈

如遇到问题，请在 [Issues](https://github.com/pencilq/opencc-chinese-converter-gui/issues) 中反馈。

### 🔄 转换模式

支持以下转换模式：
- 简体中文 → 繁体中文
- 繁体中文 → 简体中文  
- 简体中文 → 台湾繁体
- 简体中文 → 香港繁体
- 台湾繁体 → 简体中文
- 香港繁体 → 简体中文
- 繁体中文 → 台湾繁体
- 繁体中文 → 香港繁体

### 📝 使用指南

1. **选择文件**: 点击"浏览"选择要转换的文件
2. **设置转换**: 选择源语言和目标语言
3. **预览结果**: 在右侧预览区查看转换效果
4. **开始转换**: 点击"转换文件"处理整个文档
5. **直接文本**: 也可直接在文本框中输入并转换

---

感谢使用 OpenCC 中文转换器！
"""
    return notes

def create_github_release(version, exe_path):
    """使用 GitHub CLI 创建发布"""
    print_step(f"创建 GitHub Release: {version}")
    
    # 生成发布说明
    release_notes = create_release_notes(version)
    
    # 将发布说明写入临时文件
    notes_file = Path("release_notes.md")
    with open(notes_file, 'w', encoding='utf-8') as f:
        f.write(release_notes)
    
    # 创建 release
    cmd = f'gh release create {version} "{exe_path}" --title "OpenCC 中文转换器 {version}" --notes-file "{notes_file}"'
    
    success = run_command(cmd, f"创建 GitHub Release {version}", capture=False)
    
    # 清理临时文件
    if notes_file.exists():
        notes_file.unlink()
    
    if success:
        print(f"\n🎉 Release {version} 创建成功!")
        print(f"🔗 查看 Release: https://github.com/pencilq/opencc-chinese-converter-gui/releases/tag/{version}")
    
    return success

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='创建 OpenCC 中文转换器 GitHub Release')
    parser.add_argument('version', help='版本号 (例如: v1.0.5)')
    args = parser.parse_args()
    
    version = args.version
    if not version.startswith('v'):
        version = f'v{version}'
    
    print("🚀 OpenCC 中文转换器 - GitHub Release 创建器")
    print("=" * 60)
    print(f"📋 准备创建版本: {version}")
    
    # 检查是否在正确的目录
    if not Path("opencc-py-gui.py").exists():
        print("❌ 错误: 未找到 opencc-py-gui.py")
        print("💡 请在项目根目录运行此脚本")
        return False
    
    # 执行步骤
    steps = [
        ("检查先决条件", check_prerequisites),
        ("构建可执行文件", build_executables)
    ]
    
    exe_path = None
    for step_name, step_func in steps:
        result = step_func()
        if not result:
            print(f"\n❌ 失败于步骤: {step_name}")
            return False
        elif step_name == "构建可执行文件":
            exe_path = result
    
    # 创建 GitHub Release
    if not create_github_release(version, exe_path):
        print(f"\n❌ 创建 Release 失败")
        return False
    
    print_step("完成")
    print("🎉 所有步骤完成!")
    print(f"✅ Release {version} 已成功创建并发布到 GitHub")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断操作")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 意外错误: {e}")
        sys.exit(1)