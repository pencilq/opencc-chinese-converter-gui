#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Strings for OpenCC GUI - Chinese Text Conversion Tool
Externalized strings for better maintainability and internationalization
"""

# Application title
APP_TITLE = "OpenCC 中文转换器"

# File selection section
FILE_SELECTION_TITLE = "文件选择"
INPUT_FILE_LABEL = "输入文件:"
OUTPUT_FILE_LABEL = "输出文件:"
BROWSE_BUTTON = "浏览"

# Direct text input section
DIRECT_TEXT_TITLE = "直接文本输入（可替代文件输入）"

# Conversion settings section
CONVERSION_SETTINGS_TITLE = "转换设置"
SOURCE_LABEL = "原文:"
TARGET_LABEL = "目标:"
VARIANT_LABEL = "字形:"
PHRASES_LABEL = "当地词汇"

# Column selection section
COLUMN_SELECTION_TITLE = "列选择（Excel文件）"
SELECT_ALL_BUTTON = "全选"
DESELECT_ALL_BUTTON = "取消全选"
SELECTED_COLUMNS_LABEL = "已选择: {} 列"
NO_COLUMNS_AVAILABLE = "没有可用列"
NOT_APPLICABLE_FILE = "不适用于此文件类型"

# Preview limits configuration
PREVIEW_TEXT_LIMIT_LABEL = "预览字符限制:"
PREVIEW_ROW_LIMIT_LABEL = "预览行数限制:"

# Buttons
CONVERT_BUTTON = "转换文件"
CLEAR_BUTTON = "清空"
COPY_BUTTON = "复制"

# Preview section
PREVIEW_TITLE = "预览与复制区域"
PREVIEW_NO_INPUT = "没有提供输入。请选择文件或在上方直接输入文本。"
PREVIEW_EMPTY_FILE = "文件为空或没有数据。"
PREVIEW_INVALID_EXCEL = "无效的 Excel 数据。"
PREVIEW_SELECT_COLUMN = "请选择至少一列进行转换。"
PREVIEW_AVAILABLE_COLUMNS = "可用列: {}"
PREVIEW_RESULT_HEADER = "文件转换结果（前{}字符）："
PREVIEW_INVALID_TEXT = "无效的文本数据。"
PREVIEW_COLUMN_RESULT_HEADER_SINGLE = "列 '{}' 的转换结果（前{}行）："
PREVIEW_COLUMN_RESULT_HEADER_MULTI = "多列转换结果（{}列，前{}行）："

# Progress messages
PROGRESS_READY = "就绪"
PROGRESS_LOADING_FILE = "Loading file..."
PROGRESS_FILE_LOADED = "File loaded successfully"
PROGRESS_ERROR_LOADING_FILE = "Error loading file"
PROGRESS_CONVERTING_FILE = "正在转换文件..."
PROGRESS_CONVERTING_TEXT_FILE = "正在转换文本文件..."
PROGRESS_SAVING_FILE = "正在保存转换后的文件..."
PROGRESS_COMPLETED = "转换完成！"
PROGRESS_FAILED = "转换失败"

# Error messages
ERROR_IMPORT_OPENCC = "Import Error"
ERROR_IMPORT_OPENCC_MSG = "Please install opencc-python-reimplemented:\npip install opencc-python-reimplemented"
ERROR_IMPORT_OPENPYXL = "Import Error"
ERROR_IMPORT_OPENPYXL_MSG = "Please install openpyxl:\npip install openpyxl"
ERROR_IMPORT_DOCX = "Import Error"
ERROR_IMPORT_DOCX_MSG = "Please install python-docx:\npip install python-docx"
ERROR_CONVERTER_INIT = "转换器错误"
ERROR_CONVERTER_INIT_MSG = "初始化转换器失败: {}"
ERROR_FILE_LOAD = "File Error"
ERROR_FILE_LOAD_MSG = "Failed to load file: {}"
ERROR_CONVERSION = "转换错误"
ERROR_CONVERSION_MSG = "文件转换失败: {}"
ERROR_TEXT_CONVERSION = "转换错误"
ERROR_TEXT_CONVERSION_MSG = "文本转换失败: {}"
ERROR_COPY = "错误"
ERROR_COPY_MSG = "复制文本失败: {}"

# Warning messages
WARNING_NO_INPUT = "警告"
WARNING_NO_INPUT_MSG = "请选择输入文件或直接输入文本。"
WARNING_NO_OUTPUT = "警告"
WARNING_NO_OUTPUT_MSG = "请指定输出文件。"
WARNING_NO_CONVERTER = "错误"
WARNING_NO_CONVERTER_MSG = "转换器未初始化。"
WARNING_NO_COLUMN = "警告"
WARNING_NO_COLUMN_MSG = "请选择至少一列进行转换。"
WARNING_NO_COPY = "警告"
WARNING_NO_COPY_MSG = "没有转换结果可复制。"

# Success messages
SUCCESS_CONVERSION = "成功"
SUCCESS_CONVERSION_MSG = "文件转换成功！\n已保存至: {}"
SUCCESS_TEXT_CONVERSION = "成功"
SUCCESS_TEXT_CONVERSION_MSG = "文本转换成功！您可以从预览区域复制结果。"
SUCCESS_COPY = "成功"
SUCCESS_COPY_MSG = "转换结果已复制到剪贴板！"

# Conversion modes
CONVERSION_MODE_S2TWP = "s2twp"
CONVERSION_MODE_S2TW = "s2tw"
CONVERSION_MODE_S2HK = "s2hk"
CONVERSION_MODE_S2T = "s2t"
CONVERSION_MODE_TW2SP = "tw2sp"
CONVERSION_MODE_TW2S = "tw2s"
CONVERSION_MODE_HK2S = "hk2s"
CONVERSION_MODE_T2S = "t2s"
CONVERSION_MODE_T2TW = "t2tw"
CONVERSION_MODE_T2HK = "t2hk"
CONVERSION_MODE_T2T = "t2t"
CONVERSION_MODE_SIMPLIFIED = "简体"
CONVERSION_MODE_CONVERT = "convert"

# Variant standards
VARIANT_OPENCC = "OpenCC 标准"
VARIANT_HK = "香港标准"
VARIANT_TW = "台湾标准"

# Source/Target types
TYPE_SIMPLIFIED = "简体"
TYPE_TRADITIONAL = "繁体"