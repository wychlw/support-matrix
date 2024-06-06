# RT-Thread Tang Mega 138K Pro Test Report

## Test Environment

### Operating System Information

- Build System: Linux
- RT-Thread
- Source Code Download Link: [RiscV_AE350_SOC_V1.1.zip](https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip)
    - Bitstream: [TangMega-138KPro-example](https://github.com/sipeed/TangMega-138KPro-example)
- Reference Installation Document: [Gowin RiscV AE350 SOC Software Programming User Manual](https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf)
- Reference Design Document: [Gowin RiscV AE350 SOC Hardware Design User Manual](https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf)

### Hardware Information

- Tang Mega 138K Pro Dock
- Type A to C cable x1
- UART serial cable x1
- Power cord

## Installation Steps

**The following example is based on building in a Linux system. For Windows, please install AE350 SOC RDS and perform the same operations in the provided cygwin environment unless specified otherwise.**

*If IDE functionality is not needed, RDS License is not necessary for building on Windows.*

### Copy and Patch Code

The RT-Thread code is located in the compressed source code package, under the path ref_design/MCU_RefDesign/ae350_rtthread_nano. Extract it to your working directory.

For Linux: patch Debug/makefile:
Replace the following content:
```diff
diff --git a/Debug/makefile b/Debug/makefile
index eb97e6d..232a162 100644
--- a/Debug/makefile
+++ b/Debug/makefile
@@ -119,7 +119,7 @@ $(SECONDARY_OUTPUT_PATH)/.PHONY.size: $(LINKER_OUTPUTS)
 
 $(SECONDARY_OUTPUT_PATH)/ae350-ddr.ld: $(SAG_SRCS)
 	@echo 'Invoking: LdSaG Tool'
-	nds_ldsag --version=v5 -t "$(ANDESIGHT_ROOT)/utils/nds32_template_v5.txt" "$(SAG_FILE)" -o $(LDSAG_OUT)
+	cp ../src/bsp/sag/ae350-ddr.ld $(LDSAG_OUT)
 	@echo 'Finished building: $@'
 	@echo ' '
 

```
Note that line breaks should be CRLF

Replace the working directory:
```bash
find -name "*.mk" -exec sed -i "s|/cygdrive/E/RDS5/workspace/ae350_rtthread_nano|$(pwd)|g" {} \;
```

### Compile Code

#### Linux
Unpack the cross-compilation toolchain. It is recommended to use nds32le-elf-mculib-v5. Hereafter, it will be referred to as `$(nds32_path)`.

Compile target files:
```bash
cd Debug
make CROSS_COMPILE=$(nds32_path)/bin/riscv32-elf-
```

#### Windows
Open the cygwin environment provided with RDS:
Run Cygwin.bat located in the RDS installation directory under cygwin folder.

Navigate to the source code folder (drive is in `/cygdrive/$(drive_letter)`).

Compile target files. Replace RDS_ROOT with your RDS installation path:
```bash
cd Debug
make ANDESIGHT_ROOT=<RDS_ROOT> CROSS_COMPILE=<RDS_ROOT>/toolchains/nds32le-elf-mculib-v5/bin/riscv32-elf-
```

### Obtain FPGA Bitstream

**Exclusive to the commercial version of Tang Mega 138K.**

The FPGA project can use the demo provided by Sipeed, located in ae350_customized_demo within [TangMega-138KPro-example](https://github.com/sipeed/TangMega-138KPro-example). The bitstream is already compiled and does not require regeneration.

### Download Bitstream

Connect the FPGA and download the bitstream using software from the cloud source.

### Program Flash

Use the programmer.exe in the flash directory of the RDS for programming. Set as follows:
- External Flash Mode 5AT
- exFlash C Bin Erase, Program 5AT
- Start address: 0x600000

After programming, if there is no output, download the bitstream again.

### Connect Serial Port

The default UART2 is bound to:
```
IO_LOC "UART2_TXD" U16;     //1
IO_LOC "UART2_RXD" V16;     //2
```

### Check Output

Check the RT-Thread output via the serial port.

## Expected Results

The system should start normally, and the RT-Thread output should be viewable through the onboard serial port.

## Actual Results

The system started normally, and the RT-Thread output was visible through the onboard serial port.

### Startup Information

```log

It's a RT-Thread Nano version demo.

Initializes RT hw board...

 \ | /

- RT -     Thread Operating System

 / | \     3.1.5 build Apr 16 2024

 2006 - 2020 Copyright by rt-thread team

RT demo...

```

## Test Criteria

Success: Actual results match the expected results.

Failure: Actual results do not match the expected results.

## Test Conclusion

Successful test.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
