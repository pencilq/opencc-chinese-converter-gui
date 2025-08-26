# OpenCC 中文转换器 GUI

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

一个现代化、用户友好的图形界面应用程序，使用 OpenCC（开放中文转换）在简体中文和繁体中文之间进行文本转换。本应用程序提供全面的文件格式支持，具有直观的 GUI 界面，可进行批量文本转换。

## 目录

- [功能特性](#功能特性)
- [安装方法](#安装方法)
- [快速开始](#快速开始)
- [使用指南](#使用指南)
- [支持的文件格式](#支持的文件格式)
- [转换模式](#转换模式)
- [界面截图](#界面截图)
- [贡献指南](#贡献指南)
- [故障排除](#故障排除)
- [许可证](#许可证)

## 功能特性

### 核心功能
- **多格式支持**：Excel (.xlsx, .xls)、Word (.docx) 和文本 (.txt) 文件
- **列级控制**：选择特定的 Excel 列进行转换
- **实时预览**：处理前预览转换结果
- **批量处理**：转换整个文档同时保持格式
- **进度跟踪**：大文件的实时进度更新

### 用户体验
- **直观界面**：清晰的两列布局，逻辑工作流程
- **自动检测**：自动文件类型检测和输出命名
- **多层设置**：对转换参数的精细控制
- **跨平台**：适用于 Windows、macOS 和 Linux
- **无控制台**：Windows 上自动隐藏控制台窗口

### 高级功能
- **多列选择**：同时转换多个 Excel 列
- **格式保持**：维护文档结构和格式
- **错误处理**：全面的验证和用户反馈
- **直接文本输入**：无需文件操作即可转换文本
- **线程处理**：大文件的非阻塞转换

## 安装方法

### 系统要求

- Python 3.7 或更高版本
- Windows 10/11、macOS 10.14+ 或 Linux (Ubuntu 18.04+)
- 100MB 可用磁盘空间

### 方法一：从 GitHub 克隆（推荐）

```bash
# 克隆仓库
git clone https://github.com/pencilq/opencc-chinese-converter-gui.git
cd opencc-chinese-converter-gui

# 安装依赖
pip install -r requirements.txt

# 运行应用程序
python opencc-py-gui.py
```

### 方法二：手动安装

1. **下载源代码**
   - 从 GitHub 下载并解压 ZIP 文件
   - 或使用上述 Git 克隆方法

2. **安装 Python 依赖**
   ```bash
   pip install opencc-python-reimplemented pandas openpyxl python-docx
   ```

3. **验证安装**
   ```bash
   python -c "import opencc, pandas, openpyxl, docx; print('所有依赖项已成功安装')"
   ```

### 安装故障排除

如果遇到问题，请尝试单独安装依赖项：

```bash
pip install opencc-python-reimplemented
pip install pandas
pip install openpyxl
pip install python-docx
```

对于 Python 环境问题，建议使用虚拟环境：

```bash
python -m venv opencc-env
source opencc-env/bin/activate  # Windows 上：opencc-env\Scripts\activate
pip install -r requirements.txt
```

## 快速开始

1. **启动应用程序**
   ```bash
   python opencc-py-gui.py
   ```

2. **转换文件**
   - 点击"浏览"选择输入文件
   - 选择转换设置（源语言/目标语言）
   - 预览转换结果
   - 点击"转换文件"开始处理

3. **直接转换文本**
   - 在"直接文本输入"区域输入文本
   - 选择转换模式
   - 在预览区域查看结果
   - 复制转换后的文本

## 使用指南

### 界面概览

应用程序采用清晰的两列布局：
- **左列**：文件选择、转换设置和控制
- **右列**：预览区域和进度跟踪

### 分步工作流程

#### 基于文件的转换

1. **选择输入文件**
   - 点击"输入文件"旁的"浏览"
   - 选择您的 Excel、Word 或文本文件
   - 应用程序自动检测文件类型

2. **配置转换设置**
   - **原文**：选择"简体"或"繁体"
   - **目标**：选择"简体"或"繁体"
   - **字形**：选择标准（OpenCC、香港、台湾）
   - **当地词汇**：启用/禁用短语转换

3. **列选择（仅 Excel）**
   - 选择包含中文文本的列
   - 使用"全选"或"取消全选"快速操作
   - 预览显示选定的列数

4. **预览和转换**
   - 在预览区域查看转换结果
   - 点击"转换文件"处理整个文档
   - 通过进度条监控进度

#### 直接文本转换

1. **输入文本**
   - 在输入区域输入或粘贴中文文本
   - 文本自动触发预览

2. **选择转换模式**
   - 选择适当的源和目标设置
   - 查看实时转换结果

3. **复制结果**
   - 点击"复制"将转换文本复制到剪贴板
   - 无需文件操作

## 支持的文件格式

### Excel 文件 (.xlsx, .xls)
- **列选择**：选择特定列进行转换
- **格式保持**：维护单元格格式、公式和结构
- **多列支持**：同时转换多个列
- **输出**：Excel 格式 (.xlsx)，UTF-8 编码

### Word 文档 (.docx)
- **全面转换**：处理段落和表格内容
- **结构保持**：维护文档格式和布局
- **表格支持**：转换表格内的文本
- **输出**：Word 格式 (.docx)，保持原始格式

### 文本文件 (.txt)
- **完整内容转换**：处理整个文件内容
- **编码支持**：UTF-8 输入和输出
- **换行保持**：维护原始文本结构
- **输出**：纯文本 (.txt)，UTF-8 编码

## 转换模式

### 基础转换
| 模式 | 描述 | 示例 |
|------|------|------|
| `s2t` | 简体转繁体中文 | 简体 → 繁體 |
| `t2s` | 繁体转简体中文 | 繁體 → 简体 |

### 地区标准
| 模式 | 描述 | 使用场景 |
|------|------|----------|
| `s2tw` | 简体转繁体（台湾） | 大陆 → 台湾 |
| `tw2s` | 繁体（台湾）转简体 | 台湾 → 大陆 |
| `s2hk` | 简体转繁体（香港） | 大陆 → 香港 |
| `hk2s` | 繁体（香港）转简体 | 香港 → 大陆 |

### 高级转换
| 模式 | 描述 | 特性 |
|------|------|------|
| `s2twp` | 简体转繁体（台湾+短语） | 包含词汇转换 |
| `tw2sp` | 繁体（台湾）转简体+短语 | 包含词汇转换 |
| `t2tw` | 繁体转繁体（台湾） | 字符变体标准化 |
| `t2hk` | 繁体转繁体（香港） | 字符变体标准化 |

## 界面截图

### 主界面
应用程序具有清晰、专业的界面，工作流程逻辑清楚：

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           OpenCC 中文转换器                              │
├─────────────────────────────┬───┬─────────────────────────────────────────┤
│         左列区域            │ │ │            右列区域                     │
│      （输入和控制）         │ │ │        （预览和输出）                   │
│                             │ │ │                                         │
│ • 文件选择                  │ │ │ • 实时预览                              │
│ • 转换设置                  │ │ │ • 进度跟踪                              │
│ • 列选择                    │ │ │ • 复制功能                              │
│ • 操作按钮                  │ │ │                                         │
└─────────────────────────────┴───┴─────────────────────────────────────────┘
```

### 主要功能演示
- **两列布局**：从左到右的有序工作流程
- **实时预览**：转换结果的即时反馈
- **进度跟踪**：大文件操作的可视化进度条
- **专业外观**：无控制台窗口的干净界面

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
│                           OpenCC 中文转换器                              │
├─────────────────────────────┬───┬─────────────────────────────────────────┤
│         左列区域            │ │ │            右列区域                     │
│      （输入和控制）         │ │ │        （预览和输出）                   │
│                             │ │ │                                         │
│ • 文件选择                  │ │ │ • 实时预览                              │
│ • 转换设置                  │ │ │ • 进度跟踪                              │
│ • 列选择                    │ │ │ • 复制功能                              │
│ • 操作按钮                  │ │ │                                         │
└─────────────────────────────┴───┴─────────────────────────────────────────┘
```

### 主要功能演示
- **两列布局**：从左到右的有序工作流程
- **实时预览**：转换结果的即时反馈
- **进度跟踪**：大文件操作的可视化进度条
- **专业外观**：无控制台窗口的干净界面

## 贡献指南

欢迎贡献来改进这个项目！以下是您可以帮助的方式：

### 报告问题

1. **检查现有问题**，在创建新问题前先检查是否已存在
2. **使用问题模板**并提供详细信息：
   - 操作系统和 Python 版本
   - 复现问题的步骤
   - 期望与实际行为
   - 错误消息或截图

### 提交拉取请求

1. **分支仓库**并创建功能分支
2. **进行更改**，使用清楚、描述性的提交
3. **为新功能添加测试**
4. **必要时更新文档**
5. **提交拉取请求**并提供清楚的描述

### 开发环境设置

```bash
# 克隆您的分支
git clone https://github.com/pencilq/opencc-chinese-converter-gui.git
cd opencc-chinese-converter-gui

# 创建开发环境
python -m venv dev-env
source dev-env/bin/activate  # Windows 上：dev-env\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 代码风格

- 遵循 PEP 8 Python 风格指南
- 使用有意义的变量和函数名
- 为新函数和类添加文档字符串
- 保持函数专注和模块化

## 故障排除

### 常见问题

#### 安装问题

**问题**：`ImportError: No module named 'opencc'`
```bash
# 解决方案：安装正确的 OpenCC 包
pip uninstall opencc
pip install opencc-python-reimplemented
```

**问题**：Excel 文件无法打开
```bash
# 解决方案：安装 Excel 支持
pip install openpyxl
```

**问题**：Word 文档无法处理
```bash
# 解决方案：安装 Word 文档支持
pip install python-docx
```

#### 运行时问题

**问题**：应用程序启动时崩溃
- 验证 Python 版本（需要 3.7+）
- 检查所有依赖项是否已安装
- 尝试从命令行运行以查看错误消息

**问题**：Windows 上出现控制台窗口
- 从命令行运行时这是预期行为
- 正常启动时控制台会自动隐藏

**问题**：转换结果不正确
- 验证输入文本包含中文字符
- 尝试不同的转换模式
- 检查源语言/目标语言设置是否正确

#### 文件处理问题

**问题**："文件编码错误"
- 确保文本文件是 UTF-8 编码
- 尝试在文本编辑器中打开文件并保存为 UTF-8

**问题**："权限拒绝"错误
- 检查文件/文件夹权限
- 确保输出目录可写
- 如果输出文件在其他应用程序中打开，请关闭它

**问题**：Excel 列选择不工作
- 验证 Excel 文件包含实际数据
- 检查列是否包含中文文本
- 尝试选择不同的列

### 获取帮助

如果您仍然遇到问题：

1. **检查 [Issues](https://github.com/pencilq/opencc-chinese-converter-gui/issues)** 页面
2. **创建新问题**并提供详细信息
3. **包含错误消息**和系统信息

## 技术文档

### 架构概览

- **GUI 框架**：Tkinter（跨平台，Python 内置）
- **转换引擎**：OpenCC（开放中文转换）
- **文件处理**：Pandas（Excel）、python-docx（Word）
- **线程处理**：大文件的后台处理
- **错误处理**：全面的验证和用户反馈

### 项目结构

```
opencc-chinese-converter-gui/
├── opencc-py-gui.py          # 主应用程序文件
├── requirements.txt          # Python 依赖
├── README.md                 # 项目文档
├── CHANGELOG.md              # 版本历史
├── LICENSE                   # 许可证文件
├── .gitignore                # Git 忽略文件
├── sample_text.txt           # 测试样本文件
├── sample_data.xlsx          # 
└── sample_document.docx      # 
```

### 依赖项

| 包名 | 版本 | 用途 |
|---------|---------|----------|
| opencc-python-reimplemented | ≥0.1.7 | 中文文本转换引擎 |
| pandas | ≥1.3.0 | Excel 文件处理和数据操作 |
| openpyxl | ≥3.0.0 | Excel 文件读写操作 |
| python-docx | ≥0.8.11 | Word 文档处理 |
| tkinter | 内置 | GUI 框架（Python 内置） |

## 许可证

本项目使用 Apache License 2.0 许可证 - 详细信息请参阅 [LICENSE](LICENSE) 文件。

### 第三方许可证

- **OpenCC**：使用 Apache License 2.0 许可证
- **Pandas**：使用 BSD 3-Clause 许可证
- **openpyxl**：使用 MIT 许可证
- **python-docx**：使用 MIT 许可证

## 致谢

- **OpenCC 项目**：感谢 BYVoid 和贡献者们提供的优秀中文转换库
- **Python 社区**：感谢提供了令人惊叹的库生态系统
- **贡献者**：感谢每一位帮助改进这个项目的人

## 更新日志

详细的更改历史请参阅 [CHANGELOG.md](CHANGELOG.md)。

---

**为中文文本处理社区精心打造**