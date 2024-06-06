# Tina Linux Mangopi MQ Test Report

## Test Environment

### Operating System Information

- Download link: [https://mangopi.org/_media/mq-r-f133-rtl8189fs-5113-dns-uart0.zip](https://mangopi.org/_media/mq-r-f133-rtl8189fs-5113-dns-uart0.zip)
- Reference installation document: [https://mangopi.org/mangopi_mq](https://mangopi.org/mangopi_mq)

### Hardware Information

- Mangopi MQ
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Image Burning

After downloading and extracting, use `dd` to burn the image to the SD card:
```bash
sudo dd if=mq-r-f133-rtl8189fs-5113-dns-uart0.img of=/dev/your/device bs=1M status=progress
```

### System Login

Log into the system via serial port.

## Expected Results

The system boots up successfully and can be accessed by logging in through the onboard serial port.

## Actual Results

The system boots up successfully and login through the onboard serial port is achieved.

### Boot Information

Screen recording (from image flashing to system login):

```log
```

## Test Criteria

Test passed: Actual results match the expected results.

Test failed: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
