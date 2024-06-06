# Arch Linux DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- System Version: Initial Release
- Packaging Script: https://github.com/sehraf/d1-riscv-arch-image-builder

### Hardware Information

- DongshanPI-Nezha ST
- One Type-C power cable
- One UART to USB debugger
- SD card

## Installation Steps

### Using the Packaging Script

Install the dependencies for Archlinux as follows:
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```


The community has created an automated packaging script for Arch Linux. If you wish to use it, you can skip all the installation processes below.

Clone the respective repository:
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
```

Modify the `DEVICE_TREE` in `consts.sh` according to the specific board, for example:
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
+export DEVICE_TREE=sun20i-d1-dongshan-nezha-stu
 
 # folder to mount rootfs
 export MNT="${PWD}/mnt"

```

Run `1_compile.sh` to compile the image;
Run `2_create_sd.sh /dev/your/device` to burn it to the SD card.

Note: If it automatically configures the rootfs, you will need: `arch-install-scripts`, `qemu-user-static-bin (AUR)`, `binfmt-qemu-static (AUR)`. If this step is not needed, you can set `USE_CHROOT` to 0 in `consts.sh`.

```bash
./1_compile.sh
./2_create_sd.sh /dev/your/device
```

**If USE_CHROOT is enabled (enabled by default), it will automatically chroot into the image for configuration later. It is recommended to install basic applications such as vim at this stage.**


### Logging into the System

Log into the system via serial port.

Default username: `root`
Default password: `archriscv`

## Expected Results

The system starts up normally and can be logged into via the onboard serial port.

## Actual Results

The system starts up normally and successfully logs in via the onboard serial port.

### Boot Information

Screen recording (from flashing the image to logging into the system):

```log

```

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
