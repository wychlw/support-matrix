# StarFive VisionFive 2

## Test Environment

### Operating System Information

- openEuler RISC-V 23.09 Preview
    - Download Link: [Here](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive2/)
    - Installation Guide: [Here](https://gitee.com/openeuler/RISC-V/blob/master/release/openEuler-23.03/Installation_Book/Visionfive2/README.md)
- Debian (Official)
    - Download Link: [Here](https://debian.starfivetech.com/)
- openKylin
    - Download Link: [Here](https://www.openkylin.top/downloads)
    - Installation Guide: [Here](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)
- Ubuntu 23.10
    - Download Link: [Here](https://cdimage.ubuntu.com/releases/23.10/release/)
    - Installation Guide: [Here](https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive%202)
- BuildRoot (VisionFive 2 SDK)
    - Download Link: [Here](https://github.com/starfive-tech/VisionFive2/releases)
    - Installation Guide: [Here](https://github.com/starfive-tech/VisionFive2)
- Arch Linux
    - Download Link: [Here](https://github.com/cwt-vf2/archlinux-image-vf2/releases/tag/cwt21.1)
    - Installation Guide: [Here](https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459)
- Gentoo
    - Download Link: [Here](https://drive.google.com/file/d/10TDsk2FwZDJv3yJvDAfCam5Wf9ibS6Eg/view?usp=sharing)
    - Installation Guide: [Here](https://forum.rvspace.org/t/experimental-gentoo-image/1807)
- openSUSE
    - Download Link: [Here](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/)
    - Installation Guide: [Here](https://en.opensuse.org/HCL:VisionFive2)
- OpenBSD
  - Download Link: [Here](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/)
  - Installation Guide: [Here](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64)
- Armbian Noble Minimal & Armbian Jammy Xfce
    - Download Link: [Here](https://www.armbian.com/visionfive2/)
    - Installation Guide: [Here](https://www.armbian.com/visionfive2/)
- OpenWrt SNAPSHOT
    - Download Link: [Here](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive2-v1.3b)
    - Installation Guide: [Here](https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html)
- RT-Thread
    - Source Code Link: [Here](https://github.com/starfive-tech/VisionFive2)
    - Installation Guide: [Here](https://doc.rvspace.org/VisionFive2/Application_Notes/RT-Thread/index.html)
- Zephyr
    - Installation Guide: [Here](https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html)

### Hardware Development Board Information

- StarFive VisionFive 2

## Test Results

| Software Category         | Software Package | Test Result (Test Report)               |
|------------------------|------------------|-------------------------------------|
| openEuler/Base Image Boot | N/A            | [Success][oERV]                      |
| openEuler/Xfce Image Boot | Xfce           | [Success][oERV]                      |
| Debian Image Boot         | N/A            | [Success][Debian] (StarFive OEM Image) |
| openKylin Image Boot       | N/A            | [Success][oK] (Official Support)      |
| Ubuntu Image Boot         | N/A            | [Success][Ubuntu] (Official Support)  |
| BuildRoot Image Boot      | N/A            | [Success][BuildRoot] (StarFive OEM Image) |
| Arch Linux Image Boot     | N/A            | [Success][Arch]                      |
| Gentoo Image Boot         | N/A            | [Success][Gentoo]                    |
| openSUSE Image Boot       | N/A            | [Success][SUSE] (Official Support)    |
| OpenBSD Image Boot        | N/A            | [Success][OpenBSD]                   |
| Armbian/Minimal Image Boot | N/A           | [Success][Armbian]                   |
| Armbian/Xfce Image Boot    | Xfce           | [Success][Armbian]                   |
| OpenWrt Image Boot        | N/A            | [Success][OpenWrt]                   |
| RT-Thread Image Build and Boot | N/A       | [Success][RT-Thread] (Official Support) |
| Zephyr Image Build and Boot    | N/A       | [Failure][Zephyr]                    |
| NuttX Image Build and Boot      | N/A       | [Success][NuttX]                     |

[oERV]: ./openEuler/README.md
[Debian]: ./Debian/README.md
[oK]: ./openKylin/README.md
[Ubuntu]: ./Ubuntu/README.md
[BuildRoot]: ./BuildRoot/README.md
[Arch]: ./ArchLinux/README.md
[Gentoo]: ./Gentoo/README.md
[openSUSE]: ./openSUSE/README.md
[OpenBSD]: ./OpenBSD/README.md
[Armbian]: ./Armbian/README.md
[OpenWrt]: ./WRT/README.md
[RT-Thread]: ./RT-Thread/README.md
[Zephyr]: ./Zephyr/README.md
[NuttX]: ./NuttX/README.md

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
