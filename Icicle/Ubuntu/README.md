# Ubuntu on Microchip Polarfire SoC FPGA Icicle Kit

## Test Environment

### Hardware Information

- Microchip Polarfire SoC FPGA Icicle Kit development board
- Original 12V 5A DC 5.5*2.1mm power adapter (the original cable comes with a US plug, an adapter/change to a universal plug is required for use in mainland China)
- Two micro-USB to USB-A cables (included in the package) for connecting USB-UART, updating FPGA/HSS, and burning images to onboard eMMC
- (Optional) One SD card (not recommended to use microSD + adapter, as it may not be recognized; also ensure the storage card is not write-protected)

### Operating System Information

- Ubuntu 24.04
    - Download link: https://cdimage.ubuntu.com/releases/24.04/release/
        - TUNA image source: https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/noble/release/ubuntu-24.04-preinstalled-server-riscv64+icicle.img.xz
    - Installation reference: https://wiki.ubuntu.com/RISC-V/PolarFire%20SoC%20FPGA%20Icicle%20Kit

### Other Information

- Icicle Kit Reference Design Release v2024.02
    - Download link: https://github.com/polarfire-soc/icicle-kit-reference-design/releases/tag/v2024.02
- FlashPro Express v2024.1 (bundled in Programming and Debug Tools)
    - Download link (login required): https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/programming-and-debug/lab

## (Optional, Recommended) Update FPGA Design and Hart Software Services (HSS)

### Installing FlashPro Express Tool

Visit the download link mentioned above and download according to your operating system.

> Note that there is a login wall, registration and login are required for download.
>
> After providing email and other information, registration is free.

This tool supports the following systems:

- Windows 10/11
- RHEL/CentOS 7.x, RHEL/CentOS 8.0-8.2
- OpenSUSE Leap 42.3 (SLES 12.3)
- Ubuntu 18.04 LTS, 20.04.3 LTS, and 22.04.1 LTS

The author uses Windows 11 Home x64. Although the installation program may indicate an unsupported system environment, it can be installed normally.

After downloading, run it directly and install following the default process. In the Linux environment, first `chmod +x` to grant execute permission before running. Root permission might be required.

### Update FPGA Design & HSS

Ubuntu relies on Icicle Kit Reference Design v2022.10 or newer versions from kernel 5.19 onwards.

Download the latest version from GitHub:

https://github.com/polarfire-soc/icicle-kit-reference-design/releases

Download the `MPFS_ICICLE_BASE_DESIGN_yyyy_mm.zip` file and extract it for later use.

Connect the development board to the computer using a microUSB cable.

There are two microUSB interfaces on the development board. When burning the FPGA, connect it to the `J33` interface, the microUSB interface near the power switch, as shown in the image below.

![Connectors](https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/reference-designs-fpga-and-development-kits/images/icicle-kit-user-guide/icicle-kit-connectors.png?raw=true)

Open FlashPro Express, click the top-left menu `Project -> New Job Project`

![](./images/image.png)

Select the previously extracted `MPFS_ICICLE_BASE_DESIGN`, plug in the 12V power, power up the development board, and then click OK:

![alt text](./images/image-1.png)

The FPGA should now be recognized. Ensure that `PROGRAM` is selected in the left-hand dropdown menu, then click `RUN` to start burning the FPGA.

![alt text](./images/image-2.png)

A success message will appear in green after burning:

![alt text](./images/image-3.png)

## Burning Image

The Polarfire SoC FPGA Icicle Kit supports booting from onboard eMMC or an SD card.

By default, the priority is on the SD card. If the SD card is not present or fails to boot, the onboard eMMC will be used.

### Burning Image to eMMC

Connect the microUSB cable to the USB OTG port labeled `J19`, located near the SD card slot.

Connect the USB UART to the port labeled `J11`, next to the Ethernet port.

A CP2108 USB to UART converter will be recognized on the computer. If this is the only USB to UART on your computer, four serial ports will be detected.

On Windows, four COM ports will appear, and on Linux, /dev/ttyUSB{0,1,2,3} will be shown as illustrated below:

![alt text](./images/image-4.png)

- `Interface 0`: HSS output
- `Interface 1`: U-Boot and Linux console output

On a Linux system, these correspond to the first and second serial ports, respectively.

To write the image to eMMC, connect to the `HSS` console. Interrupt the boot process when prompted (`Press a key to enter CLI, ESC to skip`).

Input: `
```
mmc
usbdmsc
```
This will prompt `Waiting for USB Host to connect`. 

A high-capacity USB storage device should now be visible on the computer. You can now use tools like Win32DiskImager/Rufus/USBImager/dd to write the image directly to it.

After writing the image, exit USB storage mode by pressing Ctrl+C on the HSS console. Image burning is now complete.

### Burning Image to SD Card

Simply use Rufus/Win32DiskImager/dd or similar tools to write the image to the SD card.

```shell
xzcat ubuntu-24.04-preinstalled-server-riscv64+icicle.img.xz | sudo dd of=/dev/sdX bs=4M iflag=fullblock status=progress 
```

## Starting the Development Board

Power up the development board. Boot information will be output to the second serial port.

> During the first boot of Ubuntu, `cloud-init` will be invoked. Due to the development board's performance limitations, the boot process may be slow, taking several minutes from power-up to login. This is expected.

Username: `ubuntu`

Password: `ubuntu`

Upon initial login, you will be prompted to change the password, follow the on-screen instructions.

## Expected Result

The system boots successfully, allowing login via the serial port.

## Actual Result

The system boots successfully, allowing login via the serial port.

Screen recording (from eMMC flashing to booting):


[![asciicast](https://asciinema.org/a/ECbt7b3ltAF29zFjDDgW9NUnU.svg)](https://asciinema.org/a/ECbt7b3ltAF29zFjDDgW9NUnU)


## Test Criteria

Success: Actual results match expected results.

Failure: Actual results do not match expected results.

## Test Conclusion

The test was successful.

## Reference Documents

- [PolarFire SoC Software Tool Flow](https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/knowledge-base/polarfire-soc-software-tool-flow.md)
- [MPFS Icicle Kit User Guide](https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/reference-designs-fpga-and-development-kits/icicle-kit-user-guide.md)
- [Updating MPFS Kit](https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/reference-designs-fpga-and-development-kits/updating-mpfs-kit.md)
- Under CC BY 4.0 license, by Microchip Technology Inc. and its subsidiaries

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
