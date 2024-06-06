
# BuildRoot VisionFive 2 Version Test Report

## Test Environment

### Operating System Information

- System Version: VisionFive 2 Software v5.11.3
- Download Link: [VisionFive 2 Releases](https://github.com/starfive-tech/VisionFive2/releases)
- Installation Guide: [VisionFive 2 SDK Quick Start Guide](https://doc.rvspace.org/VisionFive2/SDK_Quick_Start_Guide/VisionFive2_SDK_QSG/running_sdk_on_visionfive_2.html)

### Hardware Information

- StarFive VisionFive 2
- One USB power adapter
- One USB-A to C or C to C cable
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232)
- Three DuPont wires

## Installation Steps

### Flash Image to microSD Card

Assuming `/dev/sdc` is the storage card.

```bash
sudo dd if=sdcard.img of=/dev/sdc bs=1M status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 offers multiple boot modes that can be configured using onboard dip switches before powering on; the board itself is also labeled.

To boot with the original BuildRoot image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Please note that this mode may require firmware updates on the Flash memory in advance. If you encounter booting issues, refer to the official documentation for firmware upgrade: [Update SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html).

If not updating the firmware, choose microSD card boot (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

> Please note that there is a small probability of boot failure in this mode. If you encounter boot failure, the serial output may resemble the following:
>
>```log
>dwmci_s: Response Timeout.                                                                                            
>dwmci_s: Response Timeout.                                                                                            
>BOOT fail,Error is 0xffffffff
>```
>
>You can try repowering the development board or pressing the button near the USB Type-C power port. This usually resolves the startup issue.

### System Login

Log in to the system via serial connection.

Default username: `root`
Default password: `starfive`

## Expected Results

The system starts up normally and can be accessed through serial connection.

## Actual Results

The system starts up properly and logging in via serial connection is successful.

### Boot Information

```log
Welcome to Buildroot
buildroot login: root
Password: 
# uname -a
Linux buildroot 5.15.0 #1 SMP Thu Mar 14 19:21:20 CST 2024 riscv64 GNU/Linux
# cat /etc/os-release 
NAME=Buildroot
VERSION=JH7110_VF2_515_v5.11.3
ID=buildroot
VERSION_ID=2021.11
PRETTY_NAME="Buildroot 2021.11"
#
```

Screen recording (from flashing the image to system login):

[![asciicast](https://asciinema.org/a/EUliFJz2UOlHIxrZbK2mePVbS.svg)](https://asciinema.org/a/EUliFJz2UOlHIxrZbK2mePVbS)

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
