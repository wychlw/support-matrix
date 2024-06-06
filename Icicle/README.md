# Microchip Polarfire SoC FPGA Icicle Kit

## Test Environment

### Operating System Information

- Ubuntu 24.04
    - Download Link: [Ubuntu 24.04](https://cdimage.ubuntu.com/releases/24.04/release/)
    - Installation Guide: [RISC-V/PolarFire SoC FPGA Icicle Kit](https://wiki.ubuntu.com/RISC-V/PolarFire%20SoC%20FPGA%20Icicle%20Kit)
- BuildRoot 24.02.2
    - Source Code Download: [BuildRoot 24.02.2](https://buildroot.org/downloads/buildroot-2024.02.2.tar.gz)
    - Installation Guide: [BuildRoot Microchip MPFS Icicle](https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/microchip/mpfs_icicle?ref_type=heads)
- OpenEmbedded / Yocto
    - Download Link: [PolarFire SoC Yocto BSP](https://github.com/polarfire-soc/meta-polarfire-soc-yocto-bsp)
    - Installation Guide: [PolarFire SoC Yocto BSP](https://github.com/polarfire-soc/meta-polarfire-soc-yocto-bsp)
- Arch Linux
    - Download Link: [Arch Linux for RISC-V](https://archriscv.felixc.at/)
    - Installation Guide: [Newbies PolarFire SoC Icicle Kit First Experience](https://felixc.at/2022/06/newbies-polarfire-soc-icicle-kit-first-experience)
- OpenBSD
    - Download Link: [OpenBSD RISC-V64 Snapshots](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/)
    - Installation Guide: [OpenBSD RISC-V64 Installation](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64)
- FreeRTOS
    - Installation Guide: [Building the Linux & FreeRTOS & BM Demo](https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/applications-and-demos/asymmetric-multiprocessing/amp.md#building-the-linux--freertos--bm-demo)
- Zephyr
    - Installation Guide: [Microchip MPFS Icicle Zephyr Board Documentation](https://docs.zephyrproject.org/latest/boards/microchip/mpfs_icicle/doc/index.html)
- NuttX
    - Installation Guide: [RISC-V MPFS Platform](https://nuttx.apache.org/docs/latest/platforms/risc-v/mpfs/index.html)

### Hardware Development Board Information

- Microchip Polarfire SoC FPGA Icicle Kit

## Test Results



| Software Category         | Package Name | Test Results (Test Report)       |
|--------------------------|--------------|----------------------------------|
| Ubuntu Image Boot        | N/A          | [Basic][Ubuntu] (Official Support)|
| Yocto Image Build and Boot| N/A         | [Basic][Yocto]                   |
| BuildRoot Image Boot      | N/A          | [Basic][BuildRoot]               |
| Arch Linux Boot           | N/A          | [CFT][Arch]                      |
| OpenBSD Image Boot        | N/A          | [CFT][OpenBSD]                    |
| FreeRTOS Image Build and Boot| N/A       | [CFT][FreeRTOS]                  |
| Zephyr Image Build and Boot | N/A        | [CFT][Zephyr]                    |
| NuttX Image Build and Boot   | N/A        | [CFT][NuttX]                      |


[Ubuntu]: ./Ubuntu/README.md
[BuildRoot]: ./BuildRoot/README.md
[Yocto]: ./Yocto/README.md
[Arch]: ./ArchLinux/README.md
[OpenBSD]: ./OpenBSD/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[Zephyr]: ./Zephyr/README.md
[NuttX]: ./NuttX/README.md

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
