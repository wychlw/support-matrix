# Debian VisionFive 2 Version Test Report

## Test Environment

### Operating System Information

- System Version: Debian bookworm (starfive-jh7110-202403-SD-minimal-desktop-wayland.img.bz2)
- Download Link: [Debian StarFive Tech](https://debian.starfivetech.com/)
- Reference Installation Document: [OpenEuler Installation Guide](https://gitee.com/openeuler/RISC-V/blob/master/release/openEuler-23.03/Installation_Book/Visionfive2/README.md)

### Hardware Information

- StarFive VisionFive 2
- 1 USB Power Adapter
- 1 USB-A to C or C to C Cable
- 1 microSD Card
- 1 USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- 3 DuPont Wires

## Installation Steps

### Extract and Write Image to microSD Card

Assume `/dev/sdc` is the storage card.

```bash
bzip2 -dk starfive-jh7110-202403-SD-minimal-desktop-wayland.img.bz2
sudo dd if=starfive-jh7110-202403-SD-minimal-desktop-wayland.img of=/dev/sdc bs=1M status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 provides multiple boot modes, which can be configured using onboard dip switches before powering on; markings are also present on the development board itself.

To boot the factory Debian image, choose the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require firmware updating in the Flash beforehand. If you encounter booting issues, please refer to the official documentation for firmware upgrading: [Updating SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

If not updating firmware, select microSD card boot (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

> Note that there is a slight chance of boot failure in this mode. If facing startup issues, serial port output may resemble the following:
>
>```log
>dwmci_s: Response Timeout.                                                                                            
>dwmci_s: Response Timeout.                                                                                            
>BOOT fail,Error is 0xffffffff
>```
>
> You can try powering off and on the development board again or pressing the button near the USB Type-C power supply port. Usually, this can resolve startup problems.

### Login System

Log in to the system via serial port.

Default username: `user`
Default password: `starfive`

## Expected Results

The system should boot normally, allowing login via serial port.

## Actual Results

The system booted successfully, and login via serial port was also successful.

### Boot Information

```log
user@starfive:~$ uname -a                                                                                             
Linux starfive 6.1.31-starfive #1 SMP Mon Mar  4 21:31:49 CST 2024 riscv64 GNU/Linux                                  
user@starfive:~$ cat /etc/os-release                                                                                  
PRETTY_NAME="Debian GNU/Linux bookworm/sid"                                                                           
NAME="Debian GNU/Linux"                                                                                               
VERSION_CODENAME=bookworm                                                                                             
ID=debian                                                                                                             
HOME_URL="https://www.debian.org/"                                                                                    
SUPPORT_URL="https://www.debian.org/support"                                                                          
BUG_REPORT_URL="https://bugs.debian.org/"                                                                             
BUILD_ID=7                                                                                                            
user@starfive:~$
```

Screen recording (from image writing to system login):

[![asciicast](https://asciinema.org/a/CCoYSyfdX7TWoiXM8Kct8nTVF.svg)](https://asciinema.org/a/CCoYSyfdX7TWoiXM8Kct8nTVF)

## Test Criteria

Test Passed: The actual results match the expected results.

Test Failed: The actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
