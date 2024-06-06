# openEuler 23.03 riscv64 Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.03 riscv64
- Download Links:
    - Buildroot: [here](https://github.com/milkv-duo/duo-buildroot-sdk.git)
    - Rootfs: [here](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/openeuler-rootfs.tar.gz)
- Reference Installation Document: [here](https://blog.inuyasha.love/linuxeveryday/33.html)

> Note: This image is provided in rootfs format

### Hardware Information

- Milk-V Duo 64M
- One USB power adapter
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont wires
- Debugging pins pre-soldered on the Milk-V Duo main body
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Image Building

#### Build Buildroot

Clone Buildroot to build the image
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git
cd duo-buildroot-sdk/
```

Modify kernel configuration

```bash
cat <<EOF >> build/boards/cv180x/cv1800b_milkv_duo_sd/linux/cvitek_cv1800b_milkv_duo_sd_defconfig
# for openEuler
CONFIG_CGROUPS=y
CONFIG_CGROUP_FREEZER=y
CONFIG_CGROUP_PIDS=y
CONFIG_CGROUP_DEVICE=y
CONFIG_CPUSETS=y
CONFIG_PROC_PID_CPUSET=y
CONFIG_CGROUP_CPUACCT=y
CONFIG_PAGE_COUNTER=y
CONFIG_MEMCG=y
CONFIG_CGROUP_SCHED=y
CONFIG_NAMESPACES=y
CONFIG_OVERLAY_FS=y
CONFIG_AUTOFS4_FS=y
CONFIG_SIGNALFD=y
CONFIG_TIMERFD=y
CONFIG_EPOLL=y
CONFIG_IPV6=y
CONFIG_FANOTIFY
EOF
```

Modify line 43 of memmap.py to 0
```bash
vim build/boards/cv180x/cv1800b_milkv_duo_sd/memmap.py

ION_SIZE = 0
```

Compile in Docker (recommended)
```bash
docker run -itd --name duodocker -v $(pwd):/home/work milkvtech/milkv-duo:latest /bin/bash
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo"
```

#### Add Rootfs

Copy the compiled image:
```bash
cd ..
cp duo-buildroot-sdk/out/milkv-duo-20240326-1620.img .
```

Write it to the SD card
```bash
sudo dd if=milkv-duo-20240326-1620.img of=/dev/your-device bs=1M status=progress
```

Start preparing to replace rootfs. Since the original image has insufficient space in rootfs, we need to repartition. As we do not need the original rootfs, we can directly delete the original partition:
```bash
sudo fdisk /dev/your-device

# In fdisk
d
3
d
2
n
p
2
# First sector
# Last sector
w

# Back to bash
sudo mkfs.ext4 /dev/your-device-p2
```

Note: The new rootfs will be mounted on mnt, and the original rootfs will be mounted on mnt2.

Next, extract rootfs to the newly created partition:
```bash
mkdir mnt
mkdir mnt2
sudo mount /dev/your-device-p2 mnt
sudo tar -zxvf /path/to/openeuler-rootfs.tar.gz -C mnt
```

Then mount the original image and copy some necessary files (change the loop devices below according to actual conditions):
```bash
sudo losetup -f -P milkv-duo-20240326-1620.img
sudo mount /dev/loop0p2 mnt2
sudo cp -r mnt2/mnt/system mnt/mnt
sudo cp mnt2/etc/run_usb.sh mnt/etc/
sudo cp mnt2/etc/uhubon.sh mnt/etc/
sudo cp mnt2/etc/init.d/S99user mnt/etc/init.d/
```

Next, prepare to enter the image, first create DNS resolution:
```bash
echo "nameserver 8.8.8.8" | sudo tee mnt/etc/resolv.conf
```

Then enter the image:
```bash
chroot mnt
# arch-chroot mnt
```

Install some necessary packages (such as dhcp, etc.):
```bash
dnf install dhcp
cat <<EOF >> /etc/dhcp/dhcpd.conf
subnet 192.168.42.0 netmask 255.255.255.0 {
        option routers 192.168.42.1;
        range 192.168.42.100 192.168.42.200;
}
EOF
```

Unmount
```bash
exit
sudo umount mnt
sudo umount mnt2
```

### Logging into the System

Note that RNDIS may not be available, so it is recommended to have a serial connection.

Log into the system via serial connection.

Username: `root`
Password: `openEuler12#$`

## Expected Results

The system boots up normally and can be accessed via serial connection.

## Actual Results

The system boots up normally and access via serial connection is successful.

### Boot Information

Screen recording (skip compilation, from image creation to system login):

[![asciicast](https://asciinema.org/a/eoIznNZpjPZSb9mI2NE4wwdzQ.svg)](https://asciinema.org/a/eoIznNZpjPZSb9mI2NE4wwdzQ)

```log
openEuler 23.03
Kernel 5.10.4-tag- on an riscv64

openeuler-riscv64 login: root
Password: 
Last failed login: Thu Jan  1 08:00:58 CST 1970 on ttyS0
There were 2 failed login attempts since the last successful login.


Welcome to 5.10.4-tag-

System information as of time:  Thu Jan  1 08:00:30 CST 1970

System load:    1.68
Processes:      70
Memory used:    61.2%
Swap used:      0.0%
Usage On:       3%
Users online:   1


[root@openeuler-riscv64 ~]# ./neofetch 
                 `.cc.`                                                                                                         
             ``.cccccccc..`                ---------------------- 
          `.cccccccccccccccc.`             OS: openEuler 23.03 riscv64 
      ``.cccccccccccccccccccccc.``         Host: Milk-V Duo 
   `..cccccccccccccccccccccccccccc..`      Kernel: 5.10.4-tag- 
`.ccccccccccccccc/++/ccccccccccccccccc.`   Uptime: 35 secs 
.cccccccccccccccmNMMNdo+oso+ccccccccccc.   Shell: bash 5.1.9 
.cccccccccc/++odms+//+mMMMMm/:+syso/cccc   Terminal: /dev/ttyS0 
.cccccccccyNNMMMs:::/::+o+/:cdMMMMMmcccc   CPU: (1) 
.ccccccc:+NmdyyhNNmNNNd:ccccc:oyyyo:cccc   Memory: 38MiB / 54MiB 
.ccc:ohdmMs:cccc+mNMNmyccccccccccccccccc
.cc/NMMMMMo////:c:///:cccccccccccccccccc                           
.cc:syysyNMNNNMNyccccccccccccccccccccccc                           
.cccccccc+MMMMMNyc:/+++/cccccccccccccccc
.cccccccccohhhs/comMMMMNhccccccccccccccc
.ccccccccccccccc:MMMMMMMM/cccccccccccccc
.ccccccccccccccccsNNNNNd+cccccccccccccc.
`..cccccccccccccccc/+/:cccccccccccccc..`
   ``.cccccccccccccccccccccccccccc.``
       `.cccccccccccccccccccccc.`
          ``.cccccccccccccc.``
              `.cccccccc.`
                 `....`

[root@openeuler-riscv64 ~]# uname -a
Linux openeuler-riscv64 5.10.4-tag- #1 PREEMPT Tue Mar 26 16:08:05 CST 2024 riscv64 riscv64 riscv64 GNU/Linux
[root@openeuler-riscv64 ~]# cat /etc/os-release 
NAME="openEuler"
VERSION="23.03"
ID="openEuler"
VERSION_ID="23.03"
PRETTY_NAME="openEuler 23.03"
ANSI_COLOR="0;31"

[root@openeuler-riscv64 ~]# 
```



## Test Criteria

Test Passed: Actual result matches the expected result.

Test Failed: Actual result does not match the expected result.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
