# Ubuntu 24.04.1 LTS D1 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 24.04.1 LTS
- 下载链接：https://ubuntu.com/download/risc-v
    - 或者镜像站：[Nezha](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.04.1/release/ubuntu-24.04.1-preinstalled-server-riscv64%2Bnezha.img.xz) | [Lichee RV](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.04.1/release/ubuntu-24.04.1-preinstalled-server-riscv64%2Blicheerv.img.xz)

- 参考安装文档：https://wiki.ubuntu.com/RISC-V/LicheeRV

### 硬件信息

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 将镜像写入至 microSD 卡。

### 登录系统

通过串口登录系统。

默认用户名：`ubuntu`
默认密码：`ubuntu`

初次登录时，系统会提示更改密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。
<details>
<summary>结果已过时（beta 版）</summary>
### 启动信息

```log

New password: 
Retype new password: 
uname -a && echo pFANgBWl 
Welcome to Ubuntu Oracular Oriole (development branch) (GNU/Linux 6.8.0-31-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Thu Sep 19 03:13:06 UTC 2024

  System load:    1.15      Processes:             27
  Usage of /home: unknown   Users logged in:       0
  Memory usage:   5%        IPv4 address for eth0: 10.10.10.2
  Swap usage:     0%

0 updates can be applied immediately.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ uname -a && echo pFANgBWl 

Linux ubuntu 6.8.0-31-generic #31.1-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr 21 01:12:53 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
pFANgBWl
ubuntu@ubuntu:~$ cat /etc/os-release && echo 6wiXKfwS 

PRETTY_NAME="Ubuntu Oracular Oriole (development branch)"
NAME="Ubuntu"
VERSION_ID="24.10"
VERSION="24.10 (Oracular Oriole)"
VERSION_CODENAME=oracular
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=oracular
LOGO=ubuntu-logo
6wiXKfwS
ubuntu@ubuntu:~$ cat /proc/cpuinfo && echo zaKdnCxp 

processor	: 0
hart		: 0
isa		: rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu		: sv39
uarch		: thead,c906
mvendorid	: 0x5b7
marchid		: 0x0
mimpid		: 0x0
hart isa	: rv64imafdc_zicntr_zicsr_zifencei_zihpm

zaKdnCxp
ubuntu@ubuntu:~$ 
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/r9ivCdzlZAGbyuz1SjpnZEJx3.svg)](https://asciinema.org/a/r9ivCdzlZAGbyuz1SjpnZEJx3)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。
10
## 测试结论

测试成功。
</details>