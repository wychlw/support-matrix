# Fedora MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download link: [here](https://openkoji-bj.isrc.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst)
- Reference installation document: [here](https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html)

### Hardware Information

- MangoPi MQ Pro
- Power adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Flashing Image

Decompress the image using `zstd`.
Write the image to the microSD card using `dd`.

```bash
zstd -kd fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
sudo dd if=/path/to/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220104-012902.n.0-sda.raw of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Log into the system via serial port.

Default username: `root`
Default password: `riscv`

## Expected Results

The system should boot up normally, allowing login via onboard serial port.

## Actual Results

The system started up successfully, and login via the onboard serial port was successful.

### Boot Information

Screen recording (from flashing the image to logging into the system):

```log
```

## Test Judgement Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
