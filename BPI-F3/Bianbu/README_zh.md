# Bianbu 香蕉派 BPI-F3 测试报告

## 测试环境

### 系统信息

- 系统版本：v2.0rc1
- 下载链接：https://archive.spacemit.com/image/k1/version/bianbu/v2.0rc1/
- 参考安装文档：https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### 硬件信息

- 香蕉派 BPI-F3
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像（sd 卡）


**请务必选择以 `.img.zip` 结尾的压缩包**
下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

```bash
unzip bianbu-24.04-desktop-k1-v2.0rc1-release-20240909135447.img.zip
sudo dd if=/path/to/bianbu-24.04-desktop-k1-v2.0rc1-release-20240909135447.img of=/dev/your-device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `bianbu`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/sAccZbGletHEuqNUrHYeCZkLa.svg)](https://asciinema.org/a/sAccZbGletHEuqNUrHYeCZkLa)

```log
Welcome to Bianbu 2.0rc1 (GNU/Linux 6.6.36 riscv64)

 * Documentation:  https://bianbu.spacemit.com
 * Support:        https://ticket.spacemit.com

0 updates can be applied immediately.


The programs included with the Bianbu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Bianbu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

uname -a && echo mBxJad47 
res =root@k1:~# uname -a && echo mBxJad47 
res =
Linux k1 6.6.36 #2.0~rc6.2 SMP PREEMPT Mon Sep  9 04:47:40 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
mBxJad47
res =root@k1:~# cat /etc/os-release && echo 88L1MpXg 
res =
PRETTY_NAME="Bianbu 2.0rc1"
NAME="Bianbu"
VERSION_ID="2.0rc1"
VERSION="2.0rc1 (Noble Numbat)"
VERSION_CODENAME=noble
ID=bianbu
ID_LIKE=debian
HOME_URL="https://bianbu.spacemit.com"
SUPPORT_URL="https://bianbu.spacemit.com"
BUG_REPORT_URL="https://ticket.spacemit.com"
PRIVACY_POLICY_URL="https://www.spacemit.com/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
88L1MpXg
res =root@k1:~# cat /proc/cpuinfo && echo E6oYZaZI 
res =
processor	: 0
hart		: 0
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 1
hart		: 1
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 2
hart		: 2
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 3
hart		: 3
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 4
hart		: 4
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 5
hart		: 5
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 6
hart		: 6
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 7
hart		: 7
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

E6oYZaZI
res =root@k1:~# 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功