# RevyOS Pioneer Test Report

## Test Environment

### Operating System Information

- System Version: RevyOS 20240119
- Download Link: [https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20240119/](https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20240119/)
- Reference Installation Guide: [https://revyos.github.io/docs/](https://revyos.github.io/docs/)

### Hardware Information

- Milk-V Pioneer Box v1.1
- One microSD card
- HDMI cable + monitor

## Installation Steps

### Flashing Image

Decompress the image using `zstd`.
Write the image to the microSD card using `dd`.

```bash
zstd -d /path/to/revyos.img.zstd
dd if=/path/to/revyos.img of=/dev/yout-device bs=4M status=progress
```

### Common Issues

- To boot from the SD card, manually add Fip.bin and ZSBL to it.

### Logging into the System

Log into the system via the graphical interface.

Default username: `debian`
Default password: `debian`

## Test Criteria

Successful test: Actual results match the expected results.

Failed test: Actual results do not match the expected results.

## Expected Results

The system boots up normally and allows login through the graphical interface.

## Actual Results

The system boots up normally and login through the graphical interface is successful.

### Boot Information

![desktop_uname](./desktop_uname.png)

Serial logs (from flashing the system to booting up):

[![asciicast](https://asciinema.org/a/voe4Uou1CvIP7u21inc3tfjAT.svg)](https://asciinema.org/a/voe4Uou1CvIP7u21inc3tfjAT)

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
