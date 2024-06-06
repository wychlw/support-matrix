
# FreeRTOS Sipeed M0s Dock Test Report

## Test Environment

### Operating System Information

- Download Link: [here](https://github.com/sipeed/M0S_BL616_example)
    - Toolchain: [here](https://gitee.com/bouffalolab/toolchain_gcc_t-head_linux)
- Reference Installation Document: [here](https://github.com/sipeed/M0S_BL616_example)
    - [here](https://bl-mcu-sdk.readthedocs.io/zh-cn/latest/get_started/get_started.html)

### Hardware Information

- Sipeed M0s Dock
- One Type-C cable

## Installation Steps

### Get SDK and Toolchain

Clone the relevant repositories to the working directory:
```bash
git clone https://github.com/sipeed/M0S_BL616_example.git
git clone https://gitee.com/bouffalolab/toolchain_gcc_t-head_linux.git
```

Configure the environment:
```bash
export PATH=path/to/toolchain_gcc_t-head_linux/bin:$PATH
```

### Compilation

Compile the FreeRTOS demo:
```bash
cd M0S_BL616_example/examples/freertos
make CHIP=bl616 BOARD=bl616dk
```

### Flashing Program

Connect the computer and the C port using a Type-C cable.

Press and hold the boot button, then connect the C port to power up.

Then:
```bash
make flash CHIP=bl616 COMX=/dev/ttyACM0 # Change com on your machine
```

### Connect Serial Port

The serial port for connection is located next to the C port, with a baud rate of 2000000.

## Expected Results

The system boots up normally, and serial output is visible.

## Actual Results

The system boots up normally, and serial output is visible.

### Startup Information

```log
  ____               __  __      _       _       _     
 |  _ \             / _|/ _|    | |     | |     | |    
 | |_) | ___  _   _| |_| |_ __ _| | ___ | | __ _| |__  
 |  _ < / _ \| | | |  _|  _/ _` | |/ _ \| |/ _` | '_ \ 
 | |_) | (_) | |_| | | | || (_| | | (_) | | (_| | |_) |
 |____/ \___/ \__,_|_| |_| \__,_|_|\___/|_|\__,_|_.__/ 

Build:11:07:19,Apr 28 2024
Copyright (c) 2022 Bouffalolab team
flash init fail!!!
=========== flash cfg ==============
jedec id   0x000000
mid            0xC8
iomode         0x11
clk delay      0x00
clk invert     0x03
read reg cmd0  0x05
read reg cmd1  0x35
write reg cmd0 0x01
write reg cmd1 0x31
qe write len   0x01
cread support  0x00
cread code     0x20
burst wrap cmd 0x77
=====================================
dynamic memory init success,heap size = 187 Kbyte 
sig1:ffffffff
sig2:0000f32f
cgen1:9f7ffffd
[I][MAIN] [OS] Starting consumer task...
[I][MAIN] [OS] Starting producer task...
[I][MAIN] Consumer task enter 
[I][MAIN] Producer task enter 
[I][MAIN] Consumer task start 
[I][MAIN] begin to loop /home/lw/Work/plct/boards/m0s/M0S_BL616_example/examples/freertos/main.c
[I][MAIN] Consumer get:
[I][MAIN] Producer task start 
[I][MAIN] Producer generates:101
[I][MAIN] Consumer get:101
[I][MAIN] Producer generates:102
[I][MAIN] Consumer get:102
[I][MAIN] Producer generates:103
[I][MAIN] Consumer get:103
[I][MAIN] Producer generates:104
[I][MAIN] Consumer get:104
[I][MAIN] Producer generates:105
[I][MAIN] Consumer get:105



```

Screen Recording:

[![asciicast](https://asciinema.org/a/zH5ndg9eZTbjEHEkWFfAxVNQk.svg)](https://asciinema.org/a/zH5ndg9eZTbjEHEkWFfAxVNQk)

## Test Judgement Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.


> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
