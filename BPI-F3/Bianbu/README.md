# Bianbu Banana Pi BPI-F3 Test Report

## Test Environment

### System Information

- Download Links:
  - Baidu Cloud: [Download here](https://pan.baidu.com/s/15owwUEjIU_i26cI1iigAew?pwd=8888) (pincode: 8888)
  - Google Drive: [Download here](https://drive.google.com/drive/folders/1LQoioz6N5YQpSOxY47OmetnPX4yggtT0?usp=sharing)
- Download Links (Desktop Version):
  - Baidu Cloud: [Download here](https://pan.baidu.com/s/1zvFkX92f5gpZdKjP-vGJvA?pwd=8888) (pincode: 8888)
  - Google Drive: [Download here](https://drive.google.com/drive/folders/1kCHiMwjnhvZaRBy5vkj6UlPeAlpRQ14P?usp=sharing)
- Reference Installation Document: [BPI-F3 Getting Started Guide](https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3)

### Hardware Information

- Bianbu Banana Pi BPI-F3
- Power Adapter
- One microSD card
- One USB to UART Debugger

## Installation Steps

### Flashing Image (SD Card)

**Please make sure to download a compressed file ending with `.img.zip`.**
Download and extract the image, then use `dd` to write the image to the microSD card.

```bash
unzip Bianbu-23.10-desktop-k1-v1.0rc1-release-20240429194149.img
sudo dd if=/path/to/Bianbu-23.10-desktop-k1-v1.0rc1-release-20240429194149.img of=/dev/your-device bs=1M status=progress
```

### System Login

Login to the system via serial port.

Default username: `root`
Default password: `bianbu`

## Expected Results

The system boots up successfully, and login is possible via the onboard serial port.

## Actual Results

The system boots up successfully, and login via the onboard serial port is successful.

### Boot Information

Screen recording (from flashing the image to logging into the system):
[![asciicast](https://asciinema.org/a/TFRjqFjOEIHc38Wha93bw0ti8.svg)](https://asciinema.org/a/TFRjqFjOEIHc38Wha93bw0ti8)

```log
Bianbu 1.0rc1 k1 ttyS0k1 login: root
密码： 
Welcome to Bianbu 1.0rc1 (GNU/Linux 6.1.15 riscv64)

 * Documentation:  coming soon
 * Management:     coming soon
 * Support:        coming soon

0 updates can be applied immediately.


The programs included with the Bianbu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Bianbu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@k1:~# cat /etc/os-release 
PRETTY_NAME="Bianbu 1.0rc1"
NAME="Bianbu"
VERSION_ID="1.0rc1"
VERSION="1.0rc1 (Mantic Minotaur)"
VERSION_CODENAME=mantic
ID=bianbu
ID_LIKE=debian
HOME_URL="coming soon"
SUPPORT_URL="coming soon"
BUG_REPORT_URL="coming soon"
PRIVACY_POLICY_URL="coming soon"
UBUNTU_CODENAME=mantic
LOGO=ubuntu-logo
root@k1:~# uname -a
Linux k1 6.1.15 #1.0~rc1 SMP PREEMPT Mon Apr 29 09:05:59 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
root@k1:~# 

```

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

Successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
