# FreeBSD 14.0 HiFive Unmatched Version Test Report

## Test Environment

### Operating System Information

- System Version: FreeBSD 14.0
- Download Link (USTC Mirror): [FreeBSD 14.0 ISO Image](https://mirrors.ustc.edu.cn/freebsd/releases/riscv/riscv64/ISO-IMAGES/14.0/FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img.xz)
- Reference Installation Documentation: [HiFiveUnmatched FreeBSD Wiki](https://wiki.freebsd.org/riscv/HiFiveUnmatched)

### Hardware Information

- HiFive Unmatched Rev A
- One microUSB cable (included with HiFive Unmatched)
- One ATX power supply
- One microSD card (Sandisk Extreme Pro 64G UHS-I) preloaded with Freedom U SDK
- One USB flash drive (Lexar S25 32G)

## Installation Steps

### Boot Device Selection

Ensure that the dip switch is set to boot from the microSD card. The factory default setting is to boot from the microSD card.

Dip switch settings should be as follows: `MSEL[3:0]=1011`

### Flashing Freedom U SDK

Fetch the demo-coreip-cli-unmatched.rootfs.wic.xz image from [here](https://github.com/sifive/freedom-u-sdk/releases/latest).

Extract the image and write it to the microSD card. The location of the microSD card is `/dev/sdc`.

```bash
xz -dk demo-coreip-cli-unmatched.rootfs.wic.xz
sudo dd if=demo-coreip-cli-unmatched.rootfs.wic of=/dev/sdc status=progress
```

### Flashing Installation Image to USB Drive

Extract the image and use the `dd` command to write the image to the microSD card.

```bash
xz -dk FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img.xz
sudo dd if=FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img of=/dev/sdc status=progress
```

### Logging into the System

Login to the system via the onboard serial port (connect to another computer using a microUSB cable).

## Expected Results

The system should boot up successfully and allow login via the onboard serial port.

## Actual Results

The system booted up successfully and login via the onboard serial port was achieved.

### Boot Messages

![alt text](image.png)

![alt text](image-1.png)

## Test Judgment Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

Test passed successfully.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
