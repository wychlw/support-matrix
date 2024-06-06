# openSUSE Tumbleweed HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: openSUSE Tumbleweed
- Download Link: https://download.opensuse.org/repositories/home:/Andreas_Schwab:/riscv:/unmatched/images/openSUSE-Tumbleweed-RISC-V-JeOS-hifiveunmatched.riscv64-2024.03.15-Build1.7.raw.xz
- Reference Installation Guide: https://en.opensuse.org/HCL:HiFive_Unmatched

### Hardware Information

- HiFive Unmatched Rev A
- One microUSB cable (included with HiFive Unmatched)
- One ATX power supply
- One microSD card (Sandisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Ensure that the DIP switches are set to boot from the microSD card. If you haven't made any changes, the factory default setting is to boot from the microSD card.

The DIP switches should be set as follows: `MSEL[3:0]=1011`

### Unzip and Burn Image to microSD Card

`/dev/sdc` is the location of the microSD card, please change it according to your actual situation.

```bash
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-hifiveunmatched.riscv64-2024.03.15-Build1.7.raw.xz | sudo dd bs=4M of=/dev/sdc iflag=fullblock status=progress
```

### System Login

Log in to the system via the onboard serial port (connect to another computer using a microUSB cable).

Default Username: `root` Default Password: `linux`

## Expected Results

The system boots up correctly and can be accessed via the onboard serial port.

## Actual Results

The system boots up correctly and login via the onboard serial port is successful.

### Boot Information

```log
Welcome to openSUSE Tumbleweed 20240320 - Kernel 6.8.1-1-default (ttySIF0).                                                         
                                                                                                                                    
end0:                                                                                                                               
                                                                                                                                    
                                                                                                                                    
localhost login: root                                                                                                               
Password:                                                                                                                           
Have a lot of fun...                                                                                                                
stty: 'standard input': unable to perform all requested operations                                                                  
localhost:~ # cat /etc/os-release                                                                                                   
NAME="openSUSE Tumbleweed"                                                                                                          
# VERSION="20240320"                                                                                                                
ID="opensuse-tumbleweed"                                                                                                            
ID_LIKE="opensuse suse"                                                                                                             
VERSION_ID="20240320"                                                                                                               
PRETTY_NAME="openSUSE Tumbleweed"                                                                                                   
ANSI_COLOR="0;32"                                                                                                                   
# CPE 2.3 format, boo#1217921                                                                                                       
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20240320:*:*:*:*:*:*:*"                                                                     
#CPE 2.2 format                                                                                                                     
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20240320"                                                                                     
BUG_REPORT_URL="https://bugzilla.opensuse.org"                                                                                      
SUPPORT_URL="https://bugs.opensuse.org"                                                                                             
HOME_URL="https://www.opensuse.org"                                                                                                 
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"                                                                       
LOGO="distributor-logo-Tumbleweed"
localhost:~ # uname -a                                                                                                              
Linux localhost.localdomain 6.8.1-1-default #1 SMP PREEMPT_DYNAMIC Tue Mar 19 07:32:20 UTC 2024 (d922afa) riscv64 riscv64 riscv64 Gx
localhost:~ # 
```

Screen recording (from flashing the image to logging into the system)

[![asciicast](https://asciinema.org/a/Yq2qb4xYNEMzUBxIcUkdyI2pp.svg)](https://asciinema.org/a/Yq2qb4xYNEMzUBxIcUkdyI2pp)

## Test Criteria

Test Success: Actual results match the expected results.

Test Failure: Actual results do not match the expected results.

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
