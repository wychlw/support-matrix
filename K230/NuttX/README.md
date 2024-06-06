# NuttX CanMV K230 Test Report

## Test Environment

### Operating System Information

- Source Code Link: [NuttX Github Repository](https://github.com/apache/nuttx)
- Installation Reference Document: [NuttX Installation Guide for Canaan Kendryte K230](https://nuttx.apache.org/docs/latest/platforms/risc-v/k230/boards/canmv230/index.html)
- Toolchains:
    - SDK: [Kendryte K230 SDK](https://github.com/kendryte/k230_sdk)
    - Boot Image: [Custom Boot Image for CanMV K230](https://gitee.com/yf1972/filexfers/tree/canmv230-tools-for-nuttx-v1.2)
    - SBI: [K230 OpenSBI](https://github.com/yf13/k230osbi)
    - Toolchain: [RISC-V GCC Toolchain by xPack](https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack)
    - kflash Tool: [Kendryte Flash Tool kflash.py](https://github.com/kendryte/kflash.py)

### Hardware Information

- Development Board: Canaan Kendryte K230
- USB A to C / USB C to C cables
- SD Card
- Network connection and TFTP server

## Installation Steps

### Prepare Source Code and Environment

Obtain pre-built boot image:
```bash
wget https://gitee.com/yf1972/filexfers/releases/download/canmv230-tools-for-nuttx-v1.2/canmv230-opensbi-dtb.tar.xz
wget https://gitee.com/yf1972/filexfers/releases/download/canmv230-tools-for-nuttx-v1.2/canmv230-sdcard.img.xz
```

Obtain toolchain:
```bash
wget https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases/download/v13.2.0-2/xpack-riscv-none-elf-gcc-13.2.0-2-linux-x64.tar.gz
tar -xvzf xpack-riscv-none-elf-gcc-13.2.0-2-linux-x64.tar.gz
export PATH=path/to/toolchain/bin:$PATH
```

Clone the repository and configure:
```bash
mkdir nuttx && cd nuttx
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps.git apps
```

### Build NuttX

```bash
cd nuttx
make distclean
./tools/configure.sh canmv230:nsh
make -j$(nproc)
```

### Flash Image

Flash the SBI environment on the SD Card:
```bash
unxz -k canmv230-sdcard.img.xz
sudo dd if=canmv230-sdcard.img of=/dev/your/device bs=1M status=progress
```

### Start NuttX

Place the compiled nuttx.bin into the TFTP server, load and run it in the U-boot console (manually interrupt autoboot):
```bash
k230# usb start
k230# env edit serverip
env: your.tftp.server.ip
k230# dhcp
k230# ping $serverip
k230# tftp 8000000 nuttx.bin
k230# go 8000000
```

### Login to the System

Connect to the development board via serial port.

## Expected Results

Successful build with normal boot information output on the development board.

## Actual Results

Successful build with normal boot information output on the development board.

### Boot Information

Screen recording (from system flashing to boot):
[![asciicast](https://asciinema.org/a/wxzebwRRYH909rIlx69ISi3ar.svg)](https://asciinema.org/a/wxzebwRRYH909rIlx69ISi3ar)

```log
## Starting application at 0x08000000 ...
ABC
NuttShell (NSH) NuttX-12.5.1
nsh> cat /proc/version
NuttX version 12.5.1 6e941aed8b May  7 2024 10:24:29 canmv230:nsh
nsh> 
```

## Test Judgment Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

Test Passed

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
