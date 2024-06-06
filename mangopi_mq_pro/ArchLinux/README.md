# Archlinux MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download links:
    - Image Builder: https://github.com/sehraf/d1-riscv-arch-image-builder
    - U-Boot: https://github.com/smaeul/u-boot.git
    - RootFS: https://archriscv.felixc.at
- Reference installation guide: https://github.com/sehraf/d1-riscv-arch-image-builder

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Install Dependencies

To install dependencies using Archlinux, follow the steps below:
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```

### Choose dtb File

After downloading the builder, modify `consts.sh`:
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
vim consts.sh
```

Choose dtb:
```diff
diff --git a/consts.sh b/consts.sh
index 11e51cd..6fc61d5 100644
--- a/consts.sh
+++ b/consts.sh
@@ -25,7 +25,7 @@ export KERNEL='defconfig'
 # sun20i-d1-lichee-rv
 # sun20i-d1-mangopi-mq-pro
 # sun20i-d1-nezha
-export DEVICE_TREE=sun20i-d1-lichee-rv-dock
+export DEVICE_TREE=sun20i-d1-mangopi-mq-pro
 
 # folder to mount rootfs
 export MNT="${PWD}/mnt"

```

### Generate Image

Run `1_compile.sh`:
```bash
./1_compile.sh
```

### Write Image

Run `2_create_sd.sh`:

```bash
2_create_sd.sh /dev/your/device
```

### Log In to System

Log in to the system via serial port.

Default username: `root`
Default password: `archriscv`

## Expected Outcome

The system should boot up successfully, allowing login via the onboard serial port.

## Actual Outcome

The system boots up successfully, and login via the onboard serial port is achieved.

### Boot Information

Screen recording (from writing image to logging into the system):

```log
```

## Test Criteria

Test Success: Actual outcome matches the expected outcome.

Test Failure: Actual outcome does not match the expected outcome.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
