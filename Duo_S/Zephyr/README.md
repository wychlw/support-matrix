
# Zephyr MilkV DuoS Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/zephyrproject-rtos/zephyr/tree/main
- Reference Documents:
    - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
    - https://github.com/milkv-duo/duo-buildroot-sdk

### Hardware Information

- MilkV DuoS
- 1 x USB to UART Debugger
- SD Card

## Installation Steps

### Create and Compile BuildRoot

Follow the official guide to obtain the source code:
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git --depth=1
```

Modify `build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c` to remove pre-mapped pins:
```diff
diff --git a/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c b/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c
index 6552f8da3..cbcb91cb6 100644
--- a/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c
+++ b/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c
@@ -6,52 +6,10 @@ static void set_rtc_register_for_power(void)
 
 int cvi_board_init(void)
 {
-       // Camera
-       PINMUX_CONFIG(CAM_MCLK0, CAM_MCLK0);
-       PINMUX_CONFIG(IIC3_SCL, IIC3_SCL);
-       PINMUX_CONFIG(IIC3_SDA, IIC3_SDA);
-       PINMUX_CONFIG(PAD_MIPIRX4P, XGPIOC_3);
-       PINMUX_CONFIG(PAD_MIPIRX4N, XGPIOC_2);
-
-       // I2C2 for Camera2
-       PINMUX_CONFIG(IIC2_SDA, IIC2_SDA);
-       PINMUX_CONFIG(IIC2_SCL, IIC2_SCL);
-
-       // LED
-       PINMUX_CONFIG(IIC0_SDA, XGPIOA_29);
-
-       // I2C4 for TP
-       PINMUX_CONFIG(VIVO_D1, IIC4_SCL);
-       PINMUX_CONFIG(VIVO_D0, IIC4_SDA);
-
-       // SPI3
-       PINMUX_CONFIG(VIVO_D8, SPI3_SDO);
-       PINMUX_CONFIG(VIVO_D7, SPI3_SDI);
-       PINMUX_CONFIG(VIVO_D6, SPI3_SCK);
-       PINMUX_CONFIG(VIVO_D5, SPI3_CS_X);
-
-       // USB
-       PINMUX_CONFIG(USB_VBUS_EN, XGPIOB_5);
-
-       // WIFI/BT
-       PINMUX_CONFIG(CLK32K, PWR_GPIO_10);
-       PINMUX_CONFIG(UART2_RX, UART4_RX);
-       PINMUX_CONFIG(UART2_TX, UART4_TX);
-       PINMUX_CONFIG(UART2_CTS, UART4_CTS);
-       PINMUX_CONFIG(UART2_RTS, UART4_RTS);
-
-       // GPIOs
-       PINMUX_CONFIG(JTAG_CPU_TCK, XGPIOA_18);
-       PINMUX_CONFIG(JTAG_CPU_TMS, XGPIOA_19);
-       PINMUX_CONFIG(JTAG_CPU_TRST, XGPIOA_20);
-       PINMUX_CONFIG(IIC0_SCL, XGPIOA_28);
-
-       // EPHY LEDs
-       PINMUX_CONFIG(PWR_WAKEUP0, EPHY_LNK_LED);
-       PINMUX_CONFIG(PWR_BUTTON1, EPHY_SPD_LED);
+       PINMUX_CONFIG(VIVO_D10, UART2_TX);
+       PINMUX_CONFIG(VIVO_D9, UART2_RX);
 
        set_rtc_register_for_power();
 
        return 0;
 }
-

```

Compile using docker:
```bash
cd duo-buildroot-sdk
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo256m"
```

Burn the source code to the SD card:
```bash 
sudo dd if=out/milkv-duo-yyyymmdd-hhmm.img of=/dev/your/device bs=1M status=progress
```

### Install Zephyr

Create a virtual environment:
```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west
```

Note: Not yet merged into the mainline, need to use a specific repository when fetching Zephyr:
```bash
west init ~/zephyrproject -m https://github.com/plctlab/rvspoc-p2307-zephyr.git
cd ~/zephyrproject
west update
```

Configure the environment:
```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
```

### Compile Code

Compile the code using west:
```bash
west build -p always -b milkv_duos samples/hello_world
```

### Merge fip.bin

Mount the SD card with the flashed BuildRoot image, merge fip:
```bash
sudo ./fsbl/plat/cv181x/fiptool.py -v genfip \
        './fsbl/build/cv1813h_milkv_duos_sd/fip.bin' \
        --MONITOR_RUNADDR="0x0000000080000000" \
        --BLCP_2ND_RUNADDR="0x000000009fe00000" \
        --CHIP_CONF='./fsbl/build/cv1813h_milkv_duos_sd/chip_conf.bin' \
        --NOR_INFO='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF' \
        --NAND_INFO='00000000'\
        --BL2='./fsbl/build/cv1813h_milkv_duos_sd/bl2.bin' \
        --BLCP_IMG_RUNADDR=0x05200200 \
        --BLCP_PARAM_LOADADDR=0 \
        --BLCP=./fsbl/test/empty.bin \
        --DDR_PARAM='./fsbl/test/cv181x/ddr_param.bin' \
        --BLCP_2ND='~/zephyrproject/zephyr/build/zephyr/zephyr.bin' \
        --MONITOR='./opensbi/build/platform/generic/firmware/fw_dynamic.bin' \
        --LOADER_2ND='./u-boot-2021.10/build/cv1813h_milkv_duos_sd/u-boot-raw.bin' \
        --compress='lzma'

```

Copy to the SD card:
```bash
sudo cp ./fsbl/build/cv1813h_milkv_duos_sd/fip.bin /path/to/sdcard
```

### Connect to Serial Port

The microkernel where Zephyr is located uses UART2 (GP11: TX, GP13: RX, GP9: GND)

## Expected Results

The system should start up properly, and information should be viewable through the onboard serial port.

## Actual Results

The system started up correctly, and information was readable through the onboard serial port.

### Startup Information

Screen recording (from compilation to startup):
[![asciicast](https://asciinema.org/a/oxAM8WHrZvcN04yDOWSlSDsKf.svg)](https://asciinema.org/a/oxAM8WHrZvcN04yDOWSlSDsKf)

```log
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000

```

## Test Criteria

Successful Test: Actual results match expected results.

Failed Test: Actual results do not match expected results.

## Test Conclusion

Test Successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
