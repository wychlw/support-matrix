# Tina Linux MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download link: [Link](https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol) Extraction code: awol
- Reference installation document: [Link](https://d1.docs.aw-ol.com/study/study_1tina/)

### Hardware Information

- MangoPi MQ Pro
- One microSD card
- One USB to UART debugger (such as: CH340, CH341, FT2232, etc.)

## Installation Steps

### Compile SDK

Download and unzip SDK, then add a new target:
```bash
git clone https://github.com/Tina-Linux/Tina_d1x_mangopi-sbc.git
cp -r Tina_d1x_mangopi-sbc tina_d1_open_v2_2
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

### Login to the System

Login to the system via serial port.

## Expected Results

The system starts up normally and can be accessed through the onboard serial port.

## Actual Results

The system started up normally and successfully accessed through the onboard serial port.

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
