# OpenBSD 7.4 HiFive Unmatched Version Test Report

## Test Environment

### Operating System Information

- System Version: OpenBSD 7.4
- Download Link (USTC Mirror): [https://mirrors.tuna.tsinghua.edu.cn/OpenBSD/7.4/riscv64/install74.img](https://mirrors.tuna.tsinghua.edu.cn/OpenBSD/7.4/riscv64/install74.img)
- Reference Installation Documentation: [https://wiki.freebsd.org/riscv/HiFiveUnmatched](https://wiki.freebsd.org/riscv/HiFiveUnmatched)

### Hardware Information

- HiFive Unmatched Rev A
- One microUSB cable (included with HiFive Unmatched)
- One ATX power supply
- One microSD card (Sandisk Extreme Pro 64G UHS-I) preloaded with Freedom U SDK
- One USB flash drive (Lexar S25 32G)

## Installation Steps

### Boot Device Selection

Ensure that the DIP switches are set to boot from the microSD card. If you have not made any changes, the factory default setting is to boot from the microSD card.

The DIP switch should be set as follows: `MSEL[3:0]=1011`

### Flash Freedom U SDK

Download the demo-coreip-cli-unmatched.rootfs.wic.xz image from [here](https://github.com/sifive/freedom-u-sdk/releases/latest).

Unzip the image and write it to the microSD card. The position of the microSD card is `/dev/sdc`.

```bash
xz -dk demo-coreip-cli-unmatched.rootfs.wic.xz
sudo dd if=demo-coreip-cli-unmatched.rootfs.wic of=/dev/sdc status=progress
```

### Write Installation Image to USB Flash Drive

Use the `dd` command to write the image to the microSD card.

```bash
sudo dd if=install74.img of=/dev/sdc status=progress
```

### System Login

Login to the system via the onboard serial port (connect to another computer using the microUSB cable).

## Expected Results

The system boots up successfully, and login via the onboard serial port is possible.

## Actual Results

The system boots up successfully, and login via the onboard serial port is successful.

### Boot Information

![alt text](image.png)

## Test Criteria

Test Successful: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
