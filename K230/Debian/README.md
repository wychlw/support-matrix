# Debian K230 Test Report

## Test Environment

### Operating System Information

- System Version: canmv_debian_sdcard_sdk_1.3
- Download Link: [Download here](https://kendryte-download.canaan-creative.com/developer/k230/canmv_debian_sdcard_sdk_1.3.img.gz)
- Reference Installation Guide: [Installation Guide](https://developer.canaan-creative.com/k230/dev/zh/CanMV_K230_%E6%95%99%E7%A8%8B.html)

### Hardware Information

- Development Board: Canaan Kendryte K230

## Installation Steps

### Write Image to microSD Card

Use the `dd` command to write the image to the microSD card. Assuming the microSD card device is `/dev/sdb`.

```bash
wget https://kendryte-download.canaan-creative.com/developer/k230/canmv_debian_sdcard_sdk_1.3.img.gz
gzip -d canmv_debian_sdcard_sdk_1.3.img.gz
sudo dd if=canmv_debian_sdcard_sdk_1.3.img of=/dev/sdb bs=1M status=progress oflag=sync
```

### System Login

Login to the system via serial console.

Default username: `root`
Default password: `root`

## Expected Result

The system should boot up successfully and allow login via the onboard serial console.

## Actual Result

The system booted up successfully, and login via the onboard serial console was also successful.

### Boot Information

![Debian](image.png)

Screen recording (from burning to logging into the system):

[![asciicast](https://asciinema.org/a/WT2Nz2w7OubHlHaQMEpJZCD8x.svg)](https://asciinema.org/a/WT2Nz2w7OubHlHaQMEpJZCD8x)

```log
Debian GNU/Linux trixie/sid v hvc0

v login: oto
Password: 

Login incorrect
v login: root
Password: 
Linux v 5.10.4 #1 SMP Thu Jan 11 19:05:37 CST 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@v:~# uname -a
Linux v 5.10.4 #1 SMP Thu Jan 11 19:05:37 CST 2024 riscv64 GNU/Linux
root@v:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@v:~# 

```

## Test Judgement Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
