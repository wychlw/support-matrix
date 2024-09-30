---
sys: armbian
sys_ver: 6.1.15
sys_var: noble

status: basic
last_update: 2024-09-13

image_link: https://mirrors.tuna.tsinghua.edu.cn/armbian-releases/bananapif3/archive/Armbian_24.8.1_Bananapif3_noble_legacy_6.1.15_minimal.img.xz
username: null
password: null
---

# Armbian Banana Pi BPI-F3 Test Report

## Test Environment

### System Information

- Download Links: [[image_link]]
- Reference Installation Document: https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### Hardware Information

- Banana Pi BPI-F3
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
extract [[image_file_zip]]
sudo dd if=/path/to/[[image_file_img]] of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

On the first boot, create a user.

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully and login through the onboard serial port was also successful.

### Boot Log

Screen recording (From flashing image to system login):
[[asciicast]]

```log
[[info]]
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
