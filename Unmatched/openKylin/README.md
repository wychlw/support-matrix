# OpenKylin 1.0 HiFive Unmatched Version Test Report

## Test Environment

### Operating System Information

- System Version: OpenKylin 1.0
- Download Link: [OpenKylin Official Website](https://www.openkylin.top/downloads)
- Installation Reference Document: [OpenKylin Installation Guide](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

### Hardware Information

- HiFive Unmatched Rev A
- One microUSB cable (included with HiFive Unmatched)
- One ATX power supply
- One microSD card (Sandisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Make sure the DIP switch is set to boot from the microSD card. If you haven't changed it, the factory default is to boot from the microSD card.

DIP switch settings should be as follows: `MSEL[3:0]=1011`

### Write Image to microSD Card using `ruyi` CLI

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### System Login

Login to the system via the onboard serial port (connect via microUSB cable to another computer) or the graphical interface.

Default username: `openkylin`
Default password: `openkylin`

## Expected Results

The system should boot up correctly, allowing login via the onboard serial port or graphical interface.

## Actual Results

The system boots up correctly and login via the onboard serial port is successful.

### Boot Information

```log
Welcome to openKylin 1.0 (GNU/Linux 5.11.0-1030-generic riscv64)                                                      
                                                                                                                      
 * Support:        https://openkylin.top                                                                              
                                                                                                                      
The programs included with the openKylin system are free software;                                                    
the exact distribution terms for each program are described in the                                                    
individual files in /usr/share/doc/*/copyright.                                                                       
                                                                                                                      
openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by                                               
applicable law.                                                                                                       
                                                                                                                      
To run a command as administrator (user "root"), use "sudo <command>".                                                
See "man sudo_root" for details.                                                                                      
                                                                                                                      
openkylin@openkylin:~$                                                                                                
openkylin@openkylin:~$ cat /etc/os-release                                                                            
NAME="openKylin"                                                                                                      
FULL_NAME="openKylin"                                                                                                 
VERSION="1.0 (yangtze)"                                                                                               
VERSION_US="1.0 (yangtze)"                                                                                            
ID=openkylin                                                                                                          
PRETTY_NAME="openKylin 1.0"                                                                                           
VERSION_ID="1.0"                                                                                                      
HOME_URL="https://www.openkylin.top/"                                                                                 
VERSION_CODENAME=yangtze                                                                                              
PRODUCT_FEATURES=3                                                                                                    
openkylin@openkylin:~$ cat /proc/cpuinfo                                                                              
processor       : 0                                                                                                   
hart            : 4                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
processor       : 1                                                                                                   
hart            : 1                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
processor       : 2                                                                                                   
hart            : 2                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
processor       : 3                                                                                                   
hart            : 3                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
openkylin@openkylin:~$ 
```

Screen recording (from image writing to system login):

[![asciicast](https://asciinema.org/a/Wgz7wgCph6BhEQpEskH4LDMd4.svg)](https://asciinema.org/a/Wgz7wgCph6BhEQpEskH4LDMd4)

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

Test Pass.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
