# NuttX Maix-I K210 Test Report

## Test Environment

### Operating System Information

- Source Code Link: [NuttX GitHub Repository](https://github.com/apache/nuttx)
- Installation Reference Document: [NuttX Maix Bit Installation Guide](https://nuttx.apache.org/docs/latest/platforms/risc-v/k210/boards/maix-bit/index.html)
- Toolchain:
    - Toolchain Download: [RISC-V Toolchain](https://static.dev.sifive.com/dev-tools/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14.tar.gz)
    - OpenOCD (for debugging if needed): [OpenOCD Kendryte Repository](https://github.com/kendryte/openocd-kendryte)
    - Kflash: [Kflash.py Repository](https://github.com/kendryte/kflash.py)

### Hardware Information

- Sipeed Maix-Bit (K210)

## Installation Steps

### Prepare Source Code and Environment

Obtain the toolchain by downloading and extracting it.
```bash
wget https://static.dev.sifive.com/dev-tools/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14.tar.gz
tar -xzvf riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14.tar.gz
export PATH=path/to/toolchain/bin:$PATH
```

Clone the repository and configure:
```bash

mkdir nuttx && cd nuttx
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps.git apps
```


### Compilation

```bash
cd nuttx
make distclean
./tools/configure.sh maix-bit:nsh
make V=1
```

### Image Burning

Use kflash for burning the image. For toolchain documentation, please refer to: [Kflash.py Repository](https://github.com/kendryte/kflash.py)

```bash
pip install kflash
kflash -b 115200 -p /dev/ttyUSBx nuttx.bin
```

### Accessing the System

Connect to the development board via serial port.

## Expected Results

Successful build with normal boot-up information displayed on the development board.

## Actual Results

Successful build with normal boot-up information displayed on the development board.

### Boot-up Information

Screen recording (from system flashing to boot-up):
[![asciicast](https://asciinema.org/a/WlWIs9g3WqjlO9zX9t0pq2ZPU.svg)](https://asciinema.org/a/WlWIs9g3WqjlO9zX9t0pq2ZPU)

```log
NuttShell (NSH) NuttX-12.5.1
nsh> cat /proc/version
NuttX version 12.5.1 6e941aed8b-dirty May  7 2024 09:51:35 maix-bit:nsh
nsh>
```

## Test Criteria

Test Successful: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
