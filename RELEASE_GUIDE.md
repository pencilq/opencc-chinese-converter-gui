# 手动创建 GitHub Release 完整指南

## 🎯 立即可用的解决方案

已为你提供了多种 GitHub Release 创建方案，每种都针对不同需求进行了优化。

## 📋 当前状态

✅ **代码已推送到 GitHub**  
✅ **创建了标签 v1.0.5**  
✅ **提供了 4 种构建方案**  
⏳ **正在创建 GitHub Release**

## 🛠️ 方案概览

### 方案1: 本地构建 + 手动上传 (推荐)
- **文件**: `build_release.py`
- **优势**: 100% 可靠，在本地环境构建
- **使用**: `python build_release.py`

### 方案2: GitHub CLI 自动化
- **文件**: `release_with_gh_cli.py`
- **前置条件**: 安装并认证 GitHub CLI
- **使用**: `python release_with_gh_cli.py v1.0.5`

### 方案3: 简化的 GitHub Actions
- **文件**: `.github/workflows/simple-release.yml`
- **触发**: 推送标签自动构建
- **状态**: 已禁用复杂版本，启用简化版本

### 方案4: 手动创建 Release
- **方式**: GitHub 网页界面操作
- **适用**: 快速发布，无需可执行文件

## 🚀 立即执行步骤

### Step 1: 检查构建状态
```bash
# 检查当前 PyInstaller 构建
dir release
```

### Step 2: 创建 GitHub Release
访问: https://github.com/pencilq/opencc-chinese-converter-gui/releases/new

填写以下信息：
```
Tag version: v1.0.5
Release title: OpenCC 中文转换器 v1.0.5
Description: [见下方模板]
```

### Step 3: 发布说明模板
```markdown
## OpenCC 中文转换器 v1.0.5

### 🔧 重要更新
- 修复了 GitHub Actions 构建问题
- 提供了多种可靠的构建替代方案
- 改进了本地构建脚本和文档

### 📥 下载方式

#### 推荐下载
- **源代码**: 下载 Source code (zip) 
- **运行要求**: Python 3.7+ 及依赖包

#### 本地构建可执行文件
```bash
# 1. 下载源代码并解压
# 2. 安装依赖
pip install -r requirements.txt
pip install pyinstaller

# 3. 运行构建脚本
python build_release.py
```

### ✨ 主要功能
- 🔄 简体/繁体中文互转
- 📊 支持 Excel、Word、文本文件批量转换
- 🎯 Excel 多列选择转换
- 👀 实时预览转换结果
- 🚀 直接文本转换
- 🎨 清晰的双列界面设计

### 📋 系统要求
- **Python**: 3.7 或更高版本
- **系统**: Windows 10/11, macOS 10.14+, Linux
- **内存**: 建议 4GB 以上
- **磁盘**: 100MB 可用空间

### 🛠️ 构建方案
提供了 4 种不同的构建和发布方案：
1. **本地构建脚本** (`build_release.py`) - 最可靠
2. **GitHub CLI 工具** (`release_with_gh_cli.py`) - 半自动化
3. **简化的 GitHub Actions** - 全自动化
4. **手动构建指令** - 最简单

### 🔄 使用指南
1. **运行程序**: `python opencc-py-gui.py`
2. **选择文件**: 点击"浏览"选择要转换的文件
3. **配置设置**: 选择源语言和目标语言
4. **预览结果**: 查看右侧预览区的转换效果
5. **开始转换**: 点击"转换文件"处理文档

### 📚 文档
- [构建指南](BUILD_GUIDE.md)
- [故障排除](BUILD_TROUBLESHOOTING.md)
- [更新日志](CHANGELOG.md)

### 🐛 问题反馈
如遇到问题，请在 [Issues](https://github.com/pencilq/opencc-chinese-converter-gui/issues) 中反馈。

### 🙏 致谢
感谢使用 OpenCC 中文转换器！本版本重点解决了构建和发布流程的可靠性问题。
```

## 📱 快速操作链接

1. **创建 Release**: https://github.com/pencilq/opencc-chinese-converter-gui/releases/new
2. **查看 Actions**: https://github.com/pencilq/opencc-chinese-converter-gui/actions
3. **查看 Releases**: https://github.com/pencilq/opencc-chinese-converter-gui/releases

## 🔧 后续优化建议

### 减少 PyInstaller 包大小
当前构建包含了很多不必要的包（torch, sklearn等），可以通过以下方式优化：

```bash
# 创建专用虚拟环境
python -m venv opencc-build-env
opencc-build-env\Scripts\activate

# 只安装必要依赖
pip install opencc-python-reimplemented pandas openpyxl python-docx pyinstaller

# 然后运行构建
pyinstaller --onefile --noconsole --name "OpenCC中文转换器" opencc-py-gui.py
```

### 使用 --exclude-module 优化
```bash
pyinstaller --onefile --noconsole \
  --exclude-module torch \
  --exclude-module sklearn \
  --exclude-module cv2 \
  --exclude-module tensorflow \
  --name "OpenCC中文转换器" \
  opencc-py-gui.py
```

## ✅ 成功指标

- [x] 代码推送到 GitHub
- [x] 创建版本标签 v1.0.5  
- [x] 提供多种构建方案
- [x] 编写详细文档
- [ ] 创建 GitHub Release
- [ ] 上传可执行文件（可选）
- [ ] 测试下载和使用

现在你可以访问 GitHub 仓库创建 Release，或者使用本地构建脚本！