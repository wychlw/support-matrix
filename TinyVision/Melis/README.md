# Melis TinyVision Test Report

## Test Environment

### Operating System Information

- SDK Link:
    - Baidu Cloud: Link: https://pan.baidu.com/s/1oIqGjCCtvUe0_k_kgXkusw?pwd=0kdr Extraction Code: 0kdr
- Reference Documents:
    - https://dongshanpi.com/YuzukiHD-Lizard/01-BoardIntroduction/
    - https://tina.100ask.net/SdkModule/Linux_E907_DevelopmentGuide-01/

### Hardware Information

- TinyVision Development Board

## Installation Steps

### Unpacking SDK

After downloading the SDK, merge the compressed package and unzip it:
```bash
tar -xzvf tina-v851se.tar.gz
```

Since the default SDK does not support this development board, we need to separately copy and add the configuration for this development board into the tina-v853-open SDK. First, clone the repository for this development board patch, then overwrite it separately:
```bash
git clone  https://github.com/DongshanPI/TinyVision-v851se_TinaSDK
cp -rfvd  TinyVision-v851se_TinaSDK/* tina-v851/
```

### Configuring the System and Compiling

After downloading the SDK, perform configuration environment tasks:
```bash
cd tina-v853-open
source build/envsetup.sh
lunch
```
Choose the corresponding solution.

**If any issues arise, try switching to bash instead of other shell environments like zsh**

Configure the E906 to start RTOS:
```bash
cconfigs
cd ../default/
vim boot_package_nor.cfg
```
```diff
--- boot_package_nor.cfg.bak    2024-05-09 15:59:28.706860360 +0800
+++ boot_package_nor.cfg        2024-05-09 16:40:10.476852456 +0800
@@ -4,6 +4,7 @@
 item=optee,                  optee.fex
 item=u-boot,                        u-boot-spinor.fex
 item=dtb,                    sunxi.fex
+item=melis-elf,              riscv.fex
 ;item=logo,                   bootlogo.bmp.lzma
 ;item=shutdowncharge,         bempty.bmp.lzma
 ;item=androidcharge,          battery_charge.bmp.lzma
```
```bash
vim boot_package.cfg
```
```diff
--- boot_package.cfg.bak        2024-05-09 16:39:35.356852125 +0800
+++ boot_package.cfg    2024-05-09 16:40:01.263519036 +0800
@@ -4,6 +4,7 @@
 item=optee,                  optee.fex
 item=u-boot,                 u-boot.fex
 item=dtb,                    sunxi.fex
+item=melis-elf,              riscv.fex
 ;item=logo,                   bootlogo.bmp.lzma
 ;item=shutdowncharge,         bempty.bmp.lzma
 ;item=androidcharge,          battery_charge.bmp.lzma
```

Configure the kernel:
```bash
ckernel
m kernel_menuconfig
```
Include `Device Drivers` under `Mailbox Hardware Support`;
Include `Device Drivers → Mailbox Hardware Support` with `sunxi Mailbox` and `sunxi rv32 standby driver`:
```diff
--- .config.old 2024-05-09 16:42:29.690187100 +0800
+++ .config     2024-05-09 16:45:57.840189075 +0800
@@ -3174,7 +3174,12 @@
 # CONFIG_SH_TIMER_MTU2 is not set
 # CONFIG_SH_TIMER_TMU is not set
 # CONFIG_EM_TIMER_STI is not set
-# CONFIG_MAILBOX is not set
+CONFIG_MAILBOX=y
+CONFIG_SUNXI_MBOX=y
+CONFIG_SUNXI_RV32_STANBY=y
+# CONFIG_PLATFORM_MHU is not set
+# CONFIG_ALTERA_MBOX is not set
+# CONFIG_MAILBOX_TEST is not set
 CONFIG_IOMMU_API=y
 CONFIG_IOMMU_SUPPORT=y
 
@@ -3192,6 +3197,7 @@
 # Remoteproc drivers
 #
 # CONFIG_STE_MODEM_RPROC is not set
+# CONFIG_SUNXI_RPROC is not set
 
 #
 # Rpmsg drivers
@@ -3304,6 +3310,7 @@
 # Firmware Drivers
 #
 CONFIG_ARM_PSCI_FW=y
+# CONFIG_ARM_SCPI_PROTOCOL is not set
 # CONFIG_FIRMWARE_MEMMAP is not set
 # CONFIG_FW_CFG_SYSFS is not set
 CONFIG_HAVE_ARM_SMCCC=y
```
```bash
mkernel -j
```

> If encountering a linker report of `yyloc` redefinition:
> This is due to GCC version higher than 10, modify `YYLTYPE yyloc` in `scripts/dtc/dtc-parser.tab.c` to `extern YYLTYPE yyloc`

Configure RTOS:
```bash
mmelis menuconfig
```

### Building and Packaging

```bash
make -j$(nproc)
p
```

### Logging into the System

Connect UART3 to view serial output.

## Expected Results

The system should start normally, and output should be viewable through the serial port.

## Actual Results

The system started normally, and the output was successfully viewed through the serial port.

### Boot Information

Screen recording:

```log
```

## Test Criteria

Successful Test: Actual results match the expected results.

Failed Test: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
