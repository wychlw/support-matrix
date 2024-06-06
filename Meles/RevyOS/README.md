
# RevyOS Meles Version Testing Report

## Test Environment

### Operating System Information

- System Version: root-meles-20231210_134926.ext4.tar.gz
- Download Link: [GitHub Repository](https://github.com/milkv-meles/meles-images/releases)
- Installation Reference: [Getting Started Guide](https://milkv.io/zh/docs/meles/getting-started/boot)

### Hardware Information

- Milk-V Meles 4GB/8GB
- eMMC Module > 16GB
- USB A to C Cable x1
- Optional: USB-TTL Debugger x1
- Optional: Keyboard, Monitor, Mouse (for GUI testing)

## Installation Steps

### Flash Image to Development Board Using `fastboot`

Download the system image and U-Boot SPL from the [GitHub release](https://github.com/milkv-meles/meles-images/releases).

Choose the u-boot-with-spl version:
- 4GB Version -> u-boot-with-spl-**single**rank.bin
- 8GB Version -> u-boot-with-spl-**dual**rank.bin

Press the download button near the GPIO interface on the development board and connect it to the computer.

Check the connection status:

```shell
$ lsusb | grep T-HEAD
Bus 001 Device 045: ID 2345:7654 T-HEAD USB download gadget
```

Next, use `fastboot` to flash the image.

If there are issues with `fastboot` recognizing the device or flashing, check the device connection and try executing `fastboot` with elevated privileges (`sudo`).

```shell
fastboot flash ram u-boot-with-spl-dualrank.bin
fastboot reboot
fastboot flash uboot u-boot-with-spl-dualrank.bin
fastboot flash boot boot.ext4
tar xvf root-meles-20231210_134926.ext4.tar.gz
fastboot flash root root-meles-20231210_134926.ext4
```

### System Login

Login to the system either via serial console or GUI.

Default username: `debian`
Default password: `debian`

## Expected Results

The system should boot up successfully and allow login via the serial console.

## Actual Results

The system booted up successfully and login via the serial console was also successful.

### Boot Information

CFT

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
