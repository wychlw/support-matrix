# Melis Allwinner V853 Development Board Test Report

## Test Environment

### Operating System Information

- Image Link: [Image Link](https://bbs.aw-ol.com/assets/uploads/files/1657169725953-e6e69a0f-5837-4840-99fe-8bc62c7abbf2-tina_v853-vision_uart0.img)
- Reference Document: [Reference Document](https://v853.docs.aw-ol.com/)

### Hardware Information

- Allwinner V853 Development Board

## Installation Steps

### Flashing Image (SD Card)

Flash the image to an SD card:
```shell
dd if=1657169725953-e6e69a0f-5837-4840-99fe-8bc62c7abbf2-tina_v853-vision_uart0.img of=/dev/your/device bs=1M status=progress
```

Insert the card into the device and boot up.

### Flashing Image (Onboard EMMC)

Use LiveSuit software, select the image, and connect the development board for flashing.

See LiveSuit setup: [LiveSuit Setup Link](https://linux-sunxi.org/LiveSuit)

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

Connect to UART3 to view serial output.

## Expected Results

The system boots up correctly, and output can be viewed through the serial port.

## Actual Results

The system boots up correctly, and serial output is successfully viewed.

### Boot Information

Screen recording:

```log
```

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
