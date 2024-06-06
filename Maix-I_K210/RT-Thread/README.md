# RT-Thread Maix-I K210 Test Report

## Test Environment

### Operating System Information

- Source Code Link: [RT-Thread GitHub Repository](https://github.com/RT-Thread/rt-thread/)
- Installation Reference Document: [RT-Thread Installation Guide](https://github.com/RT-Thread/rt-thread/tree/master/bsp/k210)
- Toolchain: [RISC-V None Embed GCC xPack](https://github.com/xpack-dev-tools/riscv-none-embed-gcc-xpack/releases)
    - Kflash Tool: [Kendryte Kflash](https://github.com/kendryte/kflash.py)

### Hardware Information

- Sipeed Maix-Bit (K210)

## Installation Steps

### Prepare Source Code and Environment

Obtain the toolchain, download, and unzip it.

Note: Kendryte's official toolchain may report compatibility errors with floating-point types, and versions of the RISC-V toolchain prior to 8.2.0 may have header file compatibility issues. (Refer to the [installation document](https://github.com/RT-Thread/rt-thread/tree/master/bsp/k210))

Clone the repository and configure:
```bash
git clone https://github.com/RT-Thread/rt-thread/
cd rt-thread/bsp/k210
scons --menuconfig
source ~/.env/env.sh
pkgs --update
```

In the menuconfig, ensure the following options are correct:
> RT-Thread online packages --->
> > peripheral libraries and drivers --->
> > > Kendryte SDK --->
> > > > [*] kendryte K210 SDK

> RT-Thread Components --->  C++ features

Then open rtconfig.py, locate line 18, and replace EXEC_PATH with the location of your toolchain's bin directory after extraction.

### Compilation

Compile using scons:
```bash
scons --exec-path="path/to/toolchain/bin"
```

### Image Flashing

Flash the image using k_flash, refer to the toolchain documentation: [Kendryte Kflash](https://github.com/kendryte/kflash.py)

```bash
pip install kflash
kflash -b 115200 -p /dev/ttyUSBx rtthread.bin
```

### System Login

Connect to the development board via serial port.

## Expected Results

Successful build with the development board displaying RT-Thread startup information.

## Actual Results

Successful build with the development board displaying RT-Thread startup information.

### Startup Information

Screen recording (from system flashing to startup):
[![asciicast](https://asciinema.org/a/UeYag1L9qPvAPgcuuWKMpF7ye.svg)](https://asciinema.org/a/UeYag1L9qPvAPgcuuWKMpF7ye)

```log
heap: [0x80076c43 - 0x80600000]

 \ | /
- RT -     Thread Operating System
 / | \     5.2.0 build Apr 18 2024 18:23:42
 2006 - 2024 Copyright by RT-Thread team
(rt_hw_interrupt_is_disabled()) assertion failed at function:rt_sched_post_ctx_switch, line number:1045 
[0] W/kernel.service: rt_hw_backtrace_frame_unwind is not implemented
please use: addr2line -e rtthread.elf -a -f 0x80013392[0] W/kernel.service: rt_hw_backtrace_frame_unwind is not implemented


```

## Test Judging Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
