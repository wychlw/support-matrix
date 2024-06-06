# BuildRoot DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link: [GitHub - DongshanPI Buildroot Nezha STU](https://github.com/DongshanPI/buildroot_dongshannezhastu)
- Reference Installation Document: [DongshanPI Nezha STU Buildroot SDK Development Guide](https://dongshanpi.com/DongshanNezhaSTU/07-Buildroot-SDK_DevelopmentGuide/)

### Hardware Information

- DongshanPI-Nezha STU
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Compile SDK

Download SDK:
```bash
git clone  https://github.com/DongshanPI/buildroot_dongshannezhastu
cd buildroot_dshannezhastu
git submodule update --init --recursive
git submodule update --recursive --remote
```

Compile SD card image:
```bash
cd buildroot-awol/
make  BR2_EXTERNAL="../br2lvgl  ../br2qt5 ../br2nezhastu"  dongshannezhastu_sdcard_core_defconfig
make -j$(nproc)
```

### Image Burning

Use `dd` to burn the image to the SD card:
```bash
sudo dd if=dongshannezhastu-sdcard.img of=/dev/your/device bs=1M status=progress
```

### System Login

Login to the system via serial port.

## Expected Results

The system starts up successfully and allows login via onboard serial port.

## Actual Results

The system boots up successfully and login via the onboard serial port is successful.

### Boot-up Information

Screen recording (from image flashing to system login):

```log
```

## Test Evaluation Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
