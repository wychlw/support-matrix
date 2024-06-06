# HiFive Unmatched

## Test Environment

### Operating System Information

- openEuler RISC-V 23.09 Preview
    - Download link: [openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/)
    - Reference installation document: [README.unmatched.txt](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/README.unmatched.txt)
- openKylin
    - Download link: [https://www.openkylin.top/downloads](https://www.openkylin.top/downloads)
    - Reference installation document: [RISC-V installation guide for openKylin](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)
- Ubuntu 23.10
    - Download link: [https://cdimage.ubuntu.com/releases/23.10/release/](https://cdimage.ubuntu.com/releases/23.10/release/)
    - Reference installation document: [RISC-V/SiFive%20HiFive%20Unmatched on Ubuntu Wiki](https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched)
- FreeBSD 14.0
    - Download link: [FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img.xz](https://mirrors.ustc.edu.cn/freebsd/releases/riscv/riscv64/ISO-IMAGES/14.0/FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img.xz)
    - Reference installation document: [HiFiveUnmatched on FreeBSD Wiki](https://wiki.freebsd.org/riscv/HiFiveUnmatched)
- OpenBSD 7.4
    - Download link: [install74.img](https://mirrors.tuna.tsinghua.edu.cn/OpenBSD/7.4/riscv64/install74.img)
    - Reference installation document: [INSTALL.riscv64 on OpenBSD FTP](https://ftp.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64)
- Zephyr
    - Reference installation document: [Zephyr RISC-V boards documentation](https://docs.zephyrproject.org/latest/boards/riscv/index.html)
- OpenWrt 23.05.2
    - Download link (Firmware Selector): [Firmware Selector for OpenWrt 23.05.2](https://firmware-selector.openwrt.org/?version=23.05.2&target=sifiveu%2Fgeneric&id=sifive_unmatched)
    - Reference installation document: [SiFive Unmatched hardware info on OpenWrt](https://openwrt.org/docs/techref/hardware/soc/soc.sifive)
- Debian sid
    - Download link: [debian-sid-risc-v-sifive-unmatched.tar.xz](https://people.debian.org/~deiv/riscv/debian-sid-risc-v-sifive-unmatched.tar.xz)
    - Reference installation document: [InstallingDebianOn/SiFive/HiFiveUnmatched on Debian Wiki](https://wiki.debian.org/InstallingDebianOn/SiFive/%20HiFiveUnmatched)
- OpenSUSE Tumbleweed
    - Download link: [openSUSE-Tumbleweed-RISC-V-JeOS-hifiveunmatched.riscv64-2024.03.15-Build1.7.raw.xz](https://download.opensuse.org/repositories/home:/Andreas_Schwab:/riscv:/unmatched/images/openSUSE-Tumbleweed-RISC-V-JeOS-hifiveunmatched.riscv64-2024.03.15-Build1.7.raw.xz)
    - Reference installation document: [HiFive Unmatched hardware compatibility list on openSUSE](https://en.opensuse.org/HCL:HiFive_Unmatched)

### Hardware Development Board Information

- HiFive Unmatched

## Test Results

| Software Category           | Package Name | Test Result (Test Report) |
|---------------------------|--------------|-------------------------|
| Debian Image Boot           | N/A          | [Success][Debian]            |
| openEuler/Base Image Boot   | N/A          | [Success][oERV]              |
| openEuler/Xfce Image Boot   | N/A          | [Success][oERV]              |
| openKylin Image Boot        | N/A          | [Success][oK] (Official Support) |
| OpenSUSE Image Boot         | N/A          | [Success][SUSE]              |
| Ubuntu Image Boot           | N/A          | [Success][Ubuntu] (Official Support) |
| FreeBSD Image Boot          | N/A          | [Success][FreeBSD] (Official Support) |
| OpenBSD Image Boot          | N/A          | [Success][OpenBSD] (Official Support) |
| Zephyr Boot                 | N/A          | [Success][Zephyr] (Official Support) |
| OpenWrt Boot                | N/A          | [Success][OpenWrt] (Official Support) |

[Debian]: ./Debian/README.md
[oERV]: ./openEuler/README.md
[oK]: ./openKylin/README.md
[SUSE]: ./OpenSUSE/README.md
[Ubuntu]: ./Ubuntu/README.md
[FreeBSD]: ./FreeBSD/README.md
[OpenBSD]: ./OpenBSD/README.md
[Zephyr]: ./Zephyr/README.md
[OpenWrt]: ./OpenWrt/README.md

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
