# BuildRoot Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: Duo-V1.0.7
- Download Link: [GitHub Duo Buildroot SDK Releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
- Reference Installation Document: [GitHub Duo Buildroot SDK](https://github.com/milkv-duo/duo-buildroot-sdk)

### Hardware Information

- Milk-V Duo 64M
- USB Power Adapter x1
- USB-A to C or USB C to C Cable x1
- MicroSD Card x1
- USB to UART Debugger x1 (e.g. CH340, CH341, FT2232, etc.)
- Dupont Cables x3
- Pre-soldered debugging pin headers on the Milk-V Duo board

## Installation Steps

### Flash Image to MicroSD Card using `ruyi` CLI

Install [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the instructions.

### Login to the System

Login to the system via serial port.

## Expected Results

System boots up correctly and can be accessed via onboard serial port.

## Actual Results

The system boots up correctly and successfully logs in via the onboard serial port.

### Boot Information

```log
[root@milkv-duo]~# uname -a                                                                                                                                             
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Sat Dec 23 12:29:13 CST 2023 riscv64 GNU/Linux                                                                                   
[root@milkv-duo]~# cat /proc/cpuinfo                                                                                                                                    
processor       : 0                                                                                                                                                     
hart            : 0                                                                                                                                                     
isa             : rv64imafdvcsu                                                                                                                                         
mmu             : sv39                                                                                                                                                  
                                                                                                                                                                        
[root@milkv-duo]~# 
```

Screen recording (from flashing image to logging into the system):

[![asciicast](https://asciinema.org/a/rsenSOJwdlmUXcJ8sQwubPgtr.svg)](https://asciinema.org/a/rsenSOJwdlmUXcJ8sQwubPgtr)

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
