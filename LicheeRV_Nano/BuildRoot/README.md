# BuildRoot LicheeRV Nano Test Report

## Test Environment

### Operating System Information

- System Version: 20240401
- Download Link: [LicheeRV Nano Build Releases](https://github.com/sipeed/LicheeRV-Nano-Build/releases)
- Installation Reference Document: [LicheeRV Nano Build Installation Document](https://github.com/sipeed/LicheeRV-Nano-Build/releases)

### Hardware Information

- LicheeRV Nano
- One type-c power cable
- One UART to USB debugger

## Installation Steps

### Write Image to microSD Card Using `dd`

Download the image, then unzip and write it to the microSD card:

```shell
gzip -kd c906-2024-04-10-14-19-16d76b.img.gz
sudo dd if=c906-2024-04-10-14-19-16d76b.img of=/dev/your_device bs=1M status=progress

```

### Log into System

Log into the system via serial port.

Default username: root
Default password: root

## Expected Results

The system should start up normally, and login should be possible via the onboard serial port.

## Actual Results

The system started up normally, and login was possible via the onboard serial port.

### Boot Information

Screen recording (from image writing to system login):

[![asciicast](https://asciinema.org/a/yNDWWKvYyXReaexbXm1t5dLxi.svg)](https://asciinema.org/a/yNDWWKvYyXReaexbXm1t5dLxi)

```log
Welcome to Linux
licheervnano-b6c0 login: root
licheervnano-b6c0 login: root
Password: 
# cat /etc/os-release 
NAME=Buildroot
VERSION=-g16d76badf-dirty
ID=buildroot
VERSION_ID=2023.11.2
PRETTY_NAME="Buildroot 2023.11.2"
# uname -a
Linux licheervnano-b6c0 5.10.4-tag- #1 PREEMPT Wed Apr 10 14:12:37 HKT 2024 riscv64 GNU/Linux
# 
 
```

## Test Determination Criteria

Test Success: Actual results match the expected results.

Test Failure: Actual results do not match the expected results.

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
