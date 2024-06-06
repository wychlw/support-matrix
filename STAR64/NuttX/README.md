# NuttX Star64 Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/apache/nuttx
- Installation Reference Document: https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html
- Toolchains:
    - Boot Image: https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
    - DTB: https://github.com/starfive-tech/VisionFive2/releases
    - Toolchain: https://github.com/sifive/freedom-tools/releases
    - kflash: https://github.com/kendryte/kflash.py

### Hardware Information

- Development Board: Star64
- USB A to C / USB C to C Cables
- SD Card

## Installation Steps

### Prepare Source Code and Environment

Obtain Toolchains:
```bash
wget https://static.dev.sifive.com/dev-tools/freedom-tools/v2020.12/riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
tar -xvzf riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
export PATH=path/to/toolchain/bin:$PATH
```

Clone the repository and configure:
```bash
mkdir nuttx && cd nuttx
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps.git apps
```

### Build NuttX

Compile nuttx.bin:
```bash
cd nuttx
make distclean
./tools/configure.sh star64:nsh
make -j$(nproc)
riscv64-unknown-elf-objcopy -O binary nuttx nuttx.bin
```

Build the file system:
```bash
make export
pushd ../apps
tools/mkimport.sh -z -x ../nuttx/nuttx-export-*.tar.gz
make import
popd
genromfs -f initrd -d ../apps/bin -V "NuttXBootVol"
```

Write the dtb file:
- Download the dtb file:
```bash
wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/jh7110-visionfive-v2.dtb
```
- Inside the nuttx folder:
```bash
cat << EOF > nuttx.its
/dts-v1/;

/ {
  description = "NuttX FIT image";
  #address-cells = <2>;

  images {
    vmlinux {
      description = "vmlinux";
      data = /incbin/("./nuttx.bin");
      type = "kernel";
      arch = "riscv";
      os = "linux";
      load = <0x0 0x40200000>;
      entry = <0x0 0x40200000>;
      compression = "none";
    };

    ramdisk {
      description = "buildroot initramfs";
      data = /incbin/("./initrd");
      type = "ramdisk";
      arch = "riscv";
      os = "linux";
      load = <0x0 0x46100000>;
      compression = "none";
      hash-1 {
        algo = "sha256";
      };
    };

    fdt {
      data = /incbin/("./jh7110-visionfive-v2.dtb");
      type = "flat_dt";
      arch = "riscv";
      load = <0x0 0x46000000>;
      compression = "none";
      hash-1 {
        algo = "sha256";
      };
    };
  };

  configurations {
    default = "nuttx";

    nuttx {
      description = "NuttX";
      kernel = "vmlinux";
      fdt = "fdt";
      loadables = "ramdisk";
    };
  };
};
EOF
```

Ensure u-boot-tools are installed on your system:
```bash
# sudo apt install u-boot-tools
# sudo pacman -S uboot-tools
# sudo dnf install u-boot-tools
```

Create a fit:
```bash
mkimage -f nuttx.its -A riscv -O linux -T flat_dt starfiveu.fit
```

### Build Image

Download the SD card image and burn it:
```bash
wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
sudo dd if=sdcard.img of=/dev/your/device bs=1M status=progress
```

### Burn Image

Burn the SBI environment on the SD card:
```bash
unxz -k canmv230-sdcard.img.xz
sudo dd if=canmv230-sdcard.img of=/dev/your/sdcard bs=1M status=progress
```

Replace the fit file:
```bash
mkdir mnt
sudo mount /dev/your/sdcard/p3 mnt
sudo cp starfiveu.fit mnt/
sudo umount mnt
rm -r mnt
```

### Login to the System

Connect to the development board via a serial port.

## Expected Results

Successful build with the development board displaying normal boot messages.

## Actual Results

Successful build with the development board displaying normal boot messages.

### Boot Messages

Screen recording (from system flashing to booting):

```log
```

## Test Verdict Criteria

Successful Test: Actual results match expected results.

Failed Test: Actual results do not match expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
