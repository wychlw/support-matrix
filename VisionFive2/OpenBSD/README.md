# OpenBSD 7.5 VisionFive 2 Test Report

## Test Environment

### System Information

- System Version: OpenWRT SnapShot
- Download Link: [https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/)
    - dtb File: https://marc.info/?l=openbsd-misc&m=169046816826966&w=2
- Installation Reference Document: [https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64)
    - Community Tutorial: https://gist.github.com/csgordon/74658096f7838382b40bd64e11f6983e

### Hardware Information

- StarFive VisionFive
- Power Adapter
- One microSD Card
- One USB to UART Debugger
- Wired Internet Connection

## Installation Steps

### Flashing Installation Image

Use `gzip` to decompress the image.
Use `dd` to write the image to the microSD card.

```bash
wget https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/install75.img
sudo dd if=install75.img of=/dev/your-device bs=1M status=progress
```

Place the dtb file in the EFI root directory:

```bash
mkdir -p mnt
sudo mount /dev/your-device-p1 mnt
cp jh7110-starfive-visionfive-2-v1.3b.dtb mnt/
sudo umount mnt
```

### System Boot-up

Manually interrupt the u-boot process and enter the boot command:
```bash
load mmc 1:1 ${fdt_addr_r} jh7110-starfive-visionfive-2-v1.3b.dtb
load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi
bootefi ${kernel_addr_r} ${fdt_addr_r}
```

Follow the process to install, then place dtb in the EFI root directory again (if it was overwritten).

### U-boot Persistence

```bash
env default -a -f
setenv bootcmd "load mmc 1:1 ${fdt_addr_r} jh7110-starfive-visionfive-2-v1.3b.dtb; load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi; bootefi ${kernel_addr_r} ${fdt_addr_r}"
saveenv
```

### Logging into the System

Log into the system via serial console.

User credentials are set during installation.

## Expected Outcome

The system boots up successfully and allows login through the onboard serial console.

## Actual Outcome

The system boots up successfully and login through the onboard serial console is successful.

### Boot-up Information

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/Cz0uvucqmbP1P0yzgZ2hnMbZY.svg)](https://asciinema.org/a/Cz0uvucqmbP1P0yzgZ2hnMbZY)

```log
Tue Mar 26 22:01:09 CST 2024

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

## Test Success Criteria

Test Pass: Actual outcome matches the expected outcome.

Test Fail: Actual outcome does not match the expected outcome.

## Test Conclusion

Partial success in the testing.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
