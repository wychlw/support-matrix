# openEuler RISC-V 23.09 VisionFive 2 Version Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.09 RISC-V preview
- Download Link: [Download here](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/VisionFive2/)
- Installation Guide: [Installation Guide Reference](https://gitee.com/openeuler/RISC-V/blob/master/release/openEuler-23.03/Installation_Book/Visionfive2/README.md)

### Hardware Information

- StarFive VisionFive 2
- One USB Power Adapter
- One USB-A to C or C to C Cable
- One microSD Card
- One USB to UART Debugger (e.g., CH340, CH341, FT2232)
- Three DuPont Wires

## Installation Steps

### Write Image to microSD Card using `ruyi` CLI

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the instructions provided.

### Boot Mode Selection

StarFive VisionFive 2 offers various boot modes that can be configured using onboard DIP switches before powering on. Refer to the StarFive [official documentation](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/boot_mode_settings.html) for details.

The board itself is also labeled.

To boot the openEuler image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require firmware updates in the Flash memory. For more details, refer to the official documentation: [Update SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

If you choose not to update the firmware, opt for microSD card boot (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

> Note: There is a slight possibility of startup failure in this mode. If faced with startup issues, and the serial port output resembles the following:

```log
dwmci_s: Response Timeout.                                                                                            
dwmci_s: Response Timeout.                                                                                            
BOOT fail,Error is 0xffffffff
```

> You can try power cycling the board or pressing the button near the USB Type-C power interface. This often resolves startup problems.

### System Login

Login to the system via serial console.

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

## Expected Results

The system should boot up successfully, allowing login through the graphical interface.

## Actual Results

The system booted up successfully, and graphical interface login was achieved.

### Boot Information

Screen recording (from image writing to system login):

[![asciicast](https://asciinema.org/a/A3KitOgctHGhyUvkUd2a8LwsH.svg)](https://asciinema.org/a/A3KitOgctHGhyUvkUd2a8LwsH)

## Test Criteria

Test Pass: Actual results match the expected results.

Test Fail: Actual results differ from the expected results.

## Test Conclusion

Test passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
