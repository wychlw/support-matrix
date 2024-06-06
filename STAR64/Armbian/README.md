# Armbian Star64 Test Report

## Test Environment

### Operating System Information

- Download Link: [Armbian Star64](https://www.armbian.com/star64/)
- Reference Installation Document: [Installing Armbian on Star64](https://www.hackster.io/lupyuen/rtos-on-a-risc-v-sbc-star64-jh7110-apache-nuttx-2a7429)

### Hardware Information

- Development Board: Star64
- USB A to C / USB C to C cables
- SD Card

## Installation Steps

### Flashing Image

After downloading, unzip and flash the image (using the XFCE version as an example):
```bash
unxz -k Armbian_community_24.5.0-trunk.667_Star64_jammy_edge_5.15.0_xfce_desktop.img.xz
sudo dd if=Armbian_community_24.5.0-trunk.667_Star64_jammy_edge_5.15.0_xfce_desktop.img of=/dev/your/sdcard bs=1M status=progress
```

### Logging into the System

Connect to the development board via serial port.

Upon startup, the system will prompt the user to manually configure username, password, time zone, language, etc.

For the XFCE version, configuration must be completed before accessing the desktop.

Configuration can be done via serial port. If a keyboard and monitor are connected, configuration can also be done using the keyboard.

## Expected Results

Successful build with the development board displaying normal boot information.

## Actual Results

Successful build with the development board displaying normal boot information.

### Boot Information

Screen recording (from flashing the system to booting):


```log
```

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
