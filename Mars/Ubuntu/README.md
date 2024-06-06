# Ubuntu on Milk-V Mars

## Test Environment

### Operating System Information

- Ubuntu
  - Download link:
  - Reference installation document: [Getting Started with Milk-V Mars](https://milkv.io/docs/mars/getting-started/boot)

### Hardware Development Board Information

- Milk-V Mars

## Installation Steps

### Flashing the Image

Use `unxz` to decompress the image.
Use `dd` to write the image to the microSD card.

The `/dev/sdc` corresponds to the storage card.

```bash
unxz -d ubuntu-24.04-preinstalled-server-riscv64+milkvmars.img.xz
sudo dd if=ubuntu-24.04-preinstalled-server-riscv64+milkvmars.img of=/dev/sdc bs=1M status=progress
```

### Updating U-Boot

**If encountering Kernel Panic during startup, update U-Boot**

Insert the SD card with the burned image, press Enter quickly when Hit any key to stop autoboot appears in the serial terminal to enter the U-boot command-line terminal.
Once in the U-Boot console, enter the following commands:
```bash
sf probe
load mmc 1:1 $kernel_addr_r /usr/lib/u-boot/starfive_visionfive2/u-boot-spl.bin.normal.out
sf update $kernel_addr_r 0 $filesize
load mmc 1:1 $kernel_addr_r /usr/lib/u-boot/starfive_visionfive2/u-boot.itb
sf update $kernel_addr_r 0x100000 $filesize
```

### Logging into the System

Log into the system via serial port.

Default username: `ubuntu`
Default password: `ubuntu`

## Expected Results

System boots up successfully, can log in via the onboard serial port, and can access the installation wizard.

## Actual Results

System boots up successfully, and the output can be viewed via the serial port.

### Boot Information

Screen recording:
[![asciicast](https://asciinema.org/a/a3DgDMfhYPQgWhUjTTScbJ04n.svg)](https://asciinema.org/a/a3DgDMfhYPQgWhUjTTScbJ04n)

```log
Welcome to Ubuntu 24.04 LTS (GNU/Linux 6.8.0-31-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information disabled due to load higher than 1.0

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ cat /etc-o
cat: /etc-o: No such file or directory
ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 24.04 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.8.0-31-generic #31.1-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr 21 01:12:53 UTC 2024 riscv64 riscv64 riscv64 GNU/Lix
ubuntu@ubuntu:~$ 
 

```

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
