# BuildRoot Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- System Version: Duo-V1.1.0
- Download Link: [click here](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
- Reference Installation Document: [click here](https://github.com/milkv-duo/duo-buildroot-sdk)

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- One USB Power Adapter
- One USB-A to C or USB C to C cable, used to power the development board
- One microSD card
- One USB card reader
- One USB to UART debugger (such as: CP2102, FT2232, etc., please note not to use CH340/341 series, as it may cause garbled text)
- Three DuPont cables

## Installation Steps

### Use the `ruyi` CLI to flash the image to the microSD card

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Log in to the system

Log in to the system via serial port.

## Expected Results

The system starts up properly and can be accessed through the onboard serial port.

## Actual Results

The system starts up properly and I can successfully log in through the onboard serial port.

### Boot Information

> The failure of the aic8800 insmod module is because the Duo S used for testing does not have a Wi-Fi chip.
>
> This is normal.

```log
Starting app...                                                                                                                     
                                                                                                                                    
[root@milkv-duo]~# insmod: can't insert '/mnt/system/ko/aic8800_fdrv.ko': No such device                                            
                                                                                                                                    
[root@milkv-duo]~#                                                                                                                  
[root@milkv-duo]~# uname -a                                                                                                         
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Mon Feb 26 16:01:35 CST 2024 riscv64 GNU/Linux                                               
[root@milkv-duo]~# cat /proc/cpuinfo                                                                                                
processor       : 0                                                                                                                 
hart            : 0                                                                                                                 
isa             : rv64imafdvcsu                                                                                                     
mmu             : sv39                                                                                                              
                                                                                                                                    
[root@milkv-duo]~# cat /etc/os-release                                                                                              
NAME=Buildroot                                                                                                                      
VERSION=20240226-1609                                                                                                               
ID=buildroot                                                                                                                        
VERSION_ID=2021.05                                                                                                                  
PRETTY_NAME="Buildroot 2021.05"                                                                                                     
[root@milkv-duo]~# 
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/Zbt8azPsJFYLWOYCKgPNrt9S7.svg)](https://asciinema.org/a/Zbt8azPsJFYLWOYCKgPNrt9S7)

## Test Judgement Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
