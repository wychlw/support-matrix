# FreeRTOS LicheeRV Nano Test Report

## Test Environment

### Operating System Information

- System Version: 20240401
- Download Link: [**Download link**](https://github.com/sipeed/LicheeRV-Nano-Build/releases)
- Installation Reference Document: [**Installation guide**](https://github.com/sipeed/LicheeRV-Nano-Build/releases)

### Hardware Information

- LicheeRV Nano
- One Type-C power cable
- One UART to USB debugger

## Installation Steps

FreeRTOS for LicheeRV Nano is integrated into the Linux SDK, communicating with the Linux system using a mailbox.

### Checking FreeRTOS Device

Communication between FreeRTOS and Linux is achieved through a mailbox, located in `/dev` as `cvi-rtos-cmdqu`.

### System Login

Log into the system via serial port.

Default username: root
Default password: root

## Expected Result

The system starts up normally, and the rtos device is visible.

## Actual Result

The system boots up successfully, and the rtos device is visible.

### Boot Information

```log

Welcome to Linux
licheervnano-b6c0 login: root
licheervnano-b6c0 login: root
Password: 
# ls /dev/ | grep rtos
cvi-rtos-cmdqu
# 

```

Screen recording:

[![asciicast](https://asciinema.org/a/zG1HsQyGWkGTVHFI74Nwhxcv8.svg)](https://asciinema.org/a/zG1HsQyGWkGTVHFI74Nwhxcv8)

## Test Criteria

Test Passed: Actual result matches the expected result.

Test Failed: Actual result does not match the expected result.

## Test Conclusion

Test Passed

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
