# Ubuntu VisionFive Test Report

## Test Environment

### System Information

- System Version: Ubuntu 23.10
- Download Link: [https://ubuntu.com/download/risc-v](https://ubuntu.com/download/risc-v)
- Reference Installation Documentation: [https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive](https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive)

### Hardware Information

- StarFive VisionFive
- Power Adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Flash Image

Use `unxz` to decompress the image.
Use `dd` to write the image to the microSD card.

```bash
unxz /path/to/ubuntu.img.xz
sudo dd if=/path/to/ubuntu.img of=/dev/your-device bs=1M status=progress
```

### System Login

Login to the system via serial port.

Default username: `ubuntu`
Default password: `ubuntu`

Upon initial boot, changing the password will be mandatory.

## Expected Results

The system should boot up correctly and allow login via the onboard serial port.

## Actual Results

The system booted up correctly and login via the onboard serial port was successful.

### Boot Information

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/yNX1czhlpU8K0CwIDzan6PZ9Q.svg)](https://asciinema.org/a/yNX1czhlpU8K0CwIDzan6PZ9Q)

```log
Welcome to Ubuntu 23.10 (GNU/Linux 6.5.0-1002-starfive riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Sep 19 15:58:17 UTC 2023

  System load:  0.71              Swap usage:  0%       Users logged in: 0
  Usage of /:   3.3% of 57.48GB   Temperature: 51.8 C
  Memory usage: 2%                Processes:   105

0 updates can be applied immediately.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.5.0-1002-starfive #3-Ubuntu SMP Sat Oct  7 21:23:58 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 23.10"
NAME="Ubuntu"
VERSION_ID="23.10"
VERSION="23.10 (Mantic Minotaur)"
VERSION_CODENAME=mantic
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=mantic
LOGO=ubuntu-logo

```

## Testing Criteria

Test Passed: The actual results match the expected results.

Test Failed: The actual results do not match the expected results.

## Test Conclusion

The test was successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
