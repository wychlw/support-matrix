# Zephyr VisionFive 2 Test Report

## Test Environment

### System Information

- Host: Arch Linux
- Reference Installation Documentation: [https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html](https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html)

### Hardware Information

- StarFive VisionFive2
- Power Adapter
- One USB to UART Debugger

## Installation Steps

### Configure Zephyr Environment

*For configuration in other distributions, refer to: [Zephyr Official Documentation](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)*

For Arch Linux, the environment can be directly installed from AUR:
```bash
yay -Syu python-west zephyr-sdk openocd
# paru -S python-west zephyr-sdk openocd pyocd
```

Next, set up the environment (remember to replace the SDK path):
```bash
cp /usr/share/zephyr-sdk/zephyrrc ~/.zephyrrc
sudo cp /opt/zephyr-sdk/sysroots/x86_64-pokysdk-linux/usr/share/openocd/contrib/60-openocd.rules /etc/udev/rules.d/
sudo udevadm control --reload
source ~/zephyrproject/.venv/bin/activate
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
source ~/zephyrproject/.venv/bin/activate
west init ~/zephyrproject/
cd ~/zephyrproject/
west update
west zephyr-export
```

### Compile spl_tools

Clone [https://github.com/starfive-tech/Tools.git](https://github.com/starfive-tech/Tools.git) and compile the spl_tool within.

```bash
git clone https://github.com/starfive-tech/Tools.git
cd Tools/spl_tool
make
cd ../..
```

### Compile Sample Program

Compile the sample program and add the SPL header:

```bash
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
west build -p always -b visionfive2 ~/zephyrproject/zephyr/samples/hello_world
Tools/spl_tool/spl_tool -c -f ~/zephyrproject/zephyr/build/zephyr/zephyr.bin
```

At this point, a `zephyr.bin.normal.out` file should have been generated in `~/zephyrproject/zephyr/build/zephyr/`.

### Flash and Run Sample Program

Set the start-up mode of VisionFive2 to boot from UART (both DIP switches set to 1). If done correctly, you should see UART output prompt: `CCCCCC...`

Clone the following repositories in your working directory:

- vf2-loader tool [https://github.com/orangecms/vf2-loader.git](https://github.com/orangecms/vf2-loader.git)
- xmodem tool [https://github.com/orangecms/xmodem.rs.git](https://github.com/orangecms/xmodem.rs.git)

Switch to the dev branch of xmodem.rs

```bash
git clone https://github.com/orangecms/vf2-loader.git 
git clone https://github.com/orangecms/xmodem.rs.git
cd xmodem.rs
git checkout dev
cd ..
```

Navigate into the `vf2-loader` directory, and copy the previously generated `zephyr.bin.normal.out` file to the current directory:

```bash
cd vf2-loader
cp ~/zephyrproject/zephyr/build/zephyr/zephyr.bin.normal.out .
```

Connect the UART, flash the image:

```bash
cargo run -- zephyr.bin.normal.out && minicom -D /dev/ttyUSB0
```

## Expected Results

The system should start up normally and display the "Hello World" message.

## Actual Results

UART flashing completed, but no output is visible.

Screen recording:
[![asciicast](https://asciinema.org/a/a2i4u5ryVYGEBo73UzswGGFAn.svg)](https://asciinema.org/a/a2i4u5ryVYGEBo73UzswGGFAn)

### Forum Post

https://forum.rvspace.org/t/no-output-while-trying-zephyr-on-visionfive-2/4243

## Test Criteria

Test Passed: Actual results match expected results.

Test Failed: Actual results do not match expected results.

## Test Conclusion

Test Failed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
