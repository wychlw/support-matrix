
# FreeRTOS RV-STAR Test Report

## Test Environment

### Operating System Information

- Source Code Link: [Nuclei SDK on Github](https://github.com/Nuclei-Software/nuclei-sdk)
- Reference Documentation:
    - PlatformIO Core: [Installation Guide](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO for ch32v: [Installation Instructions](https://pio-ch32v.readthedocs.io/en/latest/installation.html)
- Download Links:
    - SDK: [Nuclei SDK on Github](https://github.com/Nuclei-Software/nuclei-sdk)
    - Toolchain: [Nuclei Toolchain Download](https://www.nucleisys.com/download.php)
        - [Toolchain for Linux 64-bit](https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2)
    - OpenOCD: [Nuclei OpenOCD Download](https://www.nucleisys.com/download.php)
        - [OpenOCD for Linux x64](https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz)

### Hardware Information

- RV-STAR Development Board (GD32VF103VBT6)

## Installation Steps

### Environment Setup

Download the toolchain and OpenOCD, then extract and set the toolchain directory:
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

### Compile Code

Compile FreeRTOS:
```bash
cd application/freertos/demo/
make SOC=gd32vf103 BOARD=gd32vf103v_rvstar clean
make SOC=gd32vf103 BOARD=gd32vf103v_rvstar all
```

### Flash Image

```bash
make SOC=gd32vf103 BOARD=gd32vf103v_rvstar upload
```

### Start System

Connect to the development board via serial port.

## Expected Results

The system should start up normally, and information should be viewable through the onboard serial port.

## Actual Results

The system started up normally, and information was viewable through the onboard serial port.

### Startup Information

Screen recording (from compilation to startup):

```log
```

## Test Criteria

Test Success: Actual results match the expected results.

Test Failure: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
