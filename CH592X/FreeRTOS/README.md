# FreeRTOS CH592X Official Version Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://www.wch.cn/downloads/CH592EVT_ZIP.html
- Reference Documents: https://www.wch.cn/downloads/CH592EVT_ZIP.html
    - wchisp: https://github.com/ch32-rs/wchisp
- Flashing Tool:
    - https://github.com/ch32-rs/wchisp/

### Hardware Information

- CH592X-EVT-R1-1v0
- One USB to UART Debugger
- One USB Type-C Cable

## Installation Steps

### Flash Image

Pre-compiled image is located at `EVT/EXAM/FreeRTOS/obj/FreeRTOS.hex`

After downloading and extracting the source code and wchisp tool, **do not power on first**. Press and hold the boot(download) button, then connect the board to the computer via Type-C cable.

Use the wchisp tool for flashing:
```bash
./wchisp flash EVT/EXAM/FreeRTOS/obj/FreeRTOS.hex

```

### System Login

Connect to the development board via serial port.

## Expected Results

The system should boot up properly, and information can be viewed through the onboard serial port.

## Actual Results

The system booted up correctly, and information can be viewed through the onboard serial port.

### Boot-up Information

Screen recording (from flashing to boot-up):
[![asciicast](https://asciinema.org/a/dQb48LYxe4BpWMlXeT0AcSBa6.svg)](https://asciinema.org/a/dQb48LYxe4BpWMlXeT0AcSBa6)

```log
start.
      task2 entry 1
                   task1 entry 1
                                task1 entry 2
                                             task2 entry 2
                                                          task1 entry 1
                                                                       task1 entry 2
                                                                                    task2 entry 1

```

## Test Judgement Criteria

Test Succeeds: Actual results match the expected results.

Test Fails: Actual results do not match the expected results.

## Test Conclusion

Test Succeeds

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
