---
sys: bianbu
sys_ver: 2.0rc1
sys_var: null

status: basic
last_update: 2024-09-20

image_link: https://archive.spacemit.com/image/k1/version/bianbu/v2.0rc1/bianbu-24.04-desktop-k1-v2.0rc1-release-20240909135447.img.zip
username: root
password: bianbu
---

# Bianbu Banana Pi BPI-F3 Test Report

## Test Environment

### System Information

- System version: [[version]]
- Download Links: [[image_link]]
- Reference Installation Document: https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### Hardware Information

- Banana Pi BPI-F3
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

**Please make sure to choose the file ending with `.img.zip`**
After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
extract [[image_file_zip]]
sudo dd if=/path/to/[[image_file_img]] of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `[[username]]`
Default Password: `[[password]]`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (from flashing image to login):
[[asciicast]]

```log
[[info]]
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
