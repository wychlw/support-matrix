# Buildroot Icicle Test Report

## Test Environment

### System Information

### Operating System Information

- System Version: Buildroot
- Source Link: [Buildroot Download Page](https://buildroot.org/download.html)
    - As of the time of writing, the latest stable/LTS version of Buildroot is: [buildroot-2024.02.2](https://buildroot.org/downloads/buildroot-2024.02.2.tar.gz)
- Reference Installation Document: [Buildroot VisionFive Board Installation Guide](https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/visionfive?ref_type=heads)
- Build System: Arch Linux x86_64

### Hardware Information

- Microchip Polarfire SoC FPGA Icicle Kit Development Board
- Original 12V 5A DC 5.5*2.1mm Power Adapter (Original cable comes with US plug, adapter/change to local plug may be needed in mainland China)
- Two micro-USB to USB-A cables (factory-supplied) for connecting USB-UART, updating FPGA/HSS, and flashing images to onboard eMMC
- (Optional) One SD card (not recommended to use microSD + adapter as it may not be recognized; also ensure the card is not write-protected)

## Image Building and Flashing

Since the Buildroot for PolarFire SoC FPGA Icicle Kit has been mainstreamed, obtaining the source code from Buildroot allows for the construction of a usable image.

### Setting Up the Build Environment

```shell
sudo pacman -S which sed make binutils diffutils gcc bash patch gzip bzip2 perl tar cpio unzip rsync file bc findutils wget
# 或者从 AUR 安装，需要 AUR Helper，如 yay, paru 等
# paru -S buildroot-meta
```

If you are not using Arch Linux, please refer to the [official documentation](https://buildroot.org/downloads/manual/manual.html#requirement) for installing the necessary dependencies (note that package names may vary).

### Building the Image

```shell
wget https://buildroot.org/downloads/buildroot-2024.02.2.tar.gz
tar xvf buildroot-2024.02.2.tar.gz
cd buildroot-2024.02.2/
make microchip_mpfs_icicle_defconfig
make -j$(nproc)
```

Note: Ensure your internet connection is active as dependencies will be downloaded during compilation.

After the build, an `sdcard.img` image will be generated in `output/images`.

### (Optional) Updating FPGA Design and Hart Software Services (HSS)

This step is not mandatory but can be attempted if issues arise.

Follow the steps outlined in [Ubuntu](../Ubuntu/README.md) for updating.

### Flashing the Image

Polarfire SoC FPGA Icicle Kit supports booting from onboard eMMC or SD card.

SD card is the default priority. If the SD card is absent or fails to boot, the system will boot from the onboard eMMC.

### Flashing the Image to eMMC

Connect the microUSB cable to the USB OTG port near the SD card slot labeled `J19`.

Connect the USB UART located on the side of the Ethernet port labeled `J11`.

The computer will recognize a CP2108 USB to UART, and if this is the only one on your computer, four serial ports will be recognized.

On Windows, four COM ports will appear, on Linux, /dev/ttyUSB{0,1,2,3} will appear.

`Interface 0` is the `HSS` output, `Interface 1` is for U-Boot and Linux console output.

In Linux, they respectively correspond to the first and second serial ports.

| Serial Port Function | Windows     | Linux        |
| -------------------- | ----------- | ------------ |
| HSS Console          | Interface 0 | /dev/ttyUSB0 |
| U-Boot & Linux Console | Interface 1 | /dev/ttyUSB1 |

To write the image to eMMC, connect to the `HSS` console, interrupt the boot process by pressing any key when prompted with `Press a key to enter CLI, ESC to skip`.

Enter:

```
mmc
usbdmsc
```

It will prompt `Waiting for USB Host to connect`.

A USB Mass Storage Device should appear on the computer side. You can now use tools like Win32DiskImager/Rufus/USBImager/dd to write the image directly to it.

After writing the image, press Ctrl+C on the HSS console to exit USB storage mode. This concludes the image flashing process.

### Flashing the Image to SD Card

Simply use Rufus/Win32DiskImager/dd or similar tools to write the image to the SD card.

```shell
sudo dd if=sdcard.img of=/dev/sdX bs=1M status=progress
```

### Logging In

Log into the system via serial console.

Default username: `root`

Default password: none, automatically logs in after entering the username

## Expected Outcome

The system boots up successfully, and login is possible through the onboard serial console.

## Actual Outcome

The system boots up successfully, and login is possible through the onboard serial console.

### Boot Information

```log
Welcome to Buildroot
mpfs_icicle login: root
# uname -a
Linux mpfs_icicle 6.1.74-linux4microchip+fpga-2024.02 #1 SMP Mon May 13 18:29:54 CST 2024 riscv64 GNU/Linux
# cat /etc/os-release
NAME=Buildroot
VERSION=2024.02.2
ID=buildroot
VERSION_ID=2024.02.2
PRETTY_NAME="Buildroot 2024.02.2"
# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

#
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/js18pAh0YMTp0g9bQD1tXsBgH.svg)](https://asciinema.org/a/js18pAh0YMTp0g9bQD1tXsBgH)

## Test Criteria

Test Success: Actual outcome matches the expected outcome.

Test Failure: Actual outcome does not match the expected outcome.

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
