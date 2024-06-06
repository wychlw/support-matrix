# Zephyr MilkV Duo256M Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/zephyrproject-rtos/zephyr/tree/main
- Reference Documents:
    - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
    - https://github.com/milkv-duo/duo-buildroot-sdk

### Hardware Information

- MilkV Duo256M
- 1 USB to UART Debugger
- SD Card

## Installation Steps

### Create and Compile BuildRoot

Follow the official tutorial to get the source code:
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git --depth=1
```

Modify `build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c` to remove pre-mapped pins:
```diff
diff --git a/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c b/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c
index c9c722236..c388ec0ee 100644
--- a/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c
+++ b/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c
@@ -1,46 +1,14 @@
 int cvi_board_init(void)
 {
-       // Camera
-       PINMUX_CONFIG(PAD_MIPI_TXM1, IIC2_SDA);    // GP10
-       PINMUX_CONFIG(PAD_MIPI_TXP1, IIC2_SCL);    // GP11
-       PINMUX_CONFIG(PAD_MIPI_TXP0, CAM_MCLK0);   // Sensor MCLK
-       PINMUX_CONFIG(PAD_MIPI_TXP2, XGPIOC_17);   // Sensor RESET
 
        // UART1
        PINMUX_CONFIG(IIC0_SCL, UART1_TX);         // GP0
        PINMUX_CONFIG(IIC0_SDA, UART1_RX);         // GP1
 
-       // PWM
-       PINMUX_CONFIG(JTAG_CPU_TMS, PWM_7);        // GP2
-       PINMUX_CONFIG(JTAG_CPU_TCK, PWM_6);        // GP3
 
-       // I2C1
-       PINMUX_CONFIG(SD1_D2, IIC1_SCL);           // GP4
-       PINMUX_CONFIG(SD1_D1, IIC1_SDA);           // GP5
 
-       // SPI2
-       PINMUX_CONFIG(SD1_CLK, SPI2_SCK);          // GP6
-       PINMUX_CONFIG(SD1_CMD, SPI2_SDO);          // GP7
-       PINMUX_CONFIG(SD1_D0, SPI2_SDI);           // GP8
-       PINMUX_CONFIG(SD1_D3, SPI2_CS_X);          // GP9
 
-       // All default GPIOs
-       PINMUX_CONFIG(SD0_PWR_EN, XGPIOA_14);      // GP14
-       PINMUX_CONFIG(SPK_EN, XGPIOA_15);          // GP15
-       PINMUX_CONFIG(EMMC_CMD, XGPIOA_23);        // GP16
-       PINMUX_CONFIG(EMMC_DAT1, XGPIOA_24);       // GP17
-       PINMUX_CONFIG(EMMC_CLK, XGPIOA_22);        // GP18
-       PINMUX_CONFIG(EMMC_DAT0, XGPIOA_25);       // GP19
-       PINMUX_CONFIG(EMMC_DAT3, XGPIOA_27);       // GP20
-       PINMUX_CONFIG(EMMC_DAT2, XGPIOA_26);       // GP21
-       PINMUX_CONFIG(PWR_SEQ2, PWR_GPIO_4);       // GP22
 
-       // LED
-       PINMUX_CONFIG(PWR_GPIO2, PWR_GPIO_2);      // GP25
-
-       // ADC pins set to GPIO
-       PINMUX_CONFIG(ADC1, XGPIOB_3);             // GP26 (ADC1)
-       PINMUX_CONFIG(USB_VBUS_DET, XGPIOB_6);     // GP27 (ADC2)
 
        return 0;
-}
\ No newline at end of file
+}

```

Compile using docker:
```bash
cd duo-buildroot-sdk
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo256m"
```

Then flash the source code to the SD card:
```bash 
sudo dd if=out/milkv-duo-yyyymmdd-hhmm.img of=/dev/your/device bs=1M status=progress
```

### Install Zephyr

Create a virtual environment:
```bash
west init ~/zephyrproject -m https://github.com/plctlab/rvspoc-p2307-zephyr.git
cd ~/zephyrproject
west update
```

```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
```

```bash
west build -p always -b milkv_duo256m samples/hello_world
```

```bash
sudo ./fsbl/plat/cv181x/fiptool.py -v genfip \
 './fsbl/build/cv1812cp_milkv_duo256m_sd/fip.bin' \
  --BLCP_2ND_RUNADDR="0x000000008fe00000" \
  --MONITOR_RUNADDR="0x0000000080000000" \
  --CHIP_CONF='./fsbl/build/cv1812cp_milkv_duo256m_sd/chip_conf.bin' \
  --NOR_INFO='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF' \
  --NAND_INFO='00000000'\
  --BL2='./fsbl/build/cv1812cp_milkv_duo256m_sd/bl2.bin' \
  --BLCP_IMG_RUNADDR=0x05200200 \
  --BLCP_PARAM_LOADADDR=0 \
  --BLCP='./fsbl/test/empty.bin' \
  --DDR_PARAM='./fsbl/test/cv181x/ddr_param.bin' \
  --BLCP_2ND='~/zephyrproject/zephyr/build/zephyr/zephyr.bin' \
  --MONITOR='./opensbi/build/platform/generic/firmware/fw_dynamic.bin' \
  --LOADER_2ND='./u-boot-2021.10/build/cv1812cp_milkv_duo256m_sd/u-boot-raw.bin' \
  --compress='lzma'
```

# Zephyr MilkV Duo256M Test Report

## Test Environment

### Operating System Information

- Source Code Link: [Zephyr Github Repository](https://github.com/zephyrproject-rtos/zephyr/tree/main)
- Reference Documents:
    - [Getting Started with Zephyr](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)
    - [MilkV Duo Buildroot SDK](https://github.com/milkv-duo/duo-buildroot-sdk)

### Hardware Information

- MilkV Duo256M
- 1 x USB to UART Debugger
- SD Card

## Installation Steps

### Creating and Compiling BuildRoot

Following the official tutorial, fetch the source code:
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git --depth=1
```

Modify `build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c` to remove pre-mapped pins:
```diff
diff --git a/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c b/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c
index c9c722236..c388ec0ee 100644
--- a/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c
+++ b/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c
@@ -1,46 +1,14 @@
 int cvi_board_init(void)
 {
-       // Camera
-       PINMUX_CONFIG(PAD_MIPI_TXM1, IIC2_SDA);    // GP10
-       PINMUX_CONFIG(PAD_MIPI_TXP1, IIC2_SCL);    // GP11
-       PINMUX_CONFIG(PAD_MIPI_TXP0, CAM_MCLK0);   // Sensor MCLK
-       PINMUX_CONFIG(PAD_MIPI_TXP2, XGPIOC_17);   // Sensor RESET
 
        // UART1
        PINMUX_CONFIG(IIC0_SCL, UART1_TX);         // GP0
        PINMUX_CONFIG(IIC0_SDA, UART1_RX);         // GP1
 
-       // PWM
-       PINMUX_CONFIG(JTAG_CPU_TMS, PWM_7);        // GP2
-       PINMUX_CONFIG(JTAG_CPU_TCK, PWM_6);        // GP3
 
-       // I2C1
-       PINMUX_CONFIG(SD1_D2, IIC1_SCL);           // GP4
-       PINMUX_CONFIG(SD1_D1, IIC1_SDA);           // GP5
 
-       // SPI2
-       PINMUX_CONFIG(SD1_CLK, SPI2_SCK);          // GP6
-       PINMUX_CONFIG(SD1_CMD, SPI2_SDO);          // GP7
-       PINMUX_CONFIG(SD1_D0, SPI2_SDI);           // GP8
-       PINMUX_CONFIG(SD1_D3, SPI2_CS_X);          // GP9
 
-       // All default GPIOs
-       PINMUX_CONFIG(SD0_PWR_EN, XGPIOA_14);      // GP14
-       PINMUX_CONFIG(SPK_EN, XGPIOA_15);          // GP15
-       PINMUX_CONFIG(EMMC_CMD, XGPIOA_23);        // GP16
-       PINMUX_CONFIG(EMMC_DAT1, XGPIOA_24);       // GP17
-       PINMUX_CONFIG(EMMC_CLK, XGPIOA_22);        // GP18
-       PINMUX_CONFIG(EMMC_DAT0, XGPIOA_25);       // GP19
-       PINMUX_CONFIG(EMMC_DAT3, XGPIOA_27);       // GP20
-       PINMUX_CONFIG(EMMC_DAT2, XGPIOA_26);       // GP21
-       PINMUX_CONFIG(PWR_SEQ2, PWR_GPIO_4);       // GP22
 
-       // LED
-       PINMUX_CONFIG(PWR_GPIO2, PWR_GPIO_2);      // GP25
-
-       // ADC pins set to GPIO
-       PINMUX_CONFIG(ADC1, XGPIOB_3);             // GP26 (ADC1)
-       PINMUX_CONFIG(USB_VBUS_DET, XGPIOB_6);     // GP27 (ADC2)
 
        return 0;
-}
\ No newline at end of file
+}

```

Compile using Docker:
```bash
cd duo-buildroot-sdk
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo256m"
```

Then flash the source code to the SD card:
```bash 
sudo dd if=out/milkv-duo-yyyymmdd-hhmm.img of=/dev/your/device bs=1M status=progress
```

### Installing Zephyr

Create a virtual environment:

```bash
west init ~/zephyrproject -m https://github.com/plctlab/rvspoc-p2307-zephyr.git
cd ~/zephyrproject
west update
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
west build -p always -b milkv_duo256m samples/hello_world
sudo ./fsbl/plat/cv181x/fiptool.py -v genfip \
 './fsbl/build/cv1812cp_milkv_duo256m_sd/fip.bin' \
  --BLCP_2ND_RUNADDR="0x000000008fe00000" \
  --MONITOR_RUNADDR="0x0000000080000000" \
  --CHIP_CONF='./fsbl/build/cv1812cp_milkv_duo256m_sd/chip_conf.bin' \
  --NOR_INFO='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF' \
  --NAND_INFO='00000000'\
  --BL2='./fsbl/build/cv1812cp_milkv_duo256m_sd/bl2.bin' \
  --BLCP_IMG_RUNADDR=0x05200200 \
  --BLCP_PARAM_LOADADDR=0 \
  --BLCP='./fsbl/test/empty.bin' \
  --DDR_PARAM='./fsbl/test/cv181x/ddr_param.bin' \
  --BLCP_2ND='~/zephyrproject/zephyr/build/zephyr/zephyr.bin' \
  --MONITOR='./opensbi/build/platform/generic/firmware/fw_dynamic.bin' \
  --LOADER_2ND='./u-boot-2021.10/build/cv1812cp_milkv_duo256m_sd/u-boot-raw.bin' \
  --compress='lzma'
```

```bash
sudo cp ./fsbl/build/cv1812cp_milkv_duo256m_sd/fip.bin /path/to/sdcard
```

```log
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
```

## Test Criteria

Successful test: Actual results match expected results.

Failed test: Actual results do not match expected results.

## Test Conclusion

Test successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
