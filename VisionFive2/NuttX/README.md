# NuttX VisionFive 2 Test Report

## Test Environment

### Operating System Information

- Source Code Link: [https://github.com/apache/nuttx](https://github.com/apache/nuttx)
- Reference Installation Documentation: [https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html](https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html)
- Toolchains:
    - Boot Image: [https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img](https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img)
    - DTB: [https://github.com/starfive-tech/VisionFive2/releases](https://github.com/starfive-tech/VisionFive2/releases)
    - Toolchain: [https://github.com/sifive/freedom-tools/releases](https://github.com/sifive/freedom-tools/releases)
    - kflash: [https://github.com/kendryte/kflash.py](https://github.com/kendryte/kflash.py)

### Hardware Information

- Development Board: VisionFive 2
- USB A to C / USB C to C Cables
- SD Card

## Installation Steps

### Prepare Source Code and Environment

Obtain the toolchains:
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
- Download dtb:
```bash
wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/jh7110-visionfive-v2.dtb
``` 
- Perform the following steps in the nuttx folder:
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

Ensure that u-boot-tools are installed on your system:
```bash
# sudo apt install u-boot-tools
# sudo pacman -S uboot-tools
# sudo dnf install u-boot-tools
```

Create fit:
```bash
mkimage -f nuttx.its -A riscv -O linux -T flat_dt starfiveu.fit
```

### Build Image

Download the SD card image and flash it:
```bash
wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
sudo dd if=sdcard.img of=/dev/your/device bs=1M status=progress
```

### Flash Image

Flash the SBI environment on the SD card:
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

### Access the System

Connect to the development board via serial port.

## Expected Results

Successful build with normal boot output on the development board.

## Actual Results

Successful build with normal boot output on the development board.

### Boot Information

Screen recording (from system flashing to booting):
[![asciicast](https://asciinema.org/a/boXeQ4xPfJgGjsJPZeT00uMH0.svg)](https://asciinema.org/a/boXeQ4xPfJgGjsJPZeT00uMH0)

```log
ABC                                                                       
NuttShell (NSH) NuttX-12.5.1                                              
nsh> cat /proc/version                                                    
NuttX version 12.5.1 6e941aed8b May  7 2024 11:25:17 star64:nsh           
nsh> 
```

## Test Judgement Criteria

Test Success: Actual results match the expected results.

Test Failure: Actual results do not match the expected results.

## Test Conclusion

Test Successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
