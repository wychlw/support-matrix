# Arch Linux Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: milkv-duo-archlinux-riscv64-2023-10-09-7.0gb-v0.0.3-spiritdude.img
- Download Link: [Google Drive Link](https://drive.google.com/file/d/1Qf8ioR29KCsvt2MIWre168Um9Q8ot_z5/view?usp=sharing)
- Reference Installation Document: [ArchLinux Disk Image](https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#ArchLinux_Disk_Image)

> Note: This image is provided by the community developers and is unofficial.

### Hardware Information

- Milk-V Duo 64M
- 1 USB power adapter
- 1 USB-A to C or USB C to C cable
- 1 microSD card
- 1 USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- 3 DuPont wires
- Pre-soldered debug pins on the Milk-V Duo main body
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Write the Image to the microSD Card using `dd`

```shell
unzip milkv-duo-archlinux-riscv64-2023-10-09-7.0gb-v0.0.3-spiritdude.zip
dd if=milkv-duo-archlinux-riscv64-2023-10-09-7.0gb-v0.0.3-spiritdude.img of=/dev/sdc bs=1M status=progress
```

### Login to the System

Login to the system via a serial port.

Username: `root`
Password: `milkv`

## Expected Outcome

The system boots up successfully, and login is possible via the serial port.

## Actual Outcome

The system boots up successfully, and login via the serial port is successful.

### Boot Information

```log
[root@archlinux ~]# uname -a                                                                                                        
Linux archlinux 5.10.4-tag- #1 PREEMPT Wed Oct 18 17:20:17 CEST 2023 riscv64 GNU/Linux                                              
[root@archlinux ~]# neofetch                                                                                                        
                   -`                                                                                                               
                  .o+`                   --------------                                                                             
                 `ooo/                   OS: Arch Linux riscv64                                                                     
                `+oooo:                  Host: Cvitek. CV180X ASIC. C906.                                                           
               `+oooooo:                 Kernel: 5.10.4-tag-                                                                        
               -+oooooo+:                Uptime: 54 secs                                                                            
             `/:-:++oooo+:               Packages: 143 (pacman)                                                                     
            `/++++/+++++++:              Shell: bash 5.1.16                                                                         
           `/++++++++++++++:             Terminal: /dev/ttyS0                                                                       
          `/+++ooooooooooooo/`           CPU: (1)                                                                                   
         ./ooosssso++osssssso+`          Memory: 23MiB / 54MiB                                                                      
        .oossssso-````/ossssss+`                                                                                                    
       -osssssso.      :ssssssso.                                                                                                   
      :osssssss/        osssso+++.                                                                                                  
     /ossssssss/        +ssssooo/-                                                                                                  
   `/ossssso+/:-        -:/+osssso+-                                                                                                
  `+sso+:-`                 `.-/+oso:                                                                                               
 `++:.                           `-/+/                                                                                              
 .`                                 `/                                                                                              
                                                                                                                                    
[root@archlinux ~]# 
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/GIQOyBNHONziQszZ13HDhs2lP.svg)](https://asciinema.org/a/GIQOyBNHONziQszZ13HDhs2lP)

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.


> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
