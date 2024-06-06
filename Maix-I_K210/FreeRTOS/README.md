# FreeRTOS Maix-I K210 Test Report

## Test Environment

### Operating System Information

- Build System: Ubuntu 22.04.4 LTS (Docker)
- Source Code Link: [GitHub - kendryte/kendryte-freertos-sdk](https://github.com/kendryte/kendryte-freertos-sdk)
- Reference Installation Documentation: [GitHub - kendryte/kendryte-freertos-sdk](https://github.com/kendryte/kendryte-freertos-sdk)
- Toolchain: [GitHub - kendryte/kendryte-gnu-toolchain/releases/tag/v8.2.0-20190409](https://github.com/kendryte/kendryte-gnu-toolchain/releases/tag/v8.2.0-20190409)

### Hardware Information

- Sipeed Maix-Bit (K210)

## Installation Steps

### Create Docker Environment

```shell
sudo docker run -it --name ubuntu2204 ubuntu:22.04
```

All the following operations are performed in the root shell of Ubuntu 22.04.4 LTS Docker.

### Prepare Build Environment

```shell
apt update
apt install -y cmake git curl bzip2
cd /opt
curl -LO https://github.com/kendryte/kendryte-gnu-toolchain/releases/download/v8.2.0-20190409/kendryte-toolchain-ubuntu-amd64-8.2.0-20190409.tar.bz2
tar xvf kendryte-toolchain-ubuntu-amd64-8.2.0-20190409.tar.bz2
cd
```

### Build hello_world

Fetch the FreeRTOS repository to local and build it.

```shell
git clone --depth=1 https://github.com/kendryte/kendryte-freertos-sdk
cd kendryte-freertos-sdk
mkdir build && cd build
cmake .. -DPROJ=hello_world -DTOOLCHAIN=/opt/kendryte-toolchain/bin
make -j$(nproc)
```

After the build finishes, two files - `hello_world` and `hello_world.bin` - will be generated in the source code directory.

```log
[100%] Linking C executable hello_world                                             
Generating .bin file ...                                                            
[100%] Built target hello_world                                                     
root@4b1ebf5f94f4:~/kendryte-freertos-sdk/build# file hello_world
hello_world: ELF 64-bit LSB executable, UCB RISC-V, RVC, single-float ABI, version 1 (SYSV), statically linked, with debug_info, not stripped
```

### Flash Image

Use k_flash for flashing. Toolchain documentation can be found at: [kflash.py repository](https://github.com/kendryte/kflash.py)

```bash
pip install kflash
kflash -b 115200 -p /dev/ttyUSBx hello_world.bin
```

### System Login

Connect to the development board via serial port.

## Expected Result

Successful build with the development board displaying the Hello World message.

## Actual Result

Successful build with the development board displaying the Hello World message.

### Boot-up Information

Screen recording (from system flashing to boot-up):
[![asciicast](https://asciinema.org/a/uml0eDGjJXKoaFuPn2K1D2WSv.svg)](https://asciinema.org/a/uml0eDGjJXKoaFuPn2K1D2WSv)

```log
Hello World
```

## Test Judgment Criteria

Test Pass: Actual result matches the expected result.

Test Fail: Actual result does not match the expected result.

## Test Conclusion

Test Passed

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
