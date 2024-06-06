# Tina Linux DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download link: [Link: https://pan.baidu.com/s/13uKlqDXImmMl9cgKc41tZg?pwd=qcw7](https://pan.baidu.com/s/13uKlqDXImmMl9cgKc41tZg?pwd=qcw7) Extract code: qcw7
- Reference installation document: [https://d1.docs.aw-ol.com/study/study_1tina/](https://d1.docs.aw-ol.com/study/study_1tina/)

### Hardware Information

- DongshanPI-Nezha STU
- One microSD card
- One USB to UART debugger (such as: CH340, CH341, FT2232, etc.)

## Installation Steps

### Compile SDK

After downloading, you can find the SDK under DongshanNezhaSTU-TinaV2.0-SDK.
Merge and decompress the SDK:
```bash
cat tina-d1-h.tar.bz2.* | tar -zxv
```

Compile and package:
```bash
source build/envsetup.sh
lunch
make -j$(nproc)
pack
```

### Flash Image

Use dd to flash the image to the SD card:
```bash
sudo dd if=tina_d1-h.img of=/dev/your/device bs=1M status=progress
```

### Login to System

Login to the system via serial port.

## Expected Results

The system starts up normally and can be accessed via onboard serial port.

## Actual Results

The system starts up normally and login via onboard serial port is successful.

### Boot Information

Screen recording (from flashing the image to logging into the system):

```log
```

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
