// Copyright 2019 jem@seethis.link
// Licensed under the MIT license (http://opensource.org/licenses/MIT)

#define BLE_FEATURE_REP_COUNT 0

#define BLE_REPORT_ID_BOOT_KB  1
#define BLE_REPORT_ID_MOUSE    2
#define BLE_REPORT_ID_SYSTEM   3
#define BLE_REPORT_ID_CONSUMER 4
#define BLE_REPORT_ID_NKRO     5
#define BLE_REPORT_ID_VENDOR   6

#define BLE_INPUT_REPORT_INDEX_BOOT_KB  0
#define BLE_INPUT_REPORT_INDEX_MOUSE    1
#define BLE_INPUT_REPORT_INDEX_SYSTEM   2
#define BLE_INPUT_REPORT_INDEX_CONSUMER 3
#define BLE_INPUT_REPORT_INDEX_NKRO     4
#define BLE_INPUT_REPORT_INDEX_VENDOR   5

#define BLE_OUTPUT_REPORT_INDEX_BOOT_KB 0
#define BLE_OUTPUT_REPORT_INDEX_VENDOR  1

// Input reports
#define BLE_INPUT_REPORT_COUNT 6
#define BLE_INPUT_REPORT_SIZE_BOOT_KB  8
#define BLE_INPUT_REPORT_SIZE_MOUSE    8
#define BLE_INPUT_REPORT_SIZE_SYSTEM   2
#define BLE_INPUT_REPORT_SIZE_CONSUMER 2
#define BLE_INPUT_REPORT_SIZE_NKRO     29
#define BLE_INPUT_REPORT_SIZE_VENDOR   64

// Output reports
#define BLE_OUTPUT_REPORT_COUNT 2
#define BLE_OUTPUT_REPORT_SIZE_BOOT_KB 1
#define BLE_OUTPUT_REPORT_SIZE_VENDOR  64
