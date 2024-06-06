# StarFive VisionFive

## Test Environment

### Operating System Information

- Fedora
  - Download link: [Fedora VisionFive release](https://fedora.starfivetech.com/pub/downloads/VisionFive-release/Fedora-riscv64-jh7100-developer-xfce-Rawhide-20211226-214100.n.0-sda.raw.zst)
  - Reference installation document: [VisionFive Quick Start Guide](https://doc.rvspace.org/VisionFive/PDF/VisionFive_Quick_Start_Guide.pdf)

- openEuler
  - Download link: [openEuler RISC-V preview](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive/)
  - Reference installation document: [openEuler Installation Book](https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/Visionfive)

- Ubuntu
  - Download link: [Ubuntu RISC-V](https://ubuntu.com/download/risc-v)
  - Reference installation document: [StarFive VisionFive on Ubuntu](https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive)

- openKylin
  - Download link: [openKylin old releases](https://www.openkylin.top/downloads/old_releases.html)
  - Reference installation document: [Installing openKylin on RISC-V](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

- openSUSE
  - Download link: [OpenSUSE VisionFive images](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive/images/)
  - Reference installation document: [VisionFive on openSUSE](https://en.opensuse.org/HCL:VisionFive)

- Armbian
  - Download link: [Armbian Vision Five](https://www.armbian.com/vision-five/)
  - Reference installation document: [Getting Started with Armbian](https://docs.armbian.com/User-Guide_Getting-Started/)

- OpenWRT
  - Download link: [OpenWRT VisionFive Snapshot](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive-v1)
  - Reference installation document: [OpenWRT on VisionFive](https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.starfive?s[]=visionfive)

- OpenBSD
  - Download link: [OpenBSD RISC-V snapshots](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/)
  - Reference installation document: [OpenBSD RISC-V Installation Guide](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64)

- Buildroot
  - Source code link: [Buildroot downloads](https://buildroot.org/download.html)
  - Reference installation document: [VisionFive in Buildroot repository](https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/visionfive?ref_type=heads)

### Hardware Development Board Information

- StarFive VisionFive

## Test Results

| Software Category            | Package Name | Test Result (Test Report) |
|--------------------------|--------------|---------------------------|
| openEuler/Base Image Boot  | N/A          | [Successful][oERVBase]    |
| openEuler/Xfce Image Boot  | N/A          | [Successful][oERVXfce]    |
| Fedora Image Boot          | N/A          | [Successful][Fedora] (Official Support) |
| Ubuntu Image Boot          | N/A          | [Successful][Ubuntu]     |
| openKylin Image Boot       | N/A          | [Successful][oK] (Official Support)    |
| openSUSE Image Boot        | N/A          | [Successful][openSUSE]   |
| Armbian Image Boot         | N/A          | [Successful][Armbian]    |
| OpenWRT Image Boot         | N/A          | [Successful][OpenWRT]    |
| OpenBSD Image Boot         | N/A          | [Successful][OpenBSD]    |
| Buildroot Image Build and Boot | N/A      | [Successful][Buildroot]  |

[oERVBase]: ./openEuler/README.md
[oERVXfce]: ./openEuler/README.md
[Fedora]: ./Fedora/README.md
[Ubuntu]: ./Ubuntu/README.md
[oK]: ./openKylin/README.md
[openSUSE]: ./openSUSE/README.md
[Armbian]: ./Armbian/README.md
[OpenWRT]: ./OpenWRT/README.md
[OpenBSD]: ./OpenBSD/README.md
[Buildroot]: ./BuildRoot/README.md

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
