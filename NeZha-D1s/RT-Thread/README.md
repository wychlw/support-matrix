# RT-Thread D1s NeZha Test Report

## Test Environment

### Operating System Information

- Download Link: [GitHub - RT-Thread](https://github.com/RT-Thread/rt-thread)
- Installation Reference Document: [RT-Thread D1s README](https://github.com/RT-Thread/rt-thread/blob/master/bsp/allwinner/d1s/README-M7.md)

### Hardware Information

- D1s NeZha
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

Unzip the tool xfel_v1.2.9.7z under tools and prepare to use xfel for flashing to emmc:
```bash
xfel write 8192 boot0_sdcard_sun20iw1p1_f133.bin
xfel sd write 57344 sd.bin
xfel reset
```

### Login to System

Log in to the system via serial port.

## Expected Results

The system should boot up normally and allow login via the onboard serial port.

## Actual Results

The system booted up successfully and allowed login via the onboard serial port.

### Boot Information

Screen recording (from flashing the image to logging into the system):
```log
```

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
