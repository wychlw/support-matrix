
# RT-Thread Longan Nano Test Report

## Test Environment

### Operating System Information

- Source Code Link: [Nuclei-Software/nuclei-sdk](https://github.com/Nuclei-Software/nuclei-sdk)
- Reference Documentation: [GD32VF103C Longan Nano](https://doc.nucleisys.com/nuclei_sdk/design/board/gd32vf103c_longan_nano.html)
- Download Links:
    - SDK: [Nuclei-Software/nuclei-sdk](https://github.com/Nuclei-Software/nuclei-sdk)
    - Toolchain: [NucleiSys Downloads](https://www.nucleisys.com/download.php)
        - [Nuclei RISC-V Newlib prebuilt Linux 64](https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2)
    - OpenOCD: [NucleiSys Downloads](https://www.nucleisys.com/download.php)
        - [nuclei-openocd-2024.02.28-linux-x64](https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz)

### Hardware Information

- Longan Nano
- One USB to UART debugger
- **One JTAG debugger**
- One Type-C cable

## Installation Steps

### Configure Environment

Download the toolchain and OpenOCD, then unzip them. Set the toolchain directory:
```bash
wget https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
tar -xzf nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
wget https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz
tar -xzvf nuclei-openocd-2024.02.28-linux-x64.tgz
export NUCLEI_TOOL_ROOT=$(pwd)
```

Download the SDK:
```bash
git clone https://github.com/Nuclei-Software/nuclei-sdk.git
cd nuclei-sdk
cat << EOF > setup_config.sh
NUCLEI_TOOL_ROOT=$(echo $NUCLEI_TOOL_ROOT)
EOF
source setup.sh
```

### Compile Code

Compile FreeRTOS:
```bash
cd application/rtthread/demo
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano clean
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano all
```

### Flash Image

```bash
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano upload
```

### System Startup

Connect to the development board via serial port.

## Expected Results

The system boots up successfully, and information can be viewed through the onboard serial port.

## Actual Results

The system boots up successfully, and information can be viewed through the onboard serial port.

### Startup Information

Video recording (from compile to boot):
```log
```

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
