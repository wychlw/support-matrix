# Zephyr Tang Mega 138K Pro Test Report

## Test Environment

### Operating System Information

- Build System: Linux
- FreeRTOS
- Source Code Download Link: [RiscV_AE350_SOC_V1.1.zip](https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip)
    - Bitstream: [TangMega-138KPro-example](https://github.com/sipeed/TangMega-138KPro-example)
- Installation Reference Document: [Gowin RiscV AE350 SOC Software Programming User Manual](https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf)
- Design Reference Document: [Gowin RiscV AE350 SOC Hardware Design User Manual](https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf)

### Hardware Information

- FreeRTOS Tang Mega 138K Pro Dock
- Type A to C cable x1
- UART serial cable x1
- Random power cable

## Installation Steps

**The following steps are based on building in a Linux system. For Windows, please install AE350 SOC RDS and perform the same operations in the included cygwin environment unless specified otherwise**

*If IDE functionality is not required, RDS License is not needed for building in Windows*

### Copy Code

The Zephyr code is located in the compressed source package under the path ref_design/MCU_RefDesign/ae350_zephyr. Extract it to your working directory.

### Compile Code

Navigate to the code directory and set the environment variables:
```bash
source zephyr-env.sh
export ZEPHYR_TOOLCHAIN_VARIANT='cross-compile
```

Set up the cross-compilation toolchain. It is recommended to use nds32le-elf-mculib-v5 here:
```bash
export CROSS_COMPILE=path/to/nds32le-elf-mculib-v5/bin/riscv32-elf-
```

For Windows, this file is located in the toolchains directory under the RDS installation directory.

Access the hello_world directory:
```bash
cd samples/hello_world
```

Prepare the build files:
```bash
mkdir build
cd build
cmake -DBOARD=adp_xc7k_ae350 ../
```

Configure build options graphically: `make menuconfig`

Build the source code: `make`


### Obtain FPGA Bitstream

**FPGA support is available only in the commercial version**

The FPGA project can use the demo provided by Sipeed, located in [TangMega-138KPro-example](https://github.com/sipeed/TangMega-138KPro-example) under ae350_customized_demo. The bitstream is pre-compiled and does not need to be regenerated.

### Download Bitstream

Connect FPGA and download the bitstream using HighCloud Source software.

### Program Flash

Use the programmer.exe under the flash directory in RDS for programming. Set as follows:
- External Flash Mode 5AT
- exFlash C Bin Erase, Program 5AT
- Start address: 0x600000

If there is no output after programming, it may be necessary to redownload the bitstream.

### Connect Serial Port

The default UART2 is bound to:
```
IO_LOC "UART2_TXD" U16;     //1
IO_LOC "UART2_RXD" V16;     //2
```

### System Login

Login to the system via the serial port.

## Expected Result

The system boots up successfully, allowing login through the onboard serial port.

## Actual Result

Image compiled and flashed successfully, but no output on the serial port.

### Boot Information

N/A

## Test Criteria

Test Pass: Actual result matches the expected result.

Test Fail: Actual result does not match the expected result.

## Test Conclusion

CFH

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
