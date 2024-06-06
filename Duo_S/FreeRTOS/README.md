
# FreeRTOS Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Build System: Ubuntu 22.04.4 LTS x86_64
- System Version: Duo-V1.1.0
- Download Link: [here](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
- Installation Reference Document: [here](https://github.com/milkv-duo/duo-buildroot-sdk)
    - FreeRTOS: [link](https://milkv.io/zh/docs/duo/getting-started/rtoscore)

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- One USB power adapter
- One USB-A to C or USB C to C cable, for powering the development board
- One microSD card
- One USB card reader
- One USB to UART debugger (CP2102, FT2232, etc., do not use CH340/341 series to avoid garbled text)
- Three DuPont wires

## Installation Steps

### Building the mailbox-test Binary

Clone the duo-examples repository locally and build.

```shell
sudo apt install -y wget git make
git clone https://github.com/milkv-duo/duo-examples --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```

### Flashing the Image to microSD Card using `ruyi` CLI

Install [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

#### Copy the compiled binary to the microSD card

```shell
sudo mount /dev/sdX2 /mnt
cp ~/duo-examples/mailbox-test/mailbox_test /mnt/root/
sudo umount /mnt
sudo eject /dev/sdX2
```

At this point, the SD card is ready. Insert it into the development board and prepare for booting.

### Logging into the System

Log into the system via the serial port.

## Expected Outcome

The system starts up normally, runs the `mailbox_test` binary after logging in via the onboard serial port, and the onboard blue LED turns on and then off.

(Standby mode indicated by blinking blue LED)

## Actual Outcome

The system starts up normally, successfully logged in via the onboard serial port; however, the official Duo S image currently does not support wiringX. Thus, the `mailbox_test` did not run as expected, but the system has detected the rtos device.

### Boot Information

```log
[root@milkv-duo]~# ls
mailbox_test
[root@milkv-duo]~# insmod: can't insert '/mnt/system/ko/aic8800_fdrv.ko': No such device
[root@milkv-duo]~# ./mailbox_test
Error loading shared library libwiringx.so: No such file or directory (needed by ./mailbox_test)
[root@milkv-duo]~# find / -name *rtos*
find: /proc/338: No such file or directory
/sys/devices/platform/1900000.rtos_cmdqu
/sys/bus/platform/devices/1900000.rtos_cmdqu
/sys/firmware/devicetree/base/rtos_cmdqu
[root@milkv-duo]~#
```

Screen recording:

[![asciicast](https://asciinema.org/a/y8YaDpY5YnKWgw4ydZPVDf4YB.svg)](https://asciinema.org/a/y8YaDpY5YnKWgw4ydZPVDf4YB)

## Test Judgment Criteria

Test Passed: Actual outcome matches the expected outcome.

Test Failed: Actual outcome does not match the expected outcome.

## Test Conclusion

Test Failed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
