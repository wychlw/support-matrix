# Zephyr Longan Nano Test Report

## Test Environment

### Operating System Information

- Source Code Link: [link](https://github.com/zephyrproject-rtos/zephyr/tree/main)
- Reference Documentation: [link](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)

### Hardware Information

- Longan Nano
- 1 x USB to UART Debugger
- 1 x Type-C Cable

## Installation Steps

### Install Zephyr

Create a virtual environment:

```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west
```

Get Zephyr:
```bash
west init ~/zephyrproject
cd ~/zephyrproject
west update
```

Set up the environment:
```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
```

### Compile Code

Compile the code using west:
```bash
west build -p always -b longan_nano samples/basic/blinky

```

### Flash Image

Press and hold the boot button, then press reset, and release the boot button.
Flash using the USB port:
```bash
west flash --runner dfu-util

```

## Expected Results

The system should boot up properly, and information should be visible through the onboard serial port.

## Actual Results

The system booted up successfully, and information was visible through the onboard serial port.

### Boot Information

Screen recording (from compilation to boot):
[![asciicast](https://asciinema.org/a/Kz2OGHEaRjIODgvzJWO5dPTWm.svg)](https://asciinema.org/a/Kz2OGHEaRjIODgvzJWO5dPTWm)

```log
*** Booting Zephyr OS build v3.6.0-1803-gf419ea799099 ***
LED state: OFF
LED state: ON
LED state: OFF
LED state: ON
LED state: OFF

```

## Test Criteria

Test Success: Actual results match the expected results.

Test Failure: Actual results do not match the expected results.

## Test Conclusion

Test successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
