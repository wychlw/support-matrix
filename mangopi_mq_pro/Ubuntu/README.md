# Ubuntu MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download link: https://cdimage.ubuntu.com/releases/23.10/release/ubuntu-23.10-preinstalled-server-riscv64+nezha.img.xz
- Refer to installation guide: https://mangopi.org/mqpro

### Hardware Information

- MangoPi MQ Pro
- Power adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Flash Image

Use `xz` to extract the image.
Use `dd` to write the image to the microSD card.

```bash
xz -kd /path/to/ubuntu-23.10-preinstalled-server-riscv64+nezha.img.xz
sudo dd if=/path/to/ubuntu-23.10-preinstalled-server-riscv64+nezha.img  of=/dev/your_device bs=1M status=progress
```

### System Login

Log in to the system via serial port.

Default username: `ubuntu`
Default password: `ubuntu`

## Expected Results

The system boots up normally and can be accessed via onboard serial port.

## Actual Results

The system boots up normally and successfully logged in through the onboard serial port.

### Boot Information

Screen recording (from flashing the image to logging into the system):

```log
```

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
