# FreeRTOS Tang Mega 138K Pro Test Report

## Test Environment

### Operating System Information

- Build System: Linux
- FreeRTOS
- Source Code Download Link: [RiscV_AE350_SOC_V1.1.zip](https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip)
    - Bitstream: [TangMega-138KPro-example](https://github.com/sipeed/TangMega-138KPro-example)
- Installation Reference Document: [MUG1029-1.1_Gowin_RiscV_AE350_SOC Software Programming User Manual](https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf)
- Design Reference Document: [MUG1031-1.1_Gowin_RiscV_AE350_SOC Hardware Design User Manual](https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf)

### Hardware Information

- Tang Mega 138K Pro Dock
- Type A to C cable x1
- UART serial cable x1
- Power cable

## Installation Steps

**The following is an example of building under the Linux system. For Windows, please install AE350 SOC RDS and perform the same operations in the included Cygwin environment.**

*If IDE functionality is not required, RDS License is not needed for building under Windows.*

### Copy and Patch Code

The FreeRTOS code is located in the compressed source code package under the path ref_design/MCU_RefDesign/ae350_freertos. Extract it to your workspace.

For Linux: patch Debug/makefile:
Replace the following content:
```diff
diff --git a/Debug/makefile b/Debug/makefile
index eb97e6d..232a162 100644
--- a/Debug/makefile
+++ b/Debug/makefile
@@ -117,7 +117,7 @@ $(SECONDARY_OUTPUT_PATH)/.PHONY.size: $(LINKER_OUTPUTS)
 
 $(SECONDARY_OUTPUT_PATH)/ae350-ddr.ld: $(SAG_SRCS)
 	@echo 'Invoking: LdSaG Tool'
-	nds_ldsag --version=v5 -t "$(ANDESIGHT_ROOT)/utils/nds32_template_v5.txt" "$(SAG_FILE)" -o $(LDSAG_OUT)
+	cp ../src/bsp/sag/ae350-ddr.ld $(LDSAG_OUT)
 	@echo 'Finished building: $@'
 	@echo ' '
 

```
Make sure line breaks are CRLF.

Replace working directory:
```bash
find -name "*.mk" -exec sed -i "s|/cygdrive/E/RDS5/workspace/ae350_freertos|$(pwd)|g" {} \;
```

### Compile Code

#### Linux

Extract the cross-compiler toolchain, it is recommended to use nds32le-elf-mculib-v5. Refer to it as `$(nds32_path)`.

Compile target files:
```bash
cd Debug
make CROSS_COMPILE=$(nds32_path)/bin/riscv32-elf-
```

#### Windows

Open the Cygwin environment provided by RDS:
Run Cygwin.bat found in the RDS installation directory.

Navigate to the source code folder (on drive `/cygdrive/$(drive_letter)`).

Compile target files, replace RDS_ROOT with your RDS installation path:
```bash
cd Debug
make ANDESIGHT_ROOT=<RDS_ROOT> CROSS_COMPILE=<RDS_ROOT>/toolchains/nds32le-elf-mculib-v5/bin/riscv32-elf-
```

### Obtain FPGA Bitstream

**FPGA project support is only provided in the commercial version of Tang Mega 138K.**

The FPGA project can be obtained from Sipeed's official demo in [TangMega-138KPro-example](https://github.com/sipeed/TangMega-138KPro-example) under ae350_customized_demo. The bitstream is already compiled and does not need to be regenerated.

### Download Bitstream

Connect the FPGA and download the bitstream using HighCloud Source software.

### Program Flash

Use the programmer.exe in the flash directory under RDS for programming. Set as follows:
- External Flash Mode 5AT
- exFlash C Bin Erase, Program 5AT
- Start address: 0x600000

![image](image.png)

If there is no output after programming, the bitstream may need to be downloaded again.

### Connect Serial Port

The default UART2 is bound to:
```
IO_LOC "UART2_TXD" U16;     //1
IO_LOC "UART2_RXD" V16;     //2
```

### View Output

View FreeRTOS output via the serial port.

## Expected Results

The system boots up successfully, and FreeRTOS output can be viewed via the onboard serial port.

## Actual Results

The system boots up successfully, and FreeRTOS output can be viewed via the onboard serial port.

### Boot Information

```log

****************************************************************************

Name:     FreeRTOS-AE350_SOC

Edition:  V10.3.1

Compiled: Apr 16 2024, 16:25:50

Author:   GowinSemiconductor

****************************************************************************

****************************************************************************

                     ◆

           ◆◆◆◆◆◆◆◆◆◆◆            ◆◆◆◆◆◆◆

               ◆◆◆◆◆◆◆

               ◆          ◆

               ◆◆◆◆◆◆◆            ◆◆◆◆◆◆◆◆◆◆◆

                                                   ◆

           ◆◆◆◆◆◆◆◆◆◆◆                ◆

           ◆                  ◆              ◆      ◆

           ◆    ◆◆◆◆◆    ◆            ◆          ◆

           ◆    ◆      ◆    ◆          ◆◆◆◆◆◆◆◆◆

           ◆    ◆◆◆◆◆  ◆◆                          ◆

****************************************************************************

1.task1 

0.task0 

0.task0 

0.task0 

0.task0 

```

## Test Criteria

Successful Test: Actual outcome matches the expected outcome.

Failed Test: Actual outcome does not match the expected outcome.

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
