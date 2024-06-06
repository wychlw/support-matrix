# OpenBSD 7.5 VisionFive 1 Test Report

## Test Environment

### System Information

- System Version: OpenWRT SnapShot
- Download Link: [https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/)
    - Official Fedora Image (for extracting dtb file): https://fedora.starfivetech.com/pub/downloads/VisionFive-release/Fedora-riscv64-jh7100-developer-xfce-Rawhide-20211226-214100.n.0-sda.raw.zst
- Reference Installation Document: [https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64)
    - Community Tutorial: https://gist.github.com/csgordon/74658096f7838382b40bd64e11f6983e

### Hardware Information

- StarFive VisionFive
- Power Adapter
- One microSD card
- One USB to UART debugger
- Wired Internet connection

## Installation Steps

### Extracting dtb File

Unzip the Fedora image, mount the boot partition, and copy the `jh7100-starfive-visionfive-v1.dtb` file from the dtb folder.

### Flashing Installation Image

Unzip the image using `gzip`.
Write the image to the microSD card using `dd`.

```bash
wget https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/install75.img
sudo dd if=install75.img of=/dev/your-device bs=1M status=progress
```

Place the dtb file in the EFI root directory:

```bash
mkdir -p mnt
sudo mount /dev/your-device-p1 mnt
cp jh7100-starfive-visionfive-v1.dtb mnt/
sudo umount mnt
```

### System Startup

Manually interrupt the u-boot process and enter the boot command:
```bash
load mmc 0:1 0x88000000 jh7100-starfive-visionfive-v1.dtb
load mmc 0:1 0x84000000 efi/boot/bootriscv64.efi
bootefi 0x84000000 0x88000000
```

Follow the process to install, then re-place the dtb file in the EFI root directory if it was overwritten.

### Persisting uboot

```bash
env default -a -f
setenv bootcmd "load mmc 0:1 0x88000000 jh7100-starfive-visionfive-v1.dtb; load mmc 0:1 0x84000000 efi/boot/bootriscv64.efi; bootefi 0x84000000 0x88000000"
saveenv
```

### Logging into the System

Log into the system via serial port.

The username and password were set during installation.

## Expected Results

The system should boot up correctly and allow login via the onboard serial port.

## Actual Results

The system boots up correctly and successful login is achieved via the onboard serial port.

### Boot Information

Screen recording (from flashing image to system login):

[![asciicast](https://asciinema.org/a/dNtdx7un7CxaAbKEqeFsWF9Cw.svg)](https://asciinema.org/a/dNtdx7un7CxaAbKEqeFsWF9Cw)

```log
Sat Mar 23 10:02:30 CST 2024

OpenBSD/riscv64 (plct.my.domain) (console)

login: root
Password:
OpenBSD 7.5 (GENERIC.MP) #1: Fri Mar 22 19:01:44 MDT 2024

Welcome to OpenBSD: The proactively secure Unix-like operating system.

Please use the sendbug(1) utility to report bugs in the system.
Before reporting a bug, please try to reproduce it with the latest
version of the code.  With bug reports, please try to ensure that
enough information to reproduce the problem is enclosed, and if a
known fix for it exists, include that as well.

You have new mail.
plct# uname -a
OpenBSD plct.my.domain 7.5 GENERIC.MP#1 riscv64
plct# 

```

## Test Evaluation Criteria

Test Successful: The actual results match the expected results.

Test Failed: The actual results do not match the expected results.

## Test Conclusion

Partial success in the testing.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
