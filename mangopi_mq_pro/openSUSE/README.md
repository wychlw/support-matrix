# Armbian MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download link: [https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz)
- Reference installation document: [https://en.opensuse.org/HCL:MangoPi_MQ-Pro](https://en.opensuse.org/HCL:MangoPi_MQ-Pro)

### Hardware Information

- MangoPi MQ Pro
- Power adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Image Writing

Use `xz` to extract the image.
Use `dd` to write the image to the microSD card.

```bash
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz.raw.xz | dd bs=4M of=/dev/your/device iflag=fullblock oflag=direct status=progress; sync
```

### System Login

Login to the system via serial port.

Default username: `root`
Default password: `linux`

## Expected Results

The system boots up normally and can be accessed via the onboard serial port.

## Actual Results

The system boots up normally and login via the onboard serial port is successful.

### Boot Information

Screen recording (from image writing to system login):

```log
```

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
