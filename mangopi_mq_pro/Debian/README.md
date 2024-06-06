# Debian MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download link: https://popolon.org/depots/RISC-V/D1/ovsienko/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip
- Reference installation document: https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html

### Hardware Information

- MangoPi MQ Pro
- Power adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Flash Image

Use `unzip` to extract the image.
Use `dd` to write the image to the microSD card.

```bash
unzip /path/to/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip
sudo dd if=/path/to/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img of=/dev/your_device bs=1M status=progress
```

### Login to System

Login to the system via serial port.

Default username: `root`
Default password: `rvboards`

## Expected Results

The system boots up properly and can be accessed through onboard serial port.

## Actual Results

The system boots up properly and access through onboard serial port is successful.

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
