# RT-Thread VisionFive 2 Test Report

## Test Environment

### System Information

- Host: Arch Linux
- Reference Installation Document: [https://doc.rvspace.org/VisionFive2/Application_Notes/RT-Thread/index.html](https://doc.rvspace.org/VisionFive2/Application_Notes/RT-Thread/index.html)

### Hardware Information

- StarFive VisionFive2
- Power Adapter
- USB to UART debuggers (one for connecting to Linux and one for RT-Thread)

## Installation Steps

### Compiling the System

Get the toolchain: scons

```bash
sudo pacman -Syu scons
# sudo apt-get install scons
```

Download the code:

```bash
git clone https://github.com/starfive-tech/VisionFive2.git
cd VisionFive2
git checkout --track origin/rtthread_AMP
git submodule update --init --recursive
```

Initialize the repository:

```bash
cd buildroot && git checkout --track origin/JH7110_VisionFive2_devel && cd ..
cd u-boot && git checkout --track origin/rtthread_AMP && cd ..
cd linux && git checkout --track origin/rtthread_AMP && cd ..
cd opensbi && git checkout rtthread_AMP && cd ..
cd soft_3rdpart && git checkout JH7110_VisionFive2_devel && cd ..
cd rtthread && git checkout rtthread_AMP && cd ..
```

Download the toolchain:

```bash
wget https://github.com/starfive-tech/rt-thread/blob/rtthread_AMP/toolchain/tool-root1.tar.gz
sudo tar xf rtthread/toolchain/tool-root1.tar.gz -C /opt/
```

Make sure git-lfs is installed and enabled in the environment! Otherwise, compilation errors may occur ([issue #5](https://github.com/starfive-tech/VisionFive2/issues/5))

Compile:
```bash
# scons --menuconfig # 若需配置再运行
make -j($nproc)
```

**Note: Compilation takes a long time, maintain a good network connection and be patient for several hours**

### Running the System

Connect the two debug serial ports, as shown below for RTOS:
![uart](image.png)

> Pin9, Pin11, and Pin13 form a complete serial port:
> Pin9 (GND)
> Pin11 (GPIO42): UART1 RX
> Pin13 (GPIO43): UART1 TX

Burn the compiled `u-boot-spl.bin.normal.out` and `visionfive2_fw_payload.img` files. The official tutorial is to burn them to flash, you can refer to [updating uboot and spl](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/updating_spl_and_u_boot%20-%20vf2.html#updating_spl_and_u_boot-vf2__section_y3j_yp5_yvb).

Alternatively, you can burn them to an SD card to avoid overwriting the existing boot. However, since visionfive2_fw_payload.img exceeds 4M and cannot be directly replaced, this method also requires building a rootfs.
Below is an example of burning to an SD card. First, prepare the SD card image for VisionFive2.

```bash
make buildroot_rootfs -j$(nproc)
make img
```

Next, burn the image:
```bash
sudo dd if=work/sdcard.img of=/dev/ of=/dev/your-device bs=1M status=progress
sync
```

Note that this method requires selecting boot from the SD card.

## Expected Results

The system starts up normally, and login through the serial port is successful.

## Actual Results

The system starts up normally, and login through the serial port is successful.

```log
SBI: OpenSBI v1.2
SBI Specification Version: 1.0
heap: [0x6f000000 - 0x70000000]

 \ | /
- RT -     Thread Operating System
 / | \     5.1.0 build Mar 28 2024 14:25:42
 2006 - 2022 Copyright by RT-Thread team
lwIP-2.0.3 initialized!
Hello RISC-V
Hello Starfive RT-Thread! CPU_ID(4)
rpmsg linux test: receive data from linux then send back
rpmsg remote: remote core cpu_id-4
rpmsg remote: shmem_base-0x6e410000 shmem_end-0x6e7fffff
```

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
