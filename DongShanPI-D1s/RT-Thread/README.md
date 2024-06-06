# RT-Thread DongshanPI-D1s Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/RT-Thread/rt-thread
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/blob/master/bsp/allwinner/d1s/README-MQ.md

### Hardware Information

- DongshanPI-D1s
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Download Code

Download RT-Thread code:
```bash
git clone https://github.com/RT-Thread/userapps.git
cd userapps
git clone -b rt-smart https://gitee.com/rtthread/rt-thread.git
```

Configure the toolchain:
```bash
python3 get_toolchain.py riscv64
source smart-env.sh riscv64
```

Compile the kernel:
```bash
scons --menuconfig
source ~/.env/env.sh
pkgs --update
```

### Flash Image

Partition the SD card: reserve 8M space at the front for the bootloader:
```bash
sudo fdisk /dev/your/device
# In fdisk
o
n
p
1
16384
w
```

Write the system image to the SD card:
```bash
sudo dd if=boot0_sdcard_sun20iw1p1.bin of=/dev/your/device bs=1024 seek=8
sudo dd if=sd.bin of=/dev/your/device bs=1024 seek=56
```

### Log in to the System

Log in to the system via serial port.

## Expected Results

The system should boot up normally and allow login via the onboard serial port.

## Actual Results

The system booted up successfully, and login via the onboard serial port was successful.

### Boot Information


Screen recording (from flashing the image to logging into the system):

```log
```


## Test Judgment Criteria

Test Passed: The actual results match the expected results.

Test Failed: The actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
