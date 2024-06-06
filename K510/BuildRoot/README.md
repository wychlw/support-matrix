# BuildRoot K510 Test Report

## Test Environment

### Operating System Information

- Build system environment: Ubuntu 20.04.4 LTS in Docker
- System version: v1.9
- Reference installation document: [https://github.com/kendryte/k510_buildroot](https://github.com/kendryte/k510_buildroot)

### Hardware Information

- Canaan K510 CRB-V1.2 KIT
- One USB power adapter
- Two USB-A to C cables (one for power supply, the other for USB-UART and auxiliary power supply provided with the development board)
- One microSD card (capacity ≥ 1GiB, image size default to 512MiB)

## Installation Steps

### Build System Image

#### Install Docker

Please refer to the documentation of your distribution or the official Docker documentation for installation.

#### Clone the Source Code Repository

```shell
git clone --depth=1 https://github.com/kendryte/k510_buildroot
```

#### Start the Build

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
make dl
make
```

Note that by default, it compiles in single-thread which takes a long time, please ensure a stable network connection.

After compilation, the `sysimage-sdcard.img` image will be generated in the `k510_buildroot/k510_crb_lp3_v1_2_defconfig/image/` directory.

#### Write the Image using dd

Note that `/dev/sdc` is the location of the storage card. Please modify according to your actual situation.

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M status=progress
```

### Login to the System

Insert the microSD card and make sure the onboard SW1 switch is set to the microSD card boot location:

| BOOT1  | BOOT0  | Boot Mode   |
|--------|--------|------------|
| 0(ON)  | 0(ON)  | Serial      |
| 0(ON)  | 1(OFF) | microSD     |
| 1(OFF) | 0(ON)  | NAND Flash  |
| 1(OFF) | 1(OFF) | eMMC        |

Insert the USB Type-C for power supply and USB-UART serial port. The interfaces are located on both sides of the development board, labeled as `DC:5V` and `UART`.

(The K510 board is equipped with a CH340 for USB-UART, which can be directly connected and used. The UART interface also serves as a USB auxiliary power supply, and it is recommended to connect it.)

Turn the power switch `K1` to the ON position, connect via serial port, and log in to the system.

## Expected Result

The system starts up normally and can be logged in via the onboard serial port.

## Actual Result

The system starts up normally and successfully logged in via the onboard serial port.

### Boot Information

```log
[root@canaan ~ ]$ uname -a
Linux canaan 4.17.0 #1 SMP PREEMPT Fri Apr 12 18:13:44 CST 2024 riscv64 GNU/Linux
[root@canaan ~ ]$ cat /etc/os-release
NAME=Buildroot
VERSION=-g2ce01d0
ID=buildroot
VERSION_ID=2020.02.11
PRETTY_NAME="Buildroot 2020.02.11"
[root@canaan ~ ]$ cat /proc/cpuinfo
hart    : 0
isa     : rv64i2p0m2p0a2p0f2p0d2p0c2p0xv5-0p0
mmu     : sv39

hart    : 1
isa     : rv64i2p0m2p0a2p0f2p0d2p0c2p0xv5-0p0
mmu     : sv39

[root@canaan ~ ]$
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/wdVYHHOcy5laeXA2tKewkqNRR.svg)](https://asciinema.org/a/wdVYHHOcy5laeXA2tKewkqNRR)

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
