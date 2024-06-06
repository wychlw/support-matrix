# Fedora 36 D1 Test Report

## Test Environment

### System Information

- System Version: Fedora 36
- Download Link: [https://openkoji.iscas.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/](https://openkoji.iscas.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/)
- Reference Installation Document: [https://fedoraproject.org/wiki/Architectures/RISC-V/Allwinner/zh-cn](https://fedoraproject.org/wiki/Architectures/RISC-V/Allwinner/zh-cn)

### Hardware Information

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- Power Adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Flash Image

Use `unzstd` to decompress the image.
Format your SD card.
Use `dd` to write the image to the microSD card.

```bash
unzstd /path/to/fedora.raw.zst
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/fedora.raw of=/dev/your_device bs=1M status=progress
```

### System Login

*The system boots up slowly.*

Log in to the system via serial port.

Default username: `root`
Default password: `riscv`

## Expected Results

The system should boot up successfully and allow login via the onboard serial port.

## Actual Results

The system booted up successfully, logged in via the onboard serial port, and accessed the desktop.

### Boot Information

Screen recording (Flashing Image):

[![asciicast](https://asciinema.org/a/yAMbaiYvBPLsyUPujOFey6zU3.svg)](https://asciinema.org/a/yAMbaiYvBPLsyUPujOFey6zU3)

Screen recording (System Boot):

[![asciicast](https://asciinema.org/a/Evalgi6VgUvxs4gUmCtzC8n7j.svg)](https://asciinema.org/a/Evalgi6VgUvxs4gUmCtzC8n7j)

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Fri Jul 15 17:21:32 UTC 2022

Kernel 5.4.61 on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password: 
Last login: Sun Jul 17 00:20:39 on pts/0
[  194.914653] proc: Bad value for 'hidepid'
[root@fedora-riscv ~]# neofetch 
             .',;::::;,'.                                                                                                       
         .';:cccccccccccc:;,.            ----------------- 
      .;cccccccccccccccccccccc;.         OS: Fedora Linux 36 (Thirty Six) riscv64 
    .:cccccccccccccccccccccccccc:.       Host: sun20iw1p1 
  .;ccccccccccccc;.:dddl:.;ccccccc;.     Kernel: 5.4.61 
 .:ccccccccccccc;OWMKOOXMWd;ccccccc:.    Uptime: 3 mins 
.:ccccccccccccc;KMMc;cc;xMMc:ccccccc:.   Packages: 1546 (rpm) 
,cccccccccccccc;MMM.;cc;;WW::cccccccc,   Shell: bash 5.1.16 
:cccccccccccccc;MMM.;cccccccccccccccc:   Terminal: /dev/ttyS0 
:ccccccc;oxOOOo;MMM0OOk.;cccccccccccc:   CPU: (1) @ 1.008GHz 
cccccc:0MMKxdd:;MMMkddc.;cccccccccccc;   Memory: 313MiB / 1975MiB 
ccccc:XM0';cccc;MMM.;cccccccccccccccc'
ccccc;MMo;ccccc;MMW.;ccccccccccccccc;                            
ccccc;0MNc.ccc.xMMd:ccccccccccccccc;                             
cccccc;dNMWXXXWM0::cccccccccccccc:,
cccccccc;.:odl:.;cccccccccccccc:,.
:cccccccccccccccccccccccccccc:'.
.:cccccccccccccccccccccc:;,..
  '::cccccccccccccc::;,.

```

## Test Criteria

Test Success: The actual results match the expected results.

Test Failure: The actual results do not match the expected results.

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
