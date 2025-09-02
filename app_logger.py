#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logging module for OpenCC GUI - Chinese Text Conversion Tool
Provides structured logging for debugging and troubleshooting
"""

import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging
log_filename = os.path.join(log_dir, f"opencc_gui_{datetime.now().strftime('%Y%m%d')}.log")

# Create logger
logger = logging.getLogger('opencc_gui')
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages
fh = logging.FileHandler(log_filename, encoding='utf-8')
fh.setLevel(logging.DEBUG)

# Create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

def get_logger():
    """Return the configured logger instance"""
    return logger