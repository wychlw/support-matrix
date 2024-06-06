# Gentoo VisionFive 2 Version Test Report

## Test Environment

### Operating System Information

- System Version: gentoo.img.bz2
- Download Link: [Download Link](https://drive.google.com/file/d/10TDsk2FwZDJv3yJvDAfCam5Wf9ibS6Eg/view?usp=sharing)
- Reference Installation Document: [Installation Document](https://forum.rvspace.org/t/experimental-gentoo-image/1807)

> This image is provided by the community developers and is not an official image.

### Hardware Information

- StarFive VisionFive 2
- USB Power Adapter x1
- USB-A to C or C to C Cable x1
- microSD Card x1
- USB to UART Debugger x1 (e.g. CH340, CH341, FT2232, etc.)
- Dupont Wire x3

## Installation Steps

### Unzip and Write Image to microSD Card

Assuming `/dev/sdc` is the storage card.

```bash
bzcat gentoo.img.bz2 | sudo dd of=/dev/sdc iflag=fullblock bs=4M status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 offers multiple boot modes, which can be configured via onboard DIP switches before powering on; there are also markings on the development board.

To boot the Gentoo image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`) before power on. Please note that this mode may require updating the firmware in the Flash beforehand. If you encounter boot issues, refer to the official documentation for firmware upgrade instructions: [Update SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)


### Logging into the System

Login to the system using serial communication.

Username: `root`
No password required.

## Expected Results

The system boots up successfully and can be accessed through serial communication.

## Actual Results

The system boots up successfully and login via serial communication is successful.

### Boot Information

```log
root@StarFive ~ # uname -a                                                                                                          
Linux StarFive 5.15.0-starfive #1 SMP Mon Feb 27 14:03:14 EST 2023 riscv64 GNU/Linux                                                
root@StarFive ~ # cat /etc/os-release                                                                                               
NAME=Gentoo                                                                                                                         
ID=gentoo                                                                                                                           
PRETTY_NAME="Gentoo Linux"                                                                                                          
ANSI_COLOR="1;32"                                                                                                                   
HOME_URL="https://www.gentoo.org/"                                                                                                  
SUPPORT_URL="https://www.gentoo.org/support/"                                                                                       
BUG_REPORT_URL="https://bugs.gentoo.org/"                                                                                           
VERSION_ID="2.13"                                                                                                                   
root@StarFive ~ #
```

Screen recording (from image flashing to system login):

[![asciicast](https://asciinema.org/a/HYfHc1I7NtPlUkfSuY7W1cy5e.svg)](https://asciinema.org/a/HYfHc1I7NtPlUkfSuY7W1cy5e)

## Test Criteria

Test Passed: The actual results match the expected results.

Test Failed: The actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
