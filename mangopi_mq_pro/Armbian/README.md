# Armbian MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: [Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img.xz](https://disk.yandex.ru/d/da8qJ8wyE1hhcQ/Nezha_D1/ArmbianTV/20220722/Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img.xz)
- Installation Guide: [mangopi.org/mqpro](https://mangopi.org/mqpro)

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Flashing the Image

Use `xz` to extract the image.
Use `dd` to write the image to the microSD card.

```bash
xz -kd /path/to/Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img.xz
sudo dd if=/path/to/Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img of=/dev/your_device bs=1M status=progress
```

### System Login

Login to the system via serial port.

Default username: `root`
Password to be set after the first login

## Expected Results

The system boots up correctly and allows login via the onboard serial port.

## Actual Results

The system boots up correctly and login via the onboard serial port is successful.

### Bootup Information

Screen recording (from flashing the image to logging into the system):

```log
```

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
