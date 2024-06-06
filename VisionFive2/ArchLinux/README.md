# Arch Linux VisionFive 2 Version 2 Test Report

## Test Environment

### Operating System Information

- System Version: ArchLinux-VF2_5.15.2_v5.11.3-cwt21.1.img.xz
- Download Link: [https://github.com/cwt-vf2/archlinux-image-vf2/releases/tag/cwt21.1](https://github.com/cwt-vf2/archlinux-image-vf2/releases/tag/cwt21.1)
- Reference Installation Document: [https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459](https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459)

> This image is provided by community developers and is unofficial. Arch Linux RISC-V currently only provides `rootfs`.

### Hardware Information

- StarFive VisionFive 2
- One USB power adapter
- One USB-A to C or C to C cable
- One microSD card
- One USB to UART debugger (e.g. CH340, CH341, FT2232, etc.)
- Three DuPont wires

## Installation Steps

### Extracting and Flashing the Image to the microSD Card

Assuming `/dev/sdc` is the storage card.

```bash
xzcat ArchLinux-VF2_5.15.2_v5.11.3-cwt21.1.img.xz | sudo dd of=/dev/sdc iflag=fullblock bs=4M status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 provides multiple boot modes that can be configured before powering on through onboard DIP switches; the development board itself is also marked.

To boot the Arch image, you can select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`) before power on. Note that this mode may require firmware updating in the Flash beforehand. If you encounter boot issues, please refer to the official documentation for firmware upgrading: [Update SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### Logging into the System

Log into the system via serial console.

Username: `root`
Default Password: `archriscv`

Or

Username: `user`
Password: `user`

## Expected Results

The system should boot up successfully and allow login via serial console.

## Actual Results

The system booted up successfully and login via serial console was achieved.

### Boot Information

```log
Arch Linux 5.2-cwt-5.11.3-2 (hvc0)                                                                                                  
                                                                                                                                    
ArchVF2 login: 15.2-cwt-5.11.3-2 (ttyS0)                                                                                            
                                                                                                                                    
ArchVF2 login: root                                                                                                                 
Password:                                                                                                                           
Login incorrect                                                                                                                     
                                                                                                                                    
ArchVF2 login: root                                                                                                                 
Password:                                                                                                                           
[root@ArchVF2 ~]# uname -a                                                                                                          
Linux ArchVF2 5.15.2-cwt-5.11.3-2 #1 SMP PREEMPT Fri Mar 22 19:02:42 +07 2024 riscv64 GNU/Linux                                     
[root@ArchVF2 ~]# cat /etc/os-release                                                                                               
NAME="Arch Linux"                                                                                                                   
PRETTY_NAME="Arch Linux"                                                                                                            
ID=arch                                                                                                                             
BUILD_ID=rolling                                                                                                                    
ANSI_COLOR="38;2;23;147;209"                                                                                                        
HOME_URL="https://archlinux.org/"                                                                                                   
DOCUMENTATION_URL="https://wiki.archlinux.org/"                                                                                     
SUPPORT_URL="https://bbs.archlinux.org/"                                                                                            
BUG_REPORT_URL="https://gitlab.archlinux.org/groups/archlinux/-/issues"                                                             
PRIVACY_POLICY_URL="https://terms.archlinux.org/docs/privacy-policy/"                                                               
LOGO=archlinux-logo                                                                                                                 
[root@ArchVF2 ~]# 
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/X6MYCn6vv0n6Es38KHhC1uOmc.svg)](https://asciinema.org/a/X6MYCn6vv0n6Es38KHhC1uOmc)

## Test Criteria

Test Passed: Actual results match expected results.

Test Failed: Actual results do not match expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
