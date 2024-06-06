# Tina Linux D1s NeZha Test Report

## Test Environment

### Operating System Information

- Link: [https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol](https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol) Extraction code: awol
- Reference Installation Document: [https://d1s.docs.aw-ol.com/study/study_1tina/](https://d1s.docs.aw-ol.com/study/study_1tina/)

### Hardware Information

- D1s NeZha
- One microSD card
- One USB to UART debugger (such as: CH340, CH341, FT2232, etc.)

## Installation Steps

### Image Packaging

After downloading and extracting, prepare to compile the SDK:
```bash
source build/envsetup.sh
lunch
make -j$(nproc)
pack
```

### Burning Image

Use LiveSuit software, select the image, and connect to the development board for flashing.

For LiveSuit acquisition, visit: [https://linux-sunxi.org/LiveSuit](https://linux-sunxi.org/LiveSuit)

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

### Login to System

Login to the system via serial port.

## Expected Results

The system boots up normally and can be accessed by logging in via the onboard serial port.

## Actual Results

The system boots up normally and login via the onboard serial port is successful.

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
