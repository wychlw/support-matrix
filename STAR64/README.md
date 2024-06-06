# Star64

## Test Environment

### Operating System Information

**Note: Star64 can use all Visionfive2 images, but USB, Wifi, and PCI may not work (see [Bringup Notes](https://wiki.pine64.org/wiki/STAR64))**

- NuttX
    - Source code link: https://github.com/apache/nuttx
    - Installation reference: https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html
    - Toolchains:
        - Boot image: https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
        - DTB: https://github.com/starfive-tech/VisionFive2/releases
        - toolchain: https://github.com/sifive/freedom-tools/releases
        - kflash: https://github.com/kendryte/kflash.py
- Armbian
    - Download link: https://www.armbian.com/star64/
    - Installation reference: https://www.hackster.io/lupyuen/rtos-on-a-risc-v-sbc-star64-jh7110-apache-nuttx-2a7429
- Yocto
    - Download link: https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1
    - Installation reference: https://github.com/Fishwaldo/meta-pine64

### Hardware Development Board Information

- Star64

## Test Results

| Software Category         | Package Name | Test Results (Test Report)  |
|---------------------------|--------------|-----------------------------|
| NuttX Image Build and Boot | N/A          | [CFT][NuttX]                |
| Armbian Image Boot        | N/A          | [CFT][Armbian]              |
| Yocto Image Boot          | N/A          | [CFT][Yocto]                |

[NuttX]: ./NuttX/README.md
[Armbian]: ./Armbian/README.md
[Yocto]: ./Yocto/README.md

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
