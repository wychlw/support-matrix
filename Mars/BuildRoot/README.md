
# BuildRoot on Milk-V Mars

## Test Environment

### Operating System Information

- BuildRoot
  - Source Code Link: https://github.com/milkv-mars/mars-buildroot-sdk
  - Reference Installation Document: https://github.com/milkv-mars/mars-buildroot-sdk
- Build System Environment: Ubuntu 22.04.4 LTS in Docker

### Hardware Information

- Milk-V Mars
- One USB to UART Debugger
- Three DuPont wires
- One USB A to C or C to C cable
- One USB power supply
- Wired network connection

## Installation Steps

### Build Image

Note: Due to the older version of BuildRoot provided, if there are SHA errors or 404 during the build process, try updating the SHA256SUM manually or the download link. You can find the latest BuildRoot on [BuildRoot](https://github.com/buildroot/buildroot) and replace the corresponding parts under buildroot/package.
(You can also try directly replacing it with the latest BuildRoot)

Install build dependencies:

```shell
sudo apt update
sudo apt install -y build-essential automake libtool texinfo bison flex gawk \
g++ git xxd curl wget gdisk gperf cpio bc screen texinfo unzip libgmp-dev \
libmpfr-dev libmpc-dev libssl-dev libncurses-dev libglib2.0-dev libpixman-1-dev \
libyaml-dev patchutils python3-pip zlib1g-dev device-tree-compiler dosfstools \
mtools kpartx rsync libcap-dev
```

Fetch the source code:

```shell
git clone https://github.com/milkv-mars/mars-buildroot-sdk.git --depth=1
```

Checkout to the corresponding branch for the device:

- Mars
  ```
  git checkout dev
  ```

- Mars CM eMMC
  ```
  git checkout dev-mars-cm
  ```

- Mars CM SD Card
  ```
  git checkout dev-mars-cm-sdcard
  ```

Start the compilation:

```shell
make -j$(nproc)
```

**This process takes a long time, please be patient**

After compilation, the following image will be generated in the work directory:

```
work/
├── visionfive2_fw_payload.img
├── image.fit
├── initramfs.cpio.gz
├── u-boot-spl.bin.normal.out
├── linux
    ├── arch/riscv/boot
    │   ├── dts
    │   │   └── starfive
    │   │       ├── jh7110-milkv-mars-cm-emmc.dtb
    │   │       ├── jh7110-milkv-mars-cm-sdcard.dtb
    │   │       ├── jh7110-milkv-mars.dtb
    │   │       ├── jh7110-visionfive-v2-ac108.dtb
    │   │       ├── jh7110-visionfive-v2.dtb
    │   │       ├── jh7110-visionfive-v2-wm8960.dtb
    │   │       ├── vf2-overlay
    │   │       │   └── vf2-overlay-uart3-i2c.dtbo
    │   └── Image.gz
    └── vmlinuz-5.15.0
```

**This process takes a long time**

### Build SD Card Image

Continue to build the SD card image:
```bash
make buildroot_rootfs -j$(nproc)
make img
```

Note: If encountering build issues like libfakeroot, replace the related package with a newer one from BuildRoot (including patches) will resolve it.

### Write SD Card

Burn the image just built onto the SD card:
```bash
sudo dd if=work/sdcard.img of=/dev/sdX bs=4096
sync
```

### Log into the System

If booting via network directly, put the files into TFTP, then:

Connect the serial port and wired network, power up Mars.

Interrupt the boot process by pressing any key when U-Boot prompts `Hit any key to stop autoboot`, then run the TFTP server on your computer.

```
dhcp; setenv serverip xxx.xxx.xxx.xxx;
tftpboot ${fdt_addr_r} jh7110-milkv-mars.dtb;
tftpboot ${kernel_addr_r} Image.gz;
tftpboot ${ramdisk_addr_r} initramfs.cpio.gz;
run chipa_set_linux;run cpu_vol_set;
booti ${kernel_addr_r} ${ramdisk_addr_r}:${filesize} ${fdt_addr_r}
```

Username: `root`

Password: `starfive`

## Expected Outcome

The image is successfully built, the system starts up correctly, and can be logged into via the onboard serial port.

## Actual Outcome

The system starts up correctly and can be logged into via the onboard serial port.

### Boot Information

Screen recording:
[![asciicast](https://asciinema.org/a/uweoEDTIkJplZk2LZwK3KVwhn.svg)](https://asciinema.org/a/uweoEDTIkJplZk2LZwK3KVwhn)

```log
Welcome to Buildroot
buildroot login: root
Password: 
# cat /etc/os-
cat: can't open '/etc/os-': No such file or directory
# cat /etc/os-release 
NAME=Buildroot
VERSION=2021.11
ID=buildroot
VERSION_ID=2021.11
PRETTY_NAME="Buildroot 2021.11"
# uname -a
Linux buildroot 5.15.0 #1 SMP Tue May 28 17:36:13 CST 2024 riscv64 GNU/Linux


```

## Test Judgment Criteria

Test Successful: Actual outcome matches the expected outcome.

Test Failed: Actual outcome does not match the expected outcome.

## Test Conclusion

Success

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
