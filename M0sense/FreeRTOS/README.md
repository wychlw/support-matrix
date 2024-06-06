# FreeRTOS Demo M0sense Test Report

## Test Environment

### Operating System Information

- Build System: Arch Linux
- Source Code Link: https://gitee.com/Sipeed/M0sense_BL702_example
- Reference Installation Document: https://wiki.sipeed.com/hardware/zh/maixzero/sense/start.html
- Toolchain: https://gitee.com/bouffalolab/toolchain_gcc_sifive_linux

### Hardware Information

- Sipeed M0sense (BL702)
- One USB A to C or C to C cable

## Installation Steps

### Prepare Build Environment

```shell
sudo pacman -S gcc git base-devel
```

### Build FreeRTOS Demo

```shell
git clone https://gitee.com/Sipeed/M0sense_BL702_example.git
cd M0sense_BL702_example
git clone https://gitee.com/bouffalolab/bl_mcu_sdk
git clone https://gitee.com/bouffalolab/toolchain_gcc_sifive_linux
./build.sh patch
PATH=$PWD/toolchain_gcc_sifive_linux/bin:$PATH
gcc -I libs/uf2_format misc/utils/uf2_conv.c -o uf2_convert
./build.sh m0sense_apps/rtos_demos/single_button_control
```

After the build is complete, a UF2 format firmware will be generated in the `uf2_demos` directory.

```log
mx @ archlinux in ~/M0sense_BL702_example/uf2_demos |17:40:05  |main U:3 ?:2 ✗| 
$ ls
audio_recording.uf2  blink_baremetal.uf2  blink_rtos.uf2  hello_world.uf2  imu.uf2  lcd_flush.uf2  single_button_control.uf2
```

### Flash Image

Hold down the BOOT button on the development board and press the RESET button. It will appear as a USB mass storage device on the computer. Copy the `single_button_control.uf2` compiled in the previous step into it.

Once the copy is complete, the development board will automatically restart to load the new firmware.

#### If USB storage device does not appear

Please refer to [here](https://wiki.sipeed.com/hardware/zh/maixzero/sense/start.html#%E7%83%A7%E5%BD%95-bin-%E6%96%87%E4%BB%B6) for firmware burning.

1. Download the burning disk tool from Bouffalo's [official website](https://dev.bouffalolab.com/download).
2. Depending on the system, run `BLDevCube`, `BLDevCube-macos`, or `BLDevCube-ubuntu`.
3. Short the development board `3V` and `BOOT` pins, then connect the development board to the computer.
4. Open the `BLDevCube` software, select `BL702`, select `MCU` mode.
5. Click `Refresh`, select the unique serial port (if not unique, short `boot` pin and `3.3v` pin again to power on M0sense to enter download mode), set the baud rate to `2000000`, and click` Create & Download`.
6. Unplug and replug the USB to make the new firmware effective.
7. Now you can follow the above method, drag and drop the `.uf2` firmware directly to the development board for burning.

### Connect the Development Board

Connect the development board via USB. A serial port will appear on the computer.

Baud rate: 115200

Data bits: 8

## Expected Results

Successful build, pressing the development board's BOOT button will cause the LED on the development board to change color. The serial port will print LED color information.

## Actual Results

Successful build, pressing the development board's BOOT button will cause the LED on the development board to change color. The serial port will print LED color information.

[![asciicast](https://asciinema.org/a/MjevQgMAxbPcjP0Uj1RJdEdQl.svg)](https://asciinema.org/a/MjevQgMAxbPcjP0Uj1RJdEdQl)

### Boot Information

## Test Criteria

Test Successful: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
