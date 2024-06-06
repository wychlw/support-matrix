# OpenWrt MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download link (OpenWrt Firmware Selector): [here](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=mangopi_mq_pro)
- Reference installation document: [here](https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1)

> In OpenWrt Firmware Selector, you can customize and build system images online, adding the necessary pre-installed packages. The image used in this test is the **unmodified** original image.

### Hardware Information

- MangoPi MQ Pro
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Flash Image to microSD Card

Use `dd` to flash the image to the microSD card.

```bash
gzip -kd openwrt-d1-generic-mangopi_mq_pro-ext4-sdcard.img.gz
sudo dd if=openwrt-d1-generic-mangopi_mq_pro-ext4-sdcard.img of=/dev/your/device bs=1M status=progress
```

### Log into the System

Log into the system via serial port.

## Expected Result

The system boots up successfully, allowing login via the onboard serial port.

## Actual Result

The system boots up successfully, and login via the onboard serial port is successful.

### Boot Information

Screen recording (from flashing the image to logging into the system):

```log

```

## Test Criteria

Test Passed: Actual result matches the expected result.

Test Failed: Actual result does not match the expected result.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
