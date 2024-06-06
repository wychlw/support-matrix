# openEuler RISC-V 23.09 VisionFive Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.09 RISC-V preview
- Download Link: [Download Link](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive/)
- Installation Guide: [Installation Guide](https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/Visionfive)

### Hardware Information

- StarFive VisionFive
- Power adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Write Image to microSD Card Using `ruyi` CLI

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Log in to the System

Log in to the system via serial port.

Default Username: `openeuler`
Default Password: `openEuler12#$`

## Expected Results

The system boots up successfully and can be accessed through the onboard serial port.

## Actual Results

The system boots up successfully and logging in through the onboard serial port is successful.

### Boot Information

Screen recording (from writing the image to logging into the system):

[![asciicast](https://asciinema.org/a/lkduJVcErVoqb3ewZuzjl4TVi.svg)](https://asciinema.org/a/lkduJVcErVoqb3ewZuzjl4TVi)

```log
Welcome to 6.1.0-0.rc4.8.oe2309.riscv64

System information as of time:  Mon Sep 18 08:01:36 AM CST 2023

System load:    2.62
Processes:      120
Memory used:    2.4%
Swap used:      0.0%
Usage On:       4%
Users online:   1
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.1.0-0.rc4.8.oe2309.riscv64 #1 SMP Fri Oct 20 08:23:28 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release 
NAME="openEuler"
VERSION="23.09"
ID="openEuler"
VERSION_ID="23.09"
PRETTY_NAME="openEuler 23.09"
ANSI_COLOR="0;31"

[openeuler@openeuler-riscv64 ~]$ 

```

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
