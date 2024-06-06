# FreeRTOS Nuclei DDR200T Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/Community-PIO-CH32V/ch32-pio-projects
- Reference Documents:
    - PlatformIO Core: https://docs.platformio.org/en/latest/core/installation/index.html
    - PlatformIO ch32v: https://pio-ch32v.readthedocs.io/en/latest/installation.html

### Hardware Information

- Nuclei DDR200T Development Board

## Installation Steps

### Install PlatformIO Core

Check if the package manager contains the [platformio-core](https://archlinux.org/packages/?name=platformio-core) package. If not, you can install it using the installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### Configure PlatformIO Environment

Install Nuclei development environment:
```bash
pio pkg install --global --platform "nuclei/nuclei@^1.0.11"
```

Add udev rules and apply them (may need to change GROUP depending on the distribution):
```bash
curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules | sudo tee /etc/udev/rules.d/99-platformio-udev.rules
cat << EOF | sudo tee -a /etc/udev/rules.d/99-platformio-udev.rules
SUBSYSTEM=="usb", ATTR{idVendor}="1a86", ATTR{idProduct}=="8010", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}="4348", ATTR{idProduct}=="55e0", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}="1a86", ATTR{idProduct}=="8012", GROUP="plugdev"
EOF
sudo udevadm control --reload-rules
sudo udevadm trigger
```

Add user groups:
- Debian-based systems:
```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
```
- Arch-based systems:
```bash
sudo usermod -a -G uucp $USER
sudo usermod -a -G lock $USER
```

### Prepare Project Repository

Clone the relevant repository:
```bash
git clone https://github.com/Nuclei-Software/platform-nuclei.git
```

### Compile Code

Compile the code using pio:
```bash
cd cd platform-nuclei/examples/freertos_demo
pio run
```

### Flash Image

Ensure WCH-Link(E) is connected to the SWD debug port, then flash the image using pio:
```bash
pio run --target upload
```

pio will automatically detect the development board. If flashing fails, you can try manually specifying it:
```bash
pio run -e hbird_eval --target upload
```

### Log into the System

Connect to the development board via serial port.

## Expected Results

The system should start up correctly, and information should be visible through the onboard serial port.

## Actual Results

The system started up correctly, and information could be viewed through the onboard serial port.

### Boot Information

Screen recording (from compilation to startup):

```log
```

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results do not match the expected results.

## Test Conclusion

CFT

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
