# openSUSE Tumbleweed VisionFive 2 Version Testing Report

## Test Environment

### Operating System Information

- System Version: openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2024.03.15-Build23.14.raw.xz
- Download Link: [Download Link](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/)
- Installation Reference Document: [VisionFive2 Installation Guide](https://en.opensuse.org/HCL:VisionFive2)

### Hardware Information

- StarFive VisionFive 2
- 1 USB Power Adapter
- 1 USB-A to C or C to C cable
- 1 microSD card
- 1 USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- 3 Dupont wires

## Installation Steps

### Unzip and Flash Image to microSD Card

Assuming `/dev/sdc` is the storage card.

```bash
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2024.03.15-Build23.14.raw.xz | sudo dd of=/dev/sdc iflag=fullblock status=progress bs=4M
```

### Boot Mode Selection

StarFive VisionFive 2 provides various boot modes that can be configured before powering on using onboard DIP switches; the development board itself is also labeled.

To boot the openSUSE image, the microSD card boot mode needs to be selected (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

> Note that there is a small chance of boot failure in this mode. In case of boot failure, the serial output may resemble the following:

```log
dwmci_s: Response Timeout.                                                                                            
dwmci_s: Response Timeout.                                                                                            
BOOT fail,Error is 0xffffffff
```

> You can try powering the development board again or pressing the button near the USB Type-C power interface once. This usually resolves the booting issue.

### System Login

Login to the system via serial console.

Username: `root`
Default Password: `linux`

## Expected Results

The system boots up correctly and can be accessed via serial console.

## Actual Results

The system boots up correctly, and access via serial console is successful.

### Boot Information

```log
Welcome to openSUSE Tumbleweed 20240322 - Kernel 6.8.1-85-default (ttyS0).                                                          
                                                                                                                                    
end0:  fe80::ecba:cd3:320d:39f8                                                                                                     
end1:                                                                                                                               
                                                                                                                                    
                                                                                                                                    

localhost login: root                                                                                                               
Password:                                                                                                                           
Have a lot of fun...                                                                                                                
localhost:~ # uname -a                                                                                                              
Linux localhost.localdomain 6.8.1-85-default #1 SMP PREEMPT_DYNAMIC Fri Mar 22 07:05:00 UTC 2024 (c838682) riscv64 riscv64 riscv64 x
localhost:~ # cat /etc/os-release                                                                                                   
NAME="openSUSE Tumbleweed"                                                                                                          
# VERSION="20240322"                                                                                                                
ID="opensuse-tumbleweed"                                                                                                            
ID_LIKE="opensuse suse"                                                                                                             
VERSION_ID="20240322"                                                                                                               
PRETTY_NAME="openSUSE Tumbleweed"                                                                                                   
ANSI_COLOR="0;32"                                                                                                                   
# CPE 2.3 format, boo#1217921                                                                                                       
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20240322:*:*:*:*:*:*:*"                                                                     
#CPE 2.2 format                                                                                                                     
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20240322"                                                                                     
BUG_REPORT_URL="https://bugzilla.opensuse.org"                                                                                      
SUPPORT_URL="https://bugs.opensuse.org"                                                                                             
HOME_URL="https://www.opensuse.org"                                                                                                 
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"                                                                       
LOGO="distributor-logo-Tumbleweed"                                                                                                  
localhost:~ # 
```

Screen recording (from image flashing to system login):

[![asciicast](https://asciinema.org/a/z3xt9HGtT5iVtI7tbtQNi9rHf.svg)](https://asciinema.org/a/z3xt9HGtT5iVtI7tbtQNi9rHf)

## Testing Criteria

Test Successful: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
