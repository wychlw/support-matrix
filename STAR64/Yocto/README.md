# Yocto Star64 Test Report

## Test Environment

### Operating System Information

- Download link: [https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1](https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1)
- Reference installation document: [https://github.com/Fishwaldo/meta-pine64](https://github.com/Fishwaldo/meta-pine64)

### Hardware Information

- Development board: Star64
- USB A to C / USB C to C cables
- SD card

## Installation Steps

### Image Burning

After downloading, unzip and burn the image (using the plasma version as an example):
```bash
```bash
wget https://github.com/Fishwaldo/meta-pine64/releases/download/v2.1/star64-image-plasma-star64.wic.bz2
bzip2 -kd star64-image-plasma-star64.wic.bz2
sudo dd if=star64-image-plasma-star64.wic of=/dev/your/sdcard bs=1M status=progress
```
```

### Logging into the System

Connect to the development board via serial port.

Upon startup, the system will prompt the user to manually configure username, password, timezone, language, etc.

The Xfce version requires configuration before accessing the desktop.

Configuration can be done via serial port. If a keyboard and monitor are connected, configuration can also be done using the keyboard.

## Expected Results

Successful build with the development board displaying normal boot information.

## Actual Results

Successful build with the development board displaying normal boot information.

### Boot Information

Screen recording (from system flashing to boot):
```bash
```log
```
```

## Test Criteria

Test Passed: Actual results match expected results.

Test Failed: Actual results differ from expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
