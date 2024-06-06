# Debian Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: Debian trixie/sid
- Download Link: [Download here](https://drive.google.com/file/d/1TqMuFsRo5Es2Y6-qAyxV8jnFdAkcCp4v/view?usp=sharing)
- Reference Installation Document: [GitHub - Milk-V Duo Installation Guide](https://github.com/hongwenjun/riscv64/tree/main/milkv-duo)

> Note: This image is provided by community developers and is not an official release.

### Hardware Information

- Milk-V Duo 64M
- USB Power Adapter
- USB-A to C or USB C to C Cable
- One microSD card
- USB to UART Debugger (e.g. CH340, CH341, FT2232, etc.)
- Three DuPont wires
- Pre-soldered debug pins on the Milk-V Duo board
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Write the Image to the microSD card using `dd`

```shell
7z x duo-debian-full.7z
dd if=debian.img of=/dev/sdc bs=1M status=progress
```

### System Login

Login to the system via serial console.

Username: `root`
Password: `riscv`

## Expected Results

The system should boot up correctly and allow login via the serial console.

## Actual Results

The system booted up successfully and login via serial console was also successful.

### Boot Information

```log
Debian GNU/Linux trixie/sid milkv-duo ttyS0

milkv-duo login: root
Password: 
Linux milkv-duo 5.10.4-tag- #7 PREEMPT Tue Oct 24 23:07:12 JST 2023 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Jul 24 19:51:14 UTC 2023 on ttyS0
root@milkv-duo:~# uname -a
Linux milkv-duo 5.10.4-tag- #7 PREEMPT Tue Oct 24 23:07:12 JST 2023 riscv64 GNU/Linux
root@milkv-duo:~# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@milkv-duo:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@milkv-duo:~# 
```

Screen recording of the boot process:

[![asciicast](https://asciinema.org/a/oOEaHElWFYEJMCmsOkqDZfbEv.svg)](https://asciinema.org/a/oOEaHElWFYEJMCmsOkqDZfbEv)


## Test Judgement Criteria

Test Successful: The actual results match the expected results.

Test Failed: The actual results do not match the expected results.

## Test Conclusion

The test was successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
