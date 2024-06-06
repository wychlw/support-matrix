# RT-Thread Mangopi MQ test report

## Test Environment

### Operating System Information

- Download link: [Download Link](https://github.com/RT-Thread/rt-thread)
- Reference installation document: [Installation Document](https://github.com/RT-Thread/rt-thread/blob/master/bsp/allwinner/d1s/README-MQ.md)

### Hardware Information

- Mangopi MQ
- One microSD card
- One USB to UART debugger (e.g.: CH340, CH341, FT2232, etc.)

## Installation Steps

### Download Code

Download RT-Thread code:
```bash
git clone https://github.com/RT-Thread/userapps.git
cd userapps
git clone -b rt-smart https://gitee.com/rtthread/rt-thread.git
```

Configure toolchain:
```bash
python3 get_toolchain.py riscv64
source smart-env.sh riscv64
```

Compile kernel:
```bash
scons --menuconfig
source ~/.env/env.sh
pkgs --update
```

### Flash Image

Partition the SD card: leave 8M space at the front to accommodate the bootloader:
```bash
sudo fdisk /dev/your/device
# 以下在fdisk中
o
n
p
1
16384
w
```

Flash the system to the SD card:
```bash
sudo dd if=boot0_sdcard_sun20iw1p1.bin of=/dev/your/device bs=1024 seek=8
sudo dd if=sd.bin of=/dev/your/device bs=1024 seek=56
```

### Login System

Login to the system via serial port.

## Expected Results

The system boots up normally, and can be accessed through the onboard serial port.

## Actual Results

The system boots up normally and successfully accessed through the onboard serial port.

### Boot Information

Screen recording (from flashing the image to logging into the system):

```log
```

## Test Judgement Criteria

Test successful: Actual results match the expected results.

Test failed: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
