# Debian DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link: [DongshanPI/NezhaSTU-ReleaseLinux/releases/download/v0.1.0-alpha/DshanNezhaSTU-APTok-Sdcard.img.gz](https://github.com/DongshanPI/NezhaSTU-ReleaseLinux/releases/download/v0.1.0-alpha/DshanNezhaSTU-APTok-Sdcard.img.gz)
- Reference Installation Document: [DongshanPI/NezhaSTU-ReleaseLinux](https://github.com/DongshanPI/NezhaSTU-ReleaseLinux)

### Hardware Information

- DongshanPI-Nezha STU
- Power Adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Flash Image

Use `gzip` to decompress the image.
Clear your SD card.
Use `dd` to write the image to the microSD card.

```bash
gzip -kd /path/to/DshanNezhaSTU-APTok-Sdcard.img.gz
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/DshanNezhaSTU-APTok-Sdcard.img of=/dev/your_device bs=1M status=progress
```

### Log into System

Log into the system via serial port.

Default username: `root`
Default password: `100ask`

## Expected Results

The system should boot up successfully and allow login via the onboard serial port.

## Actual Results

The system booted up successfully, and login via the onboard serial port was also successful.

### Boot Information

Screen recording (from flashing the image to logging into the system):

```log
```

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
