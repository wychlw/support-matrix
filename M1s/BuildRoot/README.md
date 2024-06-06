# BuildRoot Sipeed M1s Dock Test Report

## Test Environment

### Operating System Information

- System Version: 20240401
- Download Link: [Click here](https://github.com/sipeed/LicheeRV-Nano-Build/releases)
    - Pre-compiled image: [Download here](https://dl.sipeed.com/fileList/MAIX/M1s/M1s_Dock/7_Firmware/m1sdock_linux_20221116.zip)
- Reference Installation Documentation: [Click here](https://github.com/sipeed/LicheeRV-Nano-Build/releases)

### Hardware Information

- Sipeed M1s Dock
- One Type-C cable

## Installation Steps

### Obtain Image

Download and unzip the pre-compiled image:
```bash
wget https://dl.sipeed.com/fileList/MAIX/M1s/M1s_Dock/7_Firmware/m1sdock_linux_20221116.zip
unzip m1sdock_linux_20221116.zip

```

### Program Flash via Serial Port

Connect the computer and the C port **labeled with UART** using the Type-C cable.

Download the burning tool and use the corresponding tool to flash.

After powering on, press and hold the boot button, then press the reset button, and release the boot button.

Enter the MCU page, flash m0 and d0 (files are low_load_bl808_m0/d0@0x58000000.bin), address is 0x58000000, both groups are group 0. Choose high-speed port for serial communication!

![mcu](./mcu.png)

Next, go to the IOT page, check Single Download Options, fill in the start address with the file name, and flash the whole_img file.

![iot](./iot.png)

### Connect Serial Port

Connect the Type-C cable to the C port **labeled with UART**.

## Expected Results

The system boots up normally, and serial output is visible.

## Actual Results

The system boots up normally, and serial output is visible.

### Boot Information

```log
--------Start Local Services--------
********************************
********************************

Linux login: root
login[40]: root login on 'ttyS0'
Processing /etc/profile ... 
Set search library path in /etc/profile
Set user path in /etc/profile
id: unknown ID 0
Welcome to Linux
[@Linux root]#uname -a
Linux Linux 5.10.4 #4 SMP Fri Nov 4 18:23:30 CST 2022 riscv64 GNU/Linux
[@Linux root]#cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdcvsu
mmu             : sv39
model name      : T-HEAD C910
freq            : 1.2GHz
icache          : 64kB
dcache          : 64kB
l2cache         : 2MB
tlb             : 1024 4-ways
cache line      : 64Bytes
address sizes   : 40 bits physical, 39 bits virtual
vector version  : 0.7.1

[@Linux root]#

```

Screen recording (entering the system):

[![asciicast](https://asciinema.org/a/R5eNAV87OGvoJfoNcpVCtMKRO.svg)](https://asciinema.org/a/R5eNAV87OGvoJfoNcpVCtMKRO)

## Test Judgment Criteria

Test Passed: Actual results match expected results.

Test Failed: Actual results do not match expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
