# Ubuntu 23.10 D1 Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 23.10
- Download Link: [Ubuntu RISC-V](https://ubuntu.com/download/risc-v)
    - Or mirror sites: [Nezha](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/mantic/release/ubuntu-23.10-preinstalled-server-riscv64+nezha.img.xz) | [Lichee RV](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/mantic/release/ubuntu-23.10-preinstalled-server-riscv64+licheerv.img.xz)
- Reference Installation Document: [RISC-V/LicheeRV](https://wiki.ubuntu.com/RISC-V/LicheeRV)

### Hardware Information

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- One USB-A power supply
- One USB-A to C cable
- One microSD card
- One USB to UART debugger (e.g. CH340, CH341, FT2232, etc.)
- Three DuPont wires

## Installation Steps

### Write Image to microSD Card

Use `dd` to write the image to the microSD card.

### Accessing the System

Access the system via serial console.

Default username: `ubuntu`
Default password: `ubuntu`

During the initial login, the system will prompt for a password change.

## Expected Results

The system boots successfully and allows login via on-board serial console.

## Actual Results

The system boots successfully and login via on-board serial console is successful.

### Boot Information

```log
ubuntu@ubuntu:~$ cat /proc/cpuinfo                                                                                    
processor       : 0                                                                                                   
hart            : 0                                                                                                   
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm                                                              
mmu             : sv39                                                                                                
uarch           : thead,c906                                                                                          
mvendorid       : 0x5b7                                                                                               
marchid         : 0x0                                                                                                 
mimpid          : 0x0                                                                                                 
                                                                                                                      
ubuntu@ubuntu:~$
```

Screen recording (from writing image to accessing system):

[![asciicast](https://asciinema.org/a/wEtZPokxvzJ72S9ETh8PSqdUt.svg)](https://asciinema.org/a/wEtZPokxvzJ72S9ETh8PSqdUt)

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
