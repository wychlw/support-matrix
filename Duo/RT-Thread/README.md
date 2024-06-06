# RT-Thread Milk-V Duo Test Report

## Test Environment

### Operating System Information

- Build System Version: Ubuntu 20.04 LTS x86_64
- System Version: RT-Thread 5.1.0, commit [3ff4fe5](https://github.com/RT-Thread/rt-thread/commit/3ff4fe5395516eb734b2cead9cc50f35e54f6511)
- Source Code Link: https://github.com/RT-Thread/rt-thread
- Installation Reference Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek/cv1800b

### Hardware Information

- Milk-V Duo 64M
- One USB power adapter
- One USB-A to C or USB C to C cable
- One microSD card
- One USB to UART debugger (e.g. CH340, CH341, FT2232, etc.)
- Three DuPont wires
- Debug pins pre-soldered on the Milk-V Duo main body

## Building Steps

### Prepare System Environment

Please note, use Ubuntu 20.04, as building may fail on updated system versions.

You can use container environments like Docker for building.

Install dependencies:

```shell
sudo apt update && sudo apt install -y git gcc build-essential scons libncurses5-dev python3 python3-requests curl
```

Obtain the toolchain:

```shell
curl -LO https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
tar xvf riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
export RTT_EXEC_PATH=~/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu/bin
```

### Clone Source Code and Compile Firmware

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv1800b
# Generate config file
scons --menuconfig
source ~/.env/env.sh
scons -j$(nproc) --verbose
cd ../
bash combine-fip.sh
```

After execution, two files, boot.sd and fip.bin, will be generated in the `cvitek` directory.

### Prepare microSD Card

Clear the microSD card (you can use `wipefs -af /path/to/your-card`), and create a FAT32 partition.

Copy the generated boot.sd and fip.bin into the microSD card. At this point, the memory card is ready to boot RT-Thread on the Duo.

### Log into the System

Log into the system via serial port.

## Expected Results

The system boots up successfully and allows login via the serial port.

## Actual Results

The system boots up properly and login via the serial port is successful.

### Boot Information

```log
Boot from SD ...                                                                                                                    
switch to partitions #0, OK                                                                                                         
mmc0 is current device                                                                                                              
173704 bytes read in 10 ms (16.6 MiB/s)                                                                                             
## Loading kernel from FIT Image at 81400000 ...                                                                                    
   Using 'config-cv1800b_milkv_duo_sd' configuration                                                                                
   Trying 'kernel-1' kernel subimage                                                                                                
   Verifying Hash Integrity ... crc32+ OK                                                                                           
## Loading fdt from FIT Image at 81400000 ...                                                                                       
   Using 'config-cv1800b_milkv_duo_sd' configuration                                                                                
   Trying 'fdt-cv1800b_milkv_duo_sd' fdt subimage                                                                                   
   Verifying Hash Integrity ... sha256+ OK                                                                                          
   Booting using the fdt blob at 0x814255c4                                                                                         
   Uncompressing Kernel Image                                                                                                       
   Decompressing 424720 bytes used 58ms                                                                                             
   Loading Device Tree to 0000000081be5000, end 0000000081becb60 ... OK                                                             
                                                                                                                                    
Starting kernel ...                                                                                                                 
                                                                                                                                    
heap: [0x8029be68 - 0x8129be68]                                                                                                     
                                                                                                                                    
 \ | /                                                                                                                              
- RT -     Thread Smart Operating System                                                                                            
 / | \     5.1.0 build Mar 26 2024 05:52:37                                                                                         
 2006 - 2024 Copyright by RT-Thread team                                                                                            
Hello RT-Smart!                                                                                                                     
msh />  
```

Screen recording (from flashing image to system login):

[![asciicast](https://asciinema.org/a/gbDJeUr3mdHNxd3mXev7UpBGl.svg)](https://asciinema.org/a/gbDJeUr3mdHNxd3mXev7UpBGl)

## Test Judgment Criteria

Test Success: Actual results match the expected results.

Test Failure: Actual results do not match the expected results.

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
