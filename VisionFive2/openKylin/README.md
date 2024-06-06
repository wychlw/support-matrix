# openKylin 1.0.1 VisionFive 2 Version Test Report

## Test Environment

### Operating System Information

- System Version: openKylin 1.0.1
- Download Link: [OpenKylin Download Page](https://www.openkylin.top/downloads/index-cn.html)
- Installation Reference Document: [Installation Guide for openKylin on RISC-V](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

### Hardware Information

- StarFive VisionFive 2
- USB Power Adapter x1
- USB-A to C or C to C Cable x1
- microSD Card x1
- USB to UART Debugger x1 (e.g., CH340, CH341, FT2232, etc.)
- Dupont Wires x3

## Installation Steps

### Unzip and Flash Image to microSD Card

Assuming `/dev/sdc` is the storage card.

```bash
xz -d openKylin-1.0.1-visionfive2-riscv64.img.xz 
sudo dd if=openKylin-1.0.1-visionfive2-riscv64.img of=/dev/sdc bs=1M status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 offers multiple boot modes that can be configured via on-board dip switches before power-on. The development board itself also has silk screen indications.

To boot the openKylin image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require firmware update in the Flash in advance. If booting is unsuccessful, please refer to the official documentation for firmware upgrade: [Updating SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### Login to System

Login to the system via serial port.

Default Username: `openkylin`
Default Password: `openkylin$`

## Expected Results

The system starts up normally and is accessible through the graphical interface.

## Actual Results

The system boots up successfully and login is achieved through the graphical interface.

### Boot Information

Screen recording (from image flashing to system login):

```log
openkylin@openkylin:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

openkylin@openkylin:~$ uname -a
Linux openkylin 5.15.0 #1 SMP Fri Sep 1 11:22:00 CST 2023 riscv64 riscv64 riscv64 GNU/Linux
openkylin@openkylin:~$ cat /etc/os-release 
NAME="openKylin"
FULL_NAME="openKylin"
VERSION="1.0.1 (yangtze)"
VERSION_US="1.0.1 (yangtze)"
ID=openkylin
PRETTY_NAME="openKylin 1.0.1"
VERSION_ID="1.0.1"
HOME_URL="https://www.openkylin.top/"
VERSION_CODENAME=yangtze
PRODUCT_FEATURES=3
openkylin@openkylin:~$
```

Screen recording (from flashing to boot):

[![asciicast](https://asciinema.org/a/qoDqBWFEJlBPhIBva66HFGzd9.svg)](https://asciinema.org/a/qoDqBWFEJlBPhIBva66HFGzd9)

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
