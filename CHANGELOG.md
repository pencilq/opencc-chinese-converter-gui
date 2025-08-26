# 更新日志

本项目的所有重要更改都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/) 规范。

## [未发布]

### 新增
- 完善 GitHub 仓库结构
- 添加中文文档和界面
- 专业的 README 文档，包含徽章和全面的说明文档
- LICENSE 文件 (Apache 2.0)
- Python 项目的 .gitignore 文件

## [1.0.0] - 2024-08-26

### 新增
- **核心功能**
  - OpenCC 中文文本转换的 GUI 应用程序
  - 支持 Excel (.xlsx, .xls)、Word (.docx) 和文本 (.txt) 文件
  - 多层转换设置（源语言/目标语言、字符变体、词汇）
  - 实时预览功能
  - 大文件进度跟踪
  - Excel 文件多列选择
  - 直接文本输入和转换
  - Windows 自动隐藏控制台窗口

- **用户界面**
  - 两列布局设计
  - 中文语言界面
  - Cascadia Code 字体，黑体作为后备
  - 响应式设计，带有适当的网格布局
  - 输入和预览区域之间的视觉分隔符

- **技术实现**
  - 非阻塞文件转换的线程处理
  - 全面的错误处理和验证
  - 自动文件类型检测
  - 跨平台兼容性
  - 内存高效的文件处理

- **转换模式**
  - 基础：简体 ⟷ 繁体中文
  - 地区：台湾标准、香港标准
  - 高级：短语转换支持
  - 字符变体标准化

- **文件处理**
  - Excel：列级转换，保持格式
  - Word：段落和表格文本转换
  - 文本：完整内容转换，UTF-8 支持
  - 自动输出文件命名，带转换模式后缀

- **文档**
  - 全面的 README，包含使用说明
  - 布局文档 (LAYOUT.md)
  - 测试样本文件
  - 安装和故障排除指南

### 技术详情
- Python 3.7+ 兼容性
- 依赖项：opencc-python-reimplemented、pandas、openpyxl、python-docx
- GUI 框架：tkinter（跨平台）
- Windows 系统控制台管理
- 具有优雅回退的错误安全 API 调用

### 已知问题
- 初始版本中无已报告问题

---

**注意**：此更新日志将随每次发布而更新。有关完整的更改列表，请参阅 [提交历史](https://github.com/pencilq/opencc-chinese-converter-gui/commits/)。