
# Debian on Milk-V Mars

## Test Environment

### Operating System Information

- Debian bookworm/sid
  - Download link: https://github.com/milkv-mars/mars-buildroot-sdk/releases/
    - Debian image provided by Milk-V along with BuildRoot in the repository
  - Installation guide: https://milkv.io/zh/docs/mars/getting-started/boot

### Hardware Development Board Information

- Milk-V Mars

## Installation Steps

### Flashing Image

Use `unzip` to extract the image.
Use `dd` to write the image to the microSD card.

Where `/dev/sdc` corresponds to the storage card's device.

```bash
unzip mars_debian-desktop_sdk-v3.6.1_sdcard_v1.0.6.img.zip
sudo dd if=mars_debian-desktop_sdk-v3.6.1_sdcard_v1.0.6.img of=/dev/sdc bs=1M status=progress
```

### Logging into the System

Login to the system via serial port.

Default username: `user`
Default password: `milkv`

## Expected Results

The system should boot up successfully, allowing login via onboard serial port, and access to the installation wizard.

## Actual Results

The system boots up successfully, and the output is viewable via the serial port.

### Boot Information

Screen recording:
[![asciicast](https://asciinema.org/a/v8FxrttpHTJVye5N4U5KCgUsT.svg)](https://asciinema.org/a/v8FxrttpHTJVye5N4U5KCgUsT)

```log
Debian GNU/LinuxDebian GNU/Linux bookworm/sid milkv hvc0

milkv login:  bookworm/sid milkv ttyS0

milkv login: user
Password: 
Linux milkv 5.15.0 #1 SMP Mon Nov 13 18:56:24 CST 2023 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
user@milkv:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux bookworm/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
BUILD_ID=40
user@milkv:~$ uname -a
Linux milkv 5.15.0 #1 SMP Mon Nov 13 18:56:24 CST 2023 riscv64 GNU/Linux
user@milkv:~$ 

```

## Test Criteria

Successful test: Actual results match the expected results.

Failed test: Actual results differ from the expected results.

## Test Conclusion

Successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
