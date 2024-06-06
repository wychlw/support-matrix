# Tina Linux DongshanPI-D1s Test Report

## Test Environment

### Operating System Information

- Download Link: [https://gitlab.com/dongshanpi/tools/-/raw/main/tina_d1s-nezha_sd_uart0.zip](https://gitlab.com/dongshanpi/tools/-/raw/main/tina_d1s-nezha_sd_uart0.zip)
- Reference Installation Document: [https://dongshanpi.com/DongshanPI-D1s/03-1_FlashSystem/](https://dongshanpi.com/DongshanPI-D1s/03-1_FlashSystem/)

### Hardware Information

- DongshanPI-D1s
- One microSD card
- One USB to UART debugger (e.g. CH340, CH341, FT2232)

## Installation Steps

### Flash Image

After downloading and extracting, use `dd` to write the image to the SD card:
```bash
sudo dd if=tina_d1s-nezha_sd_uart0.img of=/dev/your/device bs=1M status=progress
```

### System Login

Login to the system via serial port.

## Expected Results

The system boots up successfully and allows login via the onboard serial port.

## Actual Results

The system boots up successfully and login via the onboard serial port is successful.

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
