# Arch Linux LicheeRV / AWOL Nezha D1 Test Report

## Test Environment

### Operating System Information

- System Version: Initial Release
- Packaging Script: https://github.com/sehraf/d1-riscv-arch-image-builder

### Hardware Information

- Nezha D1
- Type-C Power Cable x1
- UART to USB Debugger x1
- SD Card

## Installation Steps

### Using Packaging Script

To install dependencies for Archlinux, use the following:
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```


A community script has been created for automatic packaging of Arch Linux. If you wish to use it, you can skip all the installation processes below.

Clone the corresponding repository:
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
```

Modify the `DEVICE_TREE` in `consts.sh` according to the specific board, for example, for Lichee RV:
```diff
diff --git a/consts.sh b/consts.sh
index 11e51cd..0b990ad 100644
--- a/consts.sh
+++ b/consts.sh
@@ -25,7 +25,7 @@ export KERNEL='defconfig'
 # sun20i-d1-lichee-rv
 # sun20i-d1-mangopi-mq-pro
 # sun20i-d1-nezha
-export DEVICE_TREE=sun20i-d1-lichee-rv-dock
+export DEVICE_TREE=sun20i-d1-lichee-rv
 
 # folder to mount rootfs
 export MNT="${PWD}/mnt"

```

Run `1_compile.sh` to compile the image;
Run `2_create_sd.sh /dev/your/device` to write to the SD card.

Note: If it automatically configures the rootfs, you will need: `arch-install-scripts`, `qemu-user-static-bin (AUR)`, `binfmt-qemu-static (AUR)`. If this step is not needed, you can set `USE_CHROOT` to 0 in `consts.sh`.

```bash
./1_compile.sh
./2_create_sd.sh /dev/your/device
```

**If USE_CHROOT is enabled (enabled by default), it will automatically chroot into the image for configuration later. It is recommended to install basic applications like vim at this step.**

### Login to the System

Log in to the system via serial console.

Default username: `root`
Default password: `archriscv`

## Expected Results

The system should start up normally, allowing login via the onboard serial console.

## Actual Results

The system starts up normally, successfully allowing login via the onboard serial console.

### Boot Information

Screen recording (from flashing the image to logging into the system):
[![asciicast](https://asciinema.org/a/D86o9kqp6phQBswrEEBt4rwyv.svg)](https://asciinema.org/a/D86o9kqp6phQBswrEEBt4rwyv)

```log
Arch Linux 6.8.0 (ttyS0)

licheerv login: root
Password: 
[root@licheerv ~]# neofetch
                   -`                                                                                                      
                  .o+`                   ------------- 
                 `ooo/                   OS: Arch Linux riscv64 
                `+oooo:                  Host: Allwinner D1 Nezha 
               `+oooooo:                 Kernel: 6.8.0 
               -+oooooo+:                Uptime: 1 min 
             `/:-:++oooo+:               Packages: 119 (pacman) 
            `/++++/+++++++:              Shell: bash 5.2.26 
           `/++++++++++++++:             Terminal: /dev/ttyS0 
          `/+++ooooooooooooo/`           CPU: (1) 
         ./ooosssso++osssssso+`          Memory: 55MiB / 970MiB 
        .oossssso-````/ossssss+`
       -osssssso.      :ssssssso.                                
      :osssssss/        osssso+++.                               
     /ossssssss/        +ssssooo/-
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+/
 .`                                 `/

[root@licheerv ~]# 

```

## Test Criteria

Successful Test: The actual results match the expected results.

Failed Test: The actual results do not match the expected results.

## Test Conclusion

Successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
