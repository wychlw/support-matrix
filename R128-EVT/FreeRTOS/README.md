
# FreeRTOS R128 EVT Development Kit Test Report

## Test Environment

### Operating System Information

- SDK Link:
    - https://r128.docs.aw-ol.com/r128/get_sdk/
- Precompiled Firmware for Testing: https://www.aw-ol.com/downloads/resources/126
- Reference Documentation:
    - https://r128.docs.aw-ol.com/devkit/r128_evt/

### Hardware Information

- TinyVision Development Board

## Installation Steps

### Image Burning

After downloading the image, use LiveSuit software, select the image, and connect to the development board to burn it.

Check how to get LiveSuit here: https://linux-sunxi.org/LiveSuit

#### LiveSuit

Download and build:
```bash
git clone https://github.com/linux-sunxi/sunxi-livesuite.git
apt-get install dkms
make
# If you are getting error that /lib/modules/4.4.50+/build is missing try adding symlink to the /usr/src/linux-headers-XXX, for example:
# sudo ln -s /usr/src/linux-headers-3.6-trunk-rpi/ /lib/modules/4.4.50+/build

cp awusb.ko /lib/modules/`uname -r`/kernel/
depmod -a
modprobe awusb
KERNEL=="aw_efex[0-9]*", MODE="0666"
udevadm control --reload-rules
```

Run:
```bash
./LiveSuit.sh
```

### System Login

Connect to UART3 to view serial port output.

## Expected Results

The system boots up properly, and the output can be viewed through the serial port.

## Actual Results

The system boots up properly, and the output is successfully viewed through the serial port.

### Boot Information

Screen recording:

```log
```

## Test Criteria

Test Success: Actual results match the expected results.

Test Failure: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
