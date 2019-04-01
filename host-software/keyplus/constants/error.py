#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 jem@seethis.link
# Licensed under the MIT license (http://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function, unicode_literals

###############################################################################
#                            error code constants                             #
###############################################################################

# non-critical errors
ERROR_EKC_OUT_OF_BOUNDS_ACCESS = 0
ERROR_UNHANDLED_KEYCODE = 1
ERROR_RECEIVED_TOO_LARGE_DEVICE_ID = 2
ERROR_RECEIVED_TOO_LARGE_MATRIX = 3
ERROR_KEY_EVENT_QUEUE_FULL = 4
ERROR_KEY_EVENT_QUEUE_UNLOADED_DEVICE = 5
ERROR_VENDOR_IN_REPORT_CANT_KEEP_UP = 6
ERROR_INVALID_KB_ID_USED = 7
ERROR_MACRO_CMD_ERROR = 8

# critical errors
CRITICAL_ERROR_START = 64
ERROR_EKC_STORAGE_TOO_LARGE = 64
ERROR_NUM_LAYOUTS_TOO_LARGE = 65
ERROR_SETTINGS_CRC_MISMATCH = 66
ERROR_LAYOUT_STORAGE_OUT_OF_BOUNDS = 67
ERROR_MATRIX_PINS_CONFIG_TOO_LARGE = 68
ERROR_PIN_MAPPING_CONFLICT = 69
ERROR_NRF24_BAD_SPI_CONNECTION = 70
ERROR_UNSUPPORTED_SCAN_MODE = 71

ERROR_CODE_MAP = {
    0: "ERROR_EKC_OUT_OF_BOUNDS_ACCESS",
    1: "ERROR_UNHANDLED_KEYCODE",
    2: "ERROR_RECEIVED_TOO_LARGE_DEVICE_ID",
    3: "ERROR_RECEIVED_TOO_LARGE_MATRIX",
    4: "ERROR_KEY_EVENT_QUEUE_FULL",
    5: "ERROR_KEY_EVENT_QUEUE_UNLOADED_DEVICE",
    6: "ERROR_VENDOR_IN_REPORT_CANT_KEEP_UP",
    7: "ERROR_INVALID_KB_ID_USED",
    8: "ERROR_MACRO_CMD_ERROR",

    64: "ERROR_EKC_STORAGE_TOO_LARGE",
    65: "ERROR_NUM_LAYOUTS_TOO_LARGE",
    66: "ERROR_SETTINGS_CRC_MISMATCH",
    67: "ERROR_LAYOUT_STORAGE_OUT_OF_BOUNDS",
    68: "ERROR_MATRIX_PINS_CONFIG_TOO_LARGE",
    69: "ERROR_PIN_MAPPING_CONFLICT",
    70: "ERROR_NRF24_BAD_SPI_CONNECTION",
    71: "ERROR_UNSUPPORTED_SCAN_MODE",
}


