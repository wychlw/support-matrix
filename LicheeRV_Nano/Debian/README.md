# BuildRoot LicheeRV Nano Test Report

## Test Environment

### Operating System Information

- System Version: Initial Release
- Download Link: [GitHub Repository](https://github.com/Fishwaldo/sophgo-sg200x-debian)
- Installation Reference Document: [GitHub Repository](https://github.com/Fishwaldo/sophgo-sg200x-debian)

### Hardware Information

- LicheeRV Nano
- One Type-C power cable
- One UART to USB debugger

## Installation Steps

### Write Image to microSD Card Using `dd`

Download the image, then extract and write it:

```shell
lz4 -dk licheervnano_sd.img.lz4
sudo dd if=licheervnano_sd.img of=/dev/your_device bs=1M status=progress
```

### System Login

Log in to the system using the serial port.

| Username | Password |
|----------|----------|
| root     | rv       |
| debian   | rv       |


## Expected Results

The system should boot up successfully and allow login via serial port.

## Actual Results

The system successfully boots up and allows login via serial port.

### Boot Information

Screen recording (from writing the image to logging into the system):

[![asciicast](https://asciinema.org/a/d6uwAengdlXVbMj0KAdVbPhMX.svg)](https://asciinema.org/a/d6uwAengdlXVbMj0KAdVbPhMX)

```log
Debian GNU/Linux trixie/sid licheervnano ttyS0                                                                          
                                                                                                                        
licheervnano login: root                                                                                                
Password:                                                                                                               
Linux licheervnano 5.10.4-20240329-1+ #1 PREEMPT Sat Apr 13 07:08:27 UTC 2024 riscv64                                   
                                                                                                                        
The programs included with the Debian GNU/Linux system are free software;                                               
the exact distribution terms for each program are described in the                                                      
individual files in /usr/share/doc/*/copyright.                                                                         
                                                                                                                        
Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent                                                       
permitted by applicable law.                                                                                            
root@licheervnano:~# cat /proc/cpuinfo                                                                                  
processor       : 0                                                                                                     
hart            : 0                                                                                                     
isa             : rv64imafdvcsu                                                                                         
mmu             : sv39                                                                                                  
                                                                                                                        
root@licheervnano:~# cat /etc/os-release                                                                                
PRETTY_NAME="Debian GNU/Linux trixie/sid"                                                                               
NAME="Debian GNU/Linux"                                                                                                 
VERSION_CODENAME=trixie                                                                                                 
ID=debian                                                                                                               
HOME_URL="https://www.debian.org/"                                                                                      
SUPPORT_URL="https://www.debian.org/support"                                                                            
BUG_REPORT_URL="https://bugs.debian.org/"                                                                               
root@licheervnano:~# uname -a                                                                                           
Linux licheervnano 5.10.4-20240329-1+ #1 PREEMPT Sat Apr 13 07:08:27 UTC 2024 riscv64 GNU/Linux                         
root@licheervnano:~# 
```

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
