# FreeBSD MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download link: [https://github.com/freebsd-d1/freebsd-d1](https://github.com/freebsd-d1/freebsd-d1)
- Reference installation document: [https://github.com/freebsd-d1/freebsd-d1](https://github.com/freebsd-d1/freebsd-d1)

### Hardware Information

- MangoPi MQ Pro
- Power adapter
- One microSD card
- One USB to UART debugger

## Installation Steps

### Flash Image

Clone the repository and create an image:

```bash
gmake
dd if=freebsd-d1.img of=/dev/your/device
```

### System Login

Login to the system via serial port.

Default username: `root`
Password will be set after the first login

## Expected Results

The system boots up successfully and can be accessed through the onboard serial port.

## Actual Results

The system boots up successfully and login through the onboard serial port is successful.

### Boot Information

Screen recording (from flashing image to system login):

```log
```

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
