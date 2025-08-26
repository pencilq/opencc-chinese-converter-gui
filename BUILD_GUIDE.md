# GitHub Actions 自动构建和发布指南

本指南介绍如何使用 GitHub Actions 自动构建 EXE 文件并创建发布版本。

## 🚀 **自动构建流程**

### 触发条件
- **标签推送**: 当推送形如 `v1.0.0` 的标签时自动触发
- **手动触发**: 在 GitHub Actions 页面手动运行

### 构建平台
- **Windows**: 构建 `.exe` 文件
- **macOS**: 构建 macOS 应用程序

## 📋 **使用步骤**

### 1. 提交代码更改
```bash
git add .
git commit -m "feat: 添加新功能"
git push origin main
```

### 2. 创建发布标签
```bash
# 创建带注释的标签
git tag -a v1.0.2 -m "Release v1.0.2: 添加自动构建功能

- 新增 GitHub Actions 自动构建
- 支持 Windows 和 macOS 平台
- 自动创建发布包"

# 推送标签到 GitHub
git push origin v1.0.2
```

### 3. 自动构建过程
推送标签后，GitHub Actions 将自动：
1. 设置 Python 环境
2. 安装项目依赖
3. 使用 PyInstaller 构建可执行文件
4. 创建发布包
5. 自动创建 GitHub Release
6. 上传构建的文件到 Release

## 📁 **构建输出**

### Windows 版本
- `OpenCC中文转换器.exe` - 单独的可执行文件
- `OpenCC中文转换器-Windows-x64.zip` - 完整安装包，包含：
  - 可执行文件
  - 说明文档
  - 示例文件
  - 许可证

### macOS 版本
- `OpenCC中文转换器-macOS-x64.tar.gz` - macOS 应用包

## 🛠 **本地构建测试**

在推送到 GitHub 之前，可以在本地测试构建：

### Windows 本地构建
```bash
# 运行构建脚本
build.bat

# 或者手动执行
pip install pyinstaller
pyinstaller --clean opencc-gui.spec
```

### 手动构建命令
```bash
# 基础命令
pyinstaller --onefile --windowed --name="OpenCC中文转换器" opencc-py-gui.py

# 使用 spec 文件（推荐）
pyinstaller --clean opencc-gui.spec
```

## ⚙ **配置文件说明**

### 1. `.github/workflows/build-release.yml`
- GitHub Actions 工作流程配置
- 定义构建环境和步骤
- 自动发布到 GitHub Releases

### 2. `opencc-gui.spec`
- PyInstaller 配置文件
- 控制打包选项和依赖
- 定义应用程序元数据

### 3. `version_info.txt`
- Windows 可执行文件版本信息
- 在文件属性中显示

### 4. `build.bat`
- Windows 本地构建脚本
- 自动化本地测试流程

## 🎯 **发布流程最佳实践**

### 1. 版本命名规范
```
v主版本.次版本.修订版本
例如：v1.0.0, v1.1.0, v1.0.1
```

### 2. 发布前检查清单
- [ ] 本地测试应用功能正常
- [ ] 更新 CHANGELOG.md
- [ ] 确认版本号正确
- [ ] 本地构建测试成功

### 3. 标签创建模板
```bash
git tag -a v1.0.2 -m "Release v1.0.2: 版本描述

主要更新：
- 功能1：描述
- 功能2：描述
- 修复：问题描述

技术改进：
- 性能优化
- 代码重构"

git push origin v1.0.2
```

## 🔧 **故障排除**

### 常见问题

1. **构建失败：缺少依赖**
   - 检查 `requirements.txt` 是否包含所有依赖
   - 确认 Python 版本兼容性

2. **EXE 文件过大**
   - 在 spec 文件中添加更多 `excludes`
   - 启用 UPX 压缩

3. **运行时错误**
   - 检查 `hiddenimports` 列表
   - 确认数据文件正确包含

4. **图标显示问题**
   - 确保 `icon.ico` 文件存在且格式正确
   - 或注释掉 spec 文件中的 icon 行

### 调试方法

1. **本地测试**
   ```bash
   # 启用调试模式
   pyinstaller --debug=all opencc-gui.spec
   ```

2. **查看构建日志**
   - 在 GitHub Actions 页面查看详细日志
   - 检查每个步骤的输出

3. **测试可执行文件**
   ```bash
   # 在命令行中运行，查看错误信息
   "dist/OpenCC中文转换器.exe"
   ```

## 📚 **相关资源**

- [PyInstaller 官方文档](https://pyinstaller.readthedocs.io/)
- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [Python 打包指南](https://packaging.python.org/)

## 🎉 **成功示例**

完成配置后，每次推送标签都会自动：
1. 触发构建流程
2. 生成跨平台可执行文件
3. 创建 GitHub Release
4. 用户可直接下载使用

这样用户就无需安装 Python 环境，可以直接运行您的应用程序！