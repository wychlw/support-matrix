# FreeRTOS Longan Nano Test Report

## Test Environment

### Operating System Information

- Source Code Link: [https://github.com/Nuclei-Software/nuclei-sdk](https://github.com/Nuclei-Software/nuclei-sdk)
- Reference Documentation: [https://doc.nucleisys.com/nuclei_sdk/design/board/gd32vf103c_longan_nano.html](https://doc.nucleisys.com/nuclei_sdk/design/board/gd32vf103c_longan_nano.html)
- Download Links:
    - SDK: [https://github.com/Nuclei-Software/nuclei-sdk](https://github.com/Nuclei-Software/nuclei-sdk)
    - Toolchain: [https://www.nucleisys.com/download.php](https://www.nucleisys.com/download.php)
        - [https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2](https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2)
    - OpenOCD: [https://www.nucleisys.com/download.php](https://www.nucleisys.com/download.php)
        - [https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz](https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz)

### Hardware Information

- Longan Nano
- One USB to UART Debugger
- **JTAG Debugger**
- One type-C cable

## Installation Steps

### Environment Configuration

Download the toolchain and OpenOCD, unzip them, and set the toolchain directory:
```bash
wget https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
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

### Code Compilation

Compile FreeRTOS:
```bash
cd application/freertos/demo/
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano clean
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano all
```

### Flashing Image

```bash
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano upload
```

### System Startup

Connect to the development board via the serial port.

## Expected Results

The system should start up properly, and information should be viewable through the onboard serial port.

## Actual Results

The system started up correctly, and information was viewable through the onboard serial port.

### Startup Information

Screen recording (from compilation to startup):

```log
```

## Test Judgment Criteria

Test Success: Actual results match the expected results.

Test Failure: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
