# openEuler RISC-V 23.03 D1 Version Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.03 RISC-V preview
- Download Link: [openEuler 23.03 V1 RISC-V64 D1](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/)
- Reference Installation Document: [Installation Book D1 and Licheerv](https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/D1_and_Licheerv)

### Hardware Information

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- One USB-A power supply
- One USB-A to C cable
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont wires

## Installation Steps

### Write Image to microSD Card Using `ruyi` CLI

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### System Login

Log in to the system via serial port.

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

## Expected Results

The system boots up successfully and can be logged into via the onboard serial port.

## Actual Results

The system boots up successfully and login is achieved through the onboard serial port.

### Boot Information

```log
openEuler 23.03                                                                                                                                   
Kernel 6.1.0-0.rv64                                                                                                                               
                                                                                                                                                  
openeuler-riscv64 login: c3.11.oe2303.riscv64 on an riscv64                                                                                       
                                                                                                                                                  
openeuler-riscv64 login: root                                                                                                                     
Password: [   57.563173] EXT4-fs (mmcblk0p4): resized filesystem to 15498496                                                                      
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  
Welcome to 6.1.0-0.rc3.11.oe2303.riscv64                                                                                                          
                                                                                                                                                  
System information as of time:  Fri Jan  2 08:01:41 CST 1970                                                                                      
                                                                                                                                                  
System load:    3.42                                                                                                                              
Processes:      93                                                                                                                                
Memory used:    6.8%                                                                                                                              
Swap used:      0.0%                                                                                                                              
Usage On:       2%                                                                                                                                
Users online:   1                                                                                                                                 
                                                                                                                                                  
                                                                                                                                                  
[root@openeuler-riscv64 ~]# cat /proc/cpuinfo                                                                                                     
processor       : 0                                                                                                                               
hart            : 0                                                                                                                               
isa             : rv64imafdc                                                                                                                      
mmu             : sv39                                                                                                                            
uarch           : thead,c906                                                                                                                      
mvendorid       : 0x5b7                                                                                                                           
marchid         : 0x0                                                                                                                             
mimpid          : 0x0                                                                                                                             
                                                                                                                                                  
[root@openeuler-riscv64 ~]#
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/dJV431qjqOPT6iR7hzieM3G41.svg)](https://asciinema.org/a/dJV431qjqOPT6iR7hzieM3G41)

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
