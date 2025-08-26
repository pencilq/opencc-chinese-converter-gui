# OpenCC GUI - Two-Column Layout

## Layout Structure

The GUI has been optimized with a two-column design for better user experience:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           OpenCC 中文转换器                              │
├─────────────────────────────┬───┬─────────────────────────────────────────┤
│         LEFT COLUMN         │ │ │            RIGHT COLUMN                 │
│      (Input & Controls)     │ │ │        (Preview & Output)               │
│                             │ │ │                                         │
│ ┌─────────────────────────┐ │ │ │ ┌─────────────────────────────────────┐ │
│ │     文件选择            │ │ │ │ │        预览与复制区域                 │ │
│ │ • 输入文件              │ │ │ │ │                                     │ │
│ │ • 输出文件              │ │ │ │ │    [Conversion Results]             │ │
│ └─────────────────────────┘ │ │ │ │                                     │ │
│                             │ │ │ │                                     │ │
│ ┌─────────────────────────┐ │ │ │ │                                     │ │
│ │   直接文本输入          │ │ │ │ │                                     │ │
│ │ [Text Input Area]       │ │ │ │ │                                     │ │
│ └─────────────────────────┘ │ │ │ └─────────────────────────────────────┘ │
│                             │ │ │ ┌─────────────────────────────────────┐ │
│ ┌─────────────────────────┐ │ │ │ │      [复制] Button                  │ │
│ │     转换设置            │ │ │ │ └─────────────────────────────────────┘ │
│ │ • 原文/目标             │ │ │ │                                         │
│ │ • 字形/当地词汇         │ │ │ │ ┌─────────────────────────────────────┐ │
│ └─────────────────────────┘ │ │ │ │         Progress Section            │ │
│                             │ │ │ │ • Progress Label                    │ │
│ ┌─────────────────────────┐ │ │ │ │ • Progress Bar                      │ │
│ │   列选择(Excel文件)     │ │ │ │ └─────────────────────────────────────┘ │
│ │ • [全选][取消全选]      │ │ │ │                                         │
│ │ • ☐ Column 1 (示例...)  │ │ │ │                                         │
│ │ • ☐ Column 2 (示例...)  │ │ │ │                                         │
│ │ • 已选择: X/Y 列        │ │ │ │                                         │
│ └─────────────────────────┘ │ │ │                                         │
│                             │ │ │                                         │
│ ┌─────────────────────────┐ │ │ │                                         │
│ │ [转换文件] [清空]       │ │ │ │                                         │
│ └─────────────────────────┘ │ │ │                                         │
└─────────────────────────────┴───┴─────────────────────────────────────────┘
```

## Key Improvements

### ✅ Better Organization
- **Left Column**: All input controls and settings
- **Right Column**: Preview area and progress tracking
- **Visual Separator**: Clear division between input and output areas

### ✅ Improved User Experience
- **Logical Flow**: Input → Settings → Preview → Action
- **Larger Preview Area**: More space for viewing conversion results
- **Consolidated Controls**: Related functions grouped together

### ✅ Enhanced Usability
- **Wider Window**: 1200x700 (was 800x700) for better content display
- **Responsive Layout**: Both columns expand proportionally
- **Clear Visual Hierarchy**: Title, sections, and controls properly organized

## Column Breakdown

### Left Column (Input & Controls)
1. **File Selection Section**
   - Input file browser
   - Output file path

2. **Direct Text Input Section**
   - Alternative to file input
   - Immediate text processing

3. **Conversion Settings Section**
   - Multi-layer conversion options
   - Original/Target language
   - Character variant standards
   - Local vocabulary options

4. **Column Selection Section**
   - Multi-column checkbox interface
   - Select All/Deselect All buttons
   - Selection counter

5. **Action Buttons**
   - Convert File button
   - Clear All button

### Right Column (Preview & Output)
1. **Preview Area**
   - Large scrollable text area
   - Shows conversion results only
   - Cascadia Code font with 黑体 fallback

2. **Copy Button**
   - One-click copy to clipboard
   - For direct text conversions

3. **Progress Section**
   - Real-time progress updates
   - Progress bar with percentage
   - Status messages

## Technical Implementation
- **Grid Layout**: Uses tkinter grid manager for precise control
- **Responsive Design**: Columns expand/contract with window resizing
- **Font Consistency**: 9pt Cascadia Code throughout
- **Visual Separator**: ttk.Separator for clean column division