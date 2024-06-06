# Debian bookworm/sid HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: Debian bookworm/sid
- Download Link: [Download Debian Sid RISC-V for SiFive Unmatched](https://people.debian.org/~deiv/riscv/debian-sid-risc-v-sifive-unmatched.tar.xz)
- Reference Installation Document: [Debian Installation Guide for SiFive HiFive Unmatched](https://wiki.debian.org/InstallingDebianOn/SiFive/%20HiFiveUnmatched)

### Hardware Information

- HiFive Unmatched Rev A
- 1 microUSB cable (included with HiFive Unmatched)
- 1 ATX power supply
- 1 microSD card (Sandisk Extreme Pro 64GB UHS-I)

## Installation Steps

### Boot Device Selection

Make sure the DIP switches are set to boot from the microSD card. If you haven't changed it, the factory default is to boot from the microSD card.

DIP switch settings should be: `MSEL[3:0]=1011`

### Unzip and Burn Image to microSD Card

`/dev/sdc` is the location of the microSD card, please change it according to your actual situation.

```bash
tar xvf debian-sid-risc-v-sifive-unmatched.tar.xz
sudo dd if=debian-sid-risc-v-sifive-unmatched.img of=/dev/sdc bs=1M status=progress
```

### Log in to the System

Log in to the system via the onboard serial port (connect to another computer using the microUSB cable).

Default username: `root`
Default password: `sifive`

## Expected Results

The system should start up properly, and you should be able to log in via the onboard serial port.

## Actual Results

The system started up successfully, and I was able to log in via the onboard serial port.

### Boot Information

```log
Debian GNU/Linux bookworm/sid unmatched ttySIF0                                                                       
                                                                                                                      
unmatched login: root                                                                                                 
Password:                                                                                                             
Linux unmatched 5.14.0-3-riscv64 #1 SMP Debian 5.14.12-1 (2021-10-14) riscv64                                         
                                                                                                                      
The programs included with the Debian GNU/Linux system are free software;                                             
the exact distribution terms for each program are described in the                                                    
individual files in /usr/share/doc/*/copyright.                                                                       
                                                                                                                      
Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent                                                     
permitted by applicable law.                                                                                          
root@unmatched:~# uname -a                                                                                            
Linux unmatched 5.14.0-3-riscv64 #1 SMP Debian 5.14.12-1 (2021-10-14) riscv64 GNU/Linux                               
root@unmatched:~# cat /etc/os-release                                                                                 
PRETTY_NAME="Debian GNU/Linux bookworm/sid"                                                                           
NAME="Debian GNU/Linux"                                                                                               
ID=debian                                                                                                             
HOME_URL="https://www.debian.org/"                                                                                    
SUPPORT_URL="https://www.debian.org/support"                                                                          
BUG_REPORT_URL="https://bugs.debian.org/"                                                                             
root@unmatched:~# cat /proc/cpuinfo                                                                                   
processor       : 0                                                                                                   
hart            : 4                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
processor       : 1                                                                                                   
hart            : 1                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
processor       : 2                                                                                                   
hart            : 2                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
processor       : 3                                                                                                   
hart            : 3                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
root@unmatched:~# 
```

Screen recording (from image flashing to system login)

[![asciicast](https://asciinema.org/a/YjvmONomTstvHYU4yLnKVX7Rv.svg)](https://asciinema.org/a/YjvmONomTstvHYU4yLnKVX7Rv)

## Test Judgment Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
