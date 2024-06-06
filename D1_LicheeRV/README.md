# LicheeRV / AWOL Nezha D1

## Test Environment

### Operating System Information

- openEuler RISC-V 23.03 Preview
  - Download Link: [ISCAS Mirror][oERVDL]
    - Choose between an image with Xfce desktop or a Base image with command line only
  - Installation Reference: [openEuler/RISC-V][oERVXfce]
- Tina Linux
  - Download Links:
    - Nezha D1: https://d1.docs.aw-ol.com/source/3_getimg/
    - Sipeed Lichee RV: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
  - Installation Reference:
    - Nezha D1: https://d1.docs.aw-ol.com/study/study_1tina/
    - Sipeed Lichee RV: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
- Ubuntu
  - Download Link: https://ubuntu.com/download/risc-v
  - Installation Reference:
    - Nezha D1: https://wiki.ubuntu.com/RISC-V/Nezha%20D1
    - Sipeed Lichee RV Dock: https://wiki.ubuntu.com/RISC-V/LicheeRV
- OpenWrt
  - Download Links (OpenWrt Firmware Selector):
    - Nezha D1: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=nezha
    - Sipeed Lichee RV Dock: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=lichee_rv_dock
  - Installation Reference: https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1
- Debian
  - Download Link: http://www.perfxlab.cn:8080/rvboards/
  - Installation Reference: https://d1.docs.aw-ol.com/strong/strong_4debian/#v041
- Fedora
  - Download Link: https://openkoji.iscas.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/
  - Installation Reference: https://fedoraproject.org/wiki/Architectures/RISC-V/Allwinner/zh-cn
- Arch Linux
  - Packaging Script: https://github.com/sehraf/d1-riscv-arch-image-builder

### Hardware Development Board Information

- Sipeed Lichee RV Dock
- AWOL Nezha D1

## Test Results

| Software Category              | Software Name | Test Result (Test Report)    |
|----------------------------|--------------|---------------------------|
| openEuler/Base Image Boot       | N/A          | [Success][oERV]                |
| openEuler/Xfce Image Boot       | Xfce Desktop | [Success][oERV]                |
| Tina-Linux Image Boot - Nezha D1 | N/A          | [Success][TinaNezha] (Official Support) |
| Ubuntu Image Boot               | N/A          | [Success][Ubuntu] (Official Support)    |
| OpenWrt Image Boot              | N/A          | [Success][OpenWrt] (Official Support)   |
| Debian Image Boot               | N/A          | [Success][Debian]              |
| Fedora Image Boot               | N/A          | [Success][Fedora]              |
| openSUSE Image Boot             | N/A          | [Success][openSUSE]            |
| Arch Linux Image Boot           | N/A          | [Success][Arch]                |

[oERVDL]: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/
[oERV]: ./openEuler/README.md
[TinaNezha]: https://d1.docs.aw-ol.com/study/study_1tina/
[Ubuntu]: ./Ubuntu/README.md
[OpenWrt]: ./OpenWrt/README.md
[Debian]: ./Debian/README.md
[Fedora]: ./Fedora/README.md
[openSUSE]: ./openSUSE/README.md
[Arch]: ./ArchLinux/README.md

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
