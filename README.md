# OpenCC Chinese Converter GUI

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)

一个简单易用的图形界面工具，用于在简体中文和繁体中文之间进行双向转换。支持 Excel、Word 和纯文本文件格式。

## 功能特点

- 🔄 双向转换：简体中文 ↔ 繁体中文
- 📄 多格式支持：Excel (.xlsx/.xls)、Word (.docx) 和纯文本 (.txt)
- 🎯 精确转换：支持香港、台湾等地区用字规范
- 🖥️ 图形界面：直观易用的用户界面
- 📊 列控制：Excel 文件支持列级转换控制
- ⚡ 实时预览：转换结果实时预览
- 📦 批量处理：支持大文件批量处理
- 🌐 跨平台：Windows、macOS 和 Linux 支持

## 安装

### 方法 1：使用预构建的可执行文件（推荐）

1. 访问 [GitHub Releases](https://github.com/pencilq/opencc-chinese-converter-gui/releases) 页面
2. 下载适用于您操作系统的最新版本
3. 解压并运行可执行文件

### 方法 2：从源代码运行

#### 系统要求
- Python 3.7 或更高版本
- Windows 7/8/10/11, macOS 10.12+, 或 Linux

#### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/pencilq/opencc-chinese-converter-gui.git
cd opencc-chinese-converter-gui

# 创建虚拟环境（推荐）
python -m venv opencc-env
# Windows:
opencc-env\Scripts\activate
# macOS/Linux:
source opencc-env/bin/activate

# 安装依赖
pip install -r requirements.txt

# 运行应用程序
python opencc-py-gui.py
```

## 使用方法

### 基本转换

1. 选择要转换的文件或直接在文本框中输入文本
2. 设置转换选项：
   - 原始文本：简体或繁体
   - 目标文本：简体或繁体
   - 变体字符：标准、香港标准、台湾标准
   - 词汇转换：启用/禁用专业词汇转换
3. 点击"转换"按钮
4. 预览结果并保存文件

### Excel 文件处理

1. 选择 Excel 文件
2. 选择要转换的列（支持多选）
3. 设置转换选项
4. 点击"转换"按钮
5. 保存转换后的文件

### Word 文件处理

1. 选择 Word 文件
2. 设置转换选项
3. 点击"转换"按钮
4. 保存转换后的文件

## 构建可执行文件

如果您希望从源代码构建自己的可执行文件：

```bash
# 安装构建工具
pip install pyinstaller

# 使用简单构建脚本
python simple_build.py
```

或者手动构建：

```bash
# Windows (隐藏控制台窗口)
pyinstaller --onefile --windowed --name "OpenCC-GUI" opencc-py-gui.py

# macOS/Linux
pyinstaller --onefile --name "OpenCC-GUI" opencc-py-gui.py
```

构建的可执行文件将位于 `dist/` 目录中。

## 开发

### 项目结构

```
opencc-chinese-converter-gui/
├── opencc-py-gui.py        # 主应用程序
├── requirements.txt        # Python 依赖
├── simple_build.py         # 简单构建脚本
├── BUILD_GUIDE.md          # 构建指南
├── BUILD_TROUBLESHOOTING.md # 构建故障排除
├── CHANGELOG.md            # 版本历史
├── LICENSE                 # 许可证
├── README.md               # 本文档
├── sample_data.csv         # 示例数据文件
├── sample_text.txt         # 示例文本文件
└── screenshots/            # 界面截图
```

### 技术栈

- **GUI 框架**: Tkinter (Python 内置)
- **转换引擎**: opencc-python-reimplemented
- **Excel 处理**: pandas + openpyxl
- **Word 处理**: python-docx
- **构建工具**: PyInstaller

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。

1. Fork 仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

本项目采用 Apache License 2.0 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 致谢

- [OpenCC](https://github.com/BYVoid/OpenCC) - 中文简繁转换工具
- [opencc-python](https://github.com/yichen0831/opencc-python) - OpenCC 的 Python 实现
- 所有贡献者和支持者
