# OpenWrt 23.05.2 DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link (OpenWrt Firmware Selector): [link](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=dongshan_nezha_stu)
- Reference Installation Document: [link](https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1)

> The OpenWrt Firmware Selector allows online customization of the build system image, adding pre-installed software packages as needed by the user. The image used in this test is **unmodified** original version.

### Hardware Information

- DongshanPI-Nezha STU
- One USB-A power
- One USB-A to C cable
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont wires

## Installation Steps

### Flashing the Image to the microSD Card

Use `dd` to flash the image to the microSD card.

```bash
gzip -kd openwrt-d1-generic-dongshan_nezha_stu-ext4-sdcard.img.gz
sudo dd if=openwrt-d1-generic-dongshan_nezha_stu-ext4-sdcard.img of=/dev/your/device bs=1M status=progress
```

### System Login

Log in to the system via serial port.

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

The system booted up successfully and allowed login via the onboard serial port.

### Boot-up Information

Screen recording (from flashing the image to logging into the system):

```log

```

## Test Criteria

Successful Test: Actual results match the expected results.

Failed Test: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
