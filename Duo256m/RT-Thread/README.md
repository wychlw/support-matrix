# RT-Thread Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/RT-Thread/rt-thread
- Installation Reference Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek/cv18xx_risc-v
   - Toolchain: https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### Hardware Information

- Milk-V Duo 256M
- One USB-A to C or USB C to C cable
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Build Steps

### Fetch Source Code and Compile Firmware

Obtain the toolchain and configure:
```bash
wget https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
tar -xzvf Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
```

Modify the following paths accordingly:
```bash
export RTT_CC_PREFIX=riscv64-unknown-elf-
export RTT_EXEC_PATH=/opt/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1/bin
```

Fetch dependencies:
```bash
sudo apt install -y scons libncurses5-dev device-tree-compiler
```

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/
cd cv18xx_risc-v
# 生成配置文件
scons --menuconfig
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
cd ../
./combine-fip.sh $(pwd)/cv18xx_risc-v Image
```

Please select the 256M version.

After execution, two files, boot.sd and fip.bin, will be generated in the `output` directory.

### Prepare microSD Card

Clear the microSD card (you can use `wipefs -af /path/to/your-card`) and create a FAT32 partition.

Copy the generated boot.sd and fip.bin to the microSD card. At this point, the storage card is ready to boot RT-Thread on Duo.

### Log In to the System

Log in to the system via a serial port.

## Expected Results

The system should start up correctly, allowing login via the serial port.

## Actual Results

The system was successfully booted, and login via the serial port was successful.

### Boot Information

```log
Starting kernel ...

heap: [0x8028c410 - 0x8128c410]

 \ | /
- RT -     Thread Operating System
 / | \     5.2.0 build May 28 2024 12:05:25
 2006 - 2024 Copyright by RT-Thread team
lwIP-2.1.2 initialized!
[I/sal.skt] Socket Abstraction Layer initialize success.
Hello RISC-V!
msh />

```

Screen recording (from flashing the image to logging into the system):
[![asciicast](https://asciinema.org/a/3zKnnFwIlQLKPek64gfsjmaqK.svg)](https://asciinema.org/a/3zKnnFwIlQLKPek64gfsjmaqK)

## Testing Criteria

Successful Test: Actual results match the expected results.

Failed Test: Actual results do not match the expected results.

## Test Conclusion

Successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
