
# Buildroot VisionFive Test Report

## Test Environment

### System Information

- System Version: Buildroot
- Source Code Link: [Buildroot Official Website](https://buildroot.org/download.html)
    - As of the writing of this document, the latest stable/LTS version of Buildroot is: [buildroot-2024.02.1](https://buildroot.org/downloads/buildroot-2024.02.1.tar.gz)
- Reference Installation Documentation: [VisionFive Board Documentation](https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/visionfive?ref_type=heads)
- Build Machine System: Arch Linux x86_64

### Hardware Information

- StarFive VisionFive (v1)
- Power Adapter
- One USB A to C or C to C cable
- One microSD card
- One USB to UART debugger

## Image Building and Flashing

Since VisionFive's Buildroot has been mainlined, obtaining the source code directly from Buildroot allows you to build a usable image.

### Setting up the Build Environment

```shell
sudo pacman -S which sed make binutils diffutils gcc bash patch gzip bzip2 perl tar cpio unzip rsync file bc findutils wget
# 或者从 AUR 安装，需要 AUR Helper，如 yay, paru 等
# paru -S buildroot-meta
```

If you are not using Arch Linux, please refer to the [official documentation](https://buildroot.org/downloads/manual/manual.html#requirement) to install the necessary dependencies (note that package names may vary).

### Building the Image

```shell
wget https://buildroot.org/downloads/buildroot-2024.02.1.tar.gz
tar xvf buildroot-2024.02.1.tar.gz
cd buildroot-2024.02.1/
make visionfive_defconfig
make -j$(nproc)
```

Note: Ensure that your internet connection is reliable as dependencies will be downloaded automatically during compilation.

After building, the `sdcard.img` image will be generated in `output/images`.

### Flashing the Image to the microSD Card

Use `dd` to write the image to the microSD card.

Here it is assumed that `/dev/sdc` is the location of the storage card.

```shell
sudo wipefs -af /dev/sdc
sudo dd if=~/buildroot-2024.02.1/output/images/sdcard.img of=/dev/sdc bs=1M status=progress oflag=direct
```

### Logging into the System

Log into the system via the serial port.

Default username: `root`

Default password: None, you will be automatically logged in after entering the username.

## Expected Outcome

The system starts up successfully and can be accessed through the onboard serial port.

## Actual Outcome

The system boots up correctly, and login through the onboard serial port is successful.

### Boot Information

```log
Welcome to Buildroot                                                                                                                
buildroot login: root                                                                                                               
# uname -a                                                                                                                          
Linux buildroot 6.0.0-visionfive #1 SMP Wed Mar 27 20:54:25 CST 2024 riscv64 GNU/Linux                                              
# starfive-drm soc:display-subsystem: [drm] Cannot find any crtc or sizes                                                           
# cat /etc/os-release                                                                                                               
NAME=Buildroot                                                                                                                      
VERSION=2024.02.1                                                                                                                   
ID=buildroot                                                                                                                        
VERSION_ID=2024.02.1                                                                                                                
PRETTY_NAME="Buildroot 2024.02.1"                                                                                                   
# 
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/jCbFkO6AUUriql5b1g7QzGuXD.svg)](https://asciinema.org/a/jCbFkO6AUUriql5b1g7QzGuXD)

## Test Criteria

Test Successful: Actual outcome matches the expected outcome.

Test Failed: Actual outcome does not match the expected outcome.

## Test Conclusion

Test Successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
