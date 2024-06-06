# Fedora 38 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: Fedora 38
- Download Link: [Fedora-Developer-38-20230519.n.0-mmc.raw.img.xz](https://dl.fedoraproject.org/pub/alt/risc-v/disk_images/Fedora-Developer-38-20230519.n.0.SiFive.Unmatched.and.QEMU/Fedora-Developer-38-20230519.n.0-mmc.raw.img.xz)
- Reference Installation Document: [README.md](https://dl.fedoraproject.org/pub/alt/risc-v/disk_images/Fedora-Developer-38-20230519.n.0.SiFive.Unmatched.and.QEMU/README.md)

### Hardware Information

- HiFive Unmatched Rev A
- One microUSB cable (included with HiFive Unmatched)
- One ATX power supply
- One microSD card (Sandisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Ensure that the DIP switches are set to boot from the microSD card. If you have not made any changes, the factory default is to boot from the microSD card.

The DIP switches should be set as follows: `MSEL[3:0]=1011`

### Extract and Flash the Image to the microSD Card

`/dev/sdc` is the location of the microSD card, please change accordingly based on your actual situation.

```bash
sudo wipefs -af /dev/sdc
xzcat Fedora-Developer-38-20230519.n.0-mmc.raw.img.xz | sudo dd of=/dev/sdc iflag=fullblock bs=4M status=progress
```

### Log in to the System

Log in to the system via the onboard serial port (connect to another computer using the microUSB cable).

Default username: `riscv` or `root`
Default password: `fedora_rocks!`

## Expected Results

The system starts up normally and can be accessed via the onboard serial port.

## Actual Results

The system boots up successfully, and access through the onboard serial port is established.

### Boot Information


```log
https://fedoraproject.org/wiki/Architectures/RISC-V                                                                                 
                                                                                                                                    
Build date: Fri May 19 12:44:23 UTC 2023                                                                                            
                                                                                                                                    
Kernel 6.2.16-300.0.riscv64.fc38.riscv64 on an riscv64 (ttySIF0)                                                                    
                                                                                                                                    
The root password is 'fedora_rocks!'.                                                                                               
root password logins are disabled in SSH starting Fedora 31.                                                                        
User 'riscv' with password 'fedora_rocks!' in 'wheel' group is provided.                                                            
                                                                                                                                    
To install new packages use 'dnf install ...'                                                                                       
                                                                                                                                    
To upgrade disk image use 'dnf upgrade --best'                                                                                      
                                                                                                                                    
If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.                                                             
                                                                                                                                    
For updates and latest information read:                                                                                            
https://fedoraproject.org/wiki/Architectures/RISC-V                                                                                 
                                                                                                                                    
Fedora/RISC-V                                                                                                                       
-------------                                                                                                                       
Koji:               http://fedora.riscv.rocks/koji/                                                                                 
SCM:                http://fedora.riscv.rocks:3000/                                                                                 
Distribution rep.:  http://fedora.riscv.rocks/repos-dist/                                                                           
Koji internal rep.: http://fedora.riscv.rocks/repos/                                                                                
fedora-riscv login: root                                                                                                            
Password:                                                                                                                           
Login incorrect                                                                                                                     
                                                                                                                                    
fedora-riscv login: root                                                                                                            
Password:                                                                                                                           
Login incorrect 

fedora-riscv login: root                                                                                                            
Password:                                                                                                                           
Last failed login: Wed May 10 20:04:31 EDT 2023 on ttySIF0                                                                          
There were 2 failed login attempts since the last successful login.                                                                 
[root@fedora-riscv ~]# cat /etc/os-release                                                                                          
NAME="Fedora Linux"                                                                                                                 
VERSION="38 (Thirty Eight)"                                                                                                         
ID=fedora                                                                                                                           
VERSION_ID=38                                                                                                                       
VERSION_CODENAME=""                                                                                                                 
PLATFORM_ID="platform:f38"                                                                                                          
PRETTY_NAME="Fedora Linux 38 (Thirty Eight)"                                                                                        
ANSI_COLOR="0;38;2;60;110;180"                                                                                                      
LOGO=fedora-logo-icon                                                                                                               
CPE_NAME="cpe:/o:fedoraproject:fedora:38"                                                                                           
DEFAULT_HOSTNAME="fedora"                                                                                                           
HOME_URL="https://fedoraproject.org/"                                                                                               
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/f38/system-administrators-guide/"                                    
SUPPORT_URL="https://ask.fedoraproject.org/"                                                                                        
BUG_REPORT_URL="https://bugzilla.redhat.com/"                                                                                       
REDHAT_BUGZILLA_PRODUCT="Fedora"                                                                                                    
REDHAT_BUGZILLA_PRODUCT_VERSION=38                                                                                                  
REDHAT_SUPPORT_PRODUCT="Fedora"                                                                                                     
REDHAT_SUPPORT_PRODUCT_VERSION=38                                                                                                   
SUPPORT_END=2024-05-14                                                                                                              
[root@fedora-riscv ~]#
```

Screen recording (from flashing the image to logging into the system)

[![asciicast](https://asciinema.org/a/vulbDuQBEkAx4ldcquyMpVR2m.svg)](https://asciinema.org/a/vulbDuQBEkAx4ldcquyMpVR2m)

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
