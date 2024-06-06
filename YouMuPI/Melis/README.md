
# Melis Yuzuki PI-Lizard Test Report

## Test Environment

### Operating System Information

- SDK Links:
    - International - Google Driver: [GoogleDriver](https://drive.google.com/drive/folders/1_HAZRddR69hRMZAVrxFrPZXFFQiV3vE0?usp=share_link)
    - Domestic - Baidu Cloud: [BaiduYun](https://pan.baidu.com/s/115gVK-8Pt-vJi8jn2AWMYw?pwd=7n4q) Extraction Code: 7n4q
- Reference Documents:
    - [Board Introduction](https://dongshanpi.com/YuzukiHD-Lizard/01-BoardIntroduction/)
    - [Development Guide](https://tina.100ask.net/SdkModule/Linux_E907_DevelopmentGuide-01/)

### Hardware Information

- Yuzuki PI-Lizard Development Board

## Installation Steps

### Extract SDK

After downloading the SDK, merge the compressed package and extract it:
```bash
cat tina-v853-open.tar.gz.* > tina-v853-open.tar.gz
tar -xzvf tina-v853-open.tar.gz
```

Since the default SDK does not support this development board, we need to separately copy and add the configuration for this development board to the tina-v853-open SDK. First, clone this development board patch repository, then overwrite it separately:
```bash
git clone  https://github.com/DongshanPI/Yzukilizard-v851s-TinaSDK
cp -rfvd Yzukilizard-v851s-TinaSDK/* tina-v853-open/
```

### Configure System and Compile

After downloading the SDK, perform configuration environment work:
```bash
cd tina-v853-open
source build/envsetup.sh
lunch
```
Select the corresponding solution.

**If you encounter issues, try using bash instead of other shell environments like zsh.**

Configure E906 to start RTOS:
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

Configure kernel:
```bash
ckernel
m kernel_menuconfig
```
Include `Mailbox Hardware Support` under `Device Drivers`;
Include `sunxi Mailbox` and `sunxi rv32 standby driver` under `Device Drivers → Mailbox Hardware Support`:
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

> If encountering a linker report of `yyloc` being redefined:
> This is due to GCC version being higher than 10, change `YYLTYPE yyloc` under `scripts/dtc/dtc-parser.tab.c` to `extern YYLTYPE yyloc`.

Configure RTOS:
```bash
mmelis menuconfig
```

### Build and Package

```bash
make -j$(nproc)
p
```

### System Login

Connect UART3 to view serial output.

## Expected Results

The system starts up normally with output visible through the serial port.

## Actual Results

The system starts up successfully with output visible through the serial port.

### Startup Information

Screen recording:

```log
```

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
