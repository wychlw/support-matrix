
# openEuler RISC-V 23.09 HiFive Unmatched Version Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.09 RISC-V preview
- Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/
- Reference Installation Documentation: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/README.unmatched.txt

### Hardware Information

- HiFive Unmatched Rev A
- One microUSB cable (included with HiFive Unmatched)
- One ATX power supply
- One microSD card (Sandisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Ensure that the DIP switch is set to boot from the microSD card. If you haven't changed it, the default setting is to boot from the microSD card.

DIP switch should be set as follows: `MSEL[3:0]=1011`

### Use the `ruyi` CLI to Flash the Image to the microSD Card

Install [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Log in to the System

Log in to the system via the onboard serial port (connect to another computer using the microUSB cable).

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

## Expected Results

The system boots up normally and can be logged into via the onboard serial port.

## Actual Results

The system boots up normally and successfully logged into via the onboard serial port.

### Boot Information

```log
Welcome to 6.1.0-11.oe2309.riscv64                                                                                    
                                                                                                                      
System information as of time:  Mon Sep 18 08:03:17 AM CST 2023                                                       
                                                                                                                      
System load:    1.94                                                                                                  
Processes:      130                                                                                                   
Memory used:    1.2%                                                                                                  
Swap used:      0.0%                                                                                                  
Usage On:       16%                                                                                                   
Users online:   1                                                                                                     
To run a command as administrator(user "root"),use "sudo <command>".                                                  
[openeuler@openeuler-riscv64 ~]$
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/GzU3kCzrnvFfJMU1cJH30knrx.svg)](https://asciinema.org/a/GzU3kCzrnvFfJMU1cJH30knrx)

## Test Judgment Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
