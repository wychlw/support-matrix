# OpenWRT SnapShot VisionFive 2 Test Report

## Test Environment

### System Information

- System Version: OpenWRT SnapShot
- Download Link: [https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive2-v1.3b](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive2-v1.3b)
- Reference Installation Document: [https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html](https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html)

### Hardware Information

- StarFive VisionFive2
- Power Adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Flashing Image

Decompress the image using `gzip`.
Write the image to the microSD card using `dd`.

```bash
wget https://downloads.openwrt.org/snapshots/targets/starfive/generic/openwrt-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz
gzip -d /path/to/openwrt.img.gz
sudo dd if=/path/to/openwrt.img of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Login to the system via a serial port.

No password required by default, automatically logs in as root.

## Expected Outcome

The system boots up successfully and can be accessed via the onboard serial port.

## Actual Outcome

The system boots up successfully and can be accessed via the onboard serial port.

### Boot-up Information

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/cNB8FumIO4mB00Ppi1OoMCFyq.svg)](https://asciinema.org/a/cNB8FumIO4mB00Ppi1OoMCFyq)

```log
BusyBox v1.36.1 (2024-03-25 22:00:37 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r25665-79e9ce354e
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# uname -a
Linux OpenWrt 6.1.82 #0 SMP Mon Mar 25 22:00:37 2024 riscv64 GNU/Linux
root@OpenWrt:/# cat /etc/os-release 
NAME="OpenWrt"
VERSION="SNAPSHOT"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt SNAPSHOT"
VERSION_ID="snapshot"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
BUILD_ID="r25665-79e9ce354e"
OPENWRT_BOARD="starfive/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt SNAPSHOT r25665-79e9ce354e"
root@OpenWrt:/# 
```

## Test Criteria

Test Successful: Actual outcome matches the expected outcome.

Test Failed: Actual outcome does not match the expected outcome.

## Test Conclusion

Test Successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
