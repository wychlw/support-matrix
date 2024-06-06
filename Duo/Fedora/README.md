# Fedora 38 Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: Fedora 38
- Download Link: [Fedora-38-Minimal-MilkV-Duo-riscv64.img.xz](https://github.com/chainsx/fedora-riscv-builder/releases/download/20230719-1650/Fedora-38-Minimal-MilkV-Duo-riscv64.img.xz)
- Installation Reference Document: [Fedora RISC-V Builder](https://github.com/chainsx/fedora-riscv-builder)
- Issue/CFH: [Fedora-riscv-builder Issue #6](https://github.com/chainsx/fedora-riscv-builder/issues/6)
    - (Image fails to boot)

> Note: This image is provided by community developers and not an official image.

### Hardware Information

- Milk-V Duo 64M
- 1 USB Power Adapter
- 1 USB-A to C or USB C to C cable
- 1 microSD card
- 1 USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- 3 DuPont lines
- Development board Milk-V Duo with pre-soldered pins for debugging
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Use `dd` to write the image to the microSD card

```shell
xzcat Fedora-38-Minimal-MilkV-Duo-riscv64.img.xz | sudo dd of=/dev/sdc bs=4M iflag=fullblock status=progress 
```

### System Login

Access the system via serial console.

Username: `root`
Password: `fedora`

## Expected Results

The system boots successfully, allowing login via the serial console.

## Actual Results

The system failed to boot successfully. Upon booting, systemd core dumps, preventing normal login.

### Boot Information

```log
[  *** ] (2 of 7) Job systemd-update-utmp.se…ice/start running (20s / no limit)                                                     
[  182.618625] (imesyncd)[130]: unhandled signal 11 code 0x1 at 0xffffffffffffffff in libsystemd-shared-253.2-614.7.riscv64.fc38.so]
[  182.632471] CPU: 0 PID: 130 Comm: (imesyncd) Not tainted 5.10.4-tag- #1                                                          
[  182.639349] epc: 0000003fb7b5aece ra : 0000003fb7b5aece sp : 0000003fffe42320                                                    
[  182.646762]  gp : 0000002ac2e73800 tp : 0000003fb71cb260 t0 : 0000003fb7c1d9d8                                                   
[  182.654266]  t1 : 0000003fb7b1dbbc t2 : 0000000000000000 s0 : 0000003fffe423a0                                                   
[  182.661769]  s1 : 0000003fb7ce9c20 a0 : 0000000000000000 a1 : 0000002ac2f6ee80                                                   
[  182.669273]  a2 : 0000002ac2f6ee80 a3 : 0000000000000000 a4 : 0000000000000000                                                   
[  182.676778]  a5 : 0000000000000000 a6 : fefefefefefefeff a7 : 0000000000000024                                                   
[  182.684277]  s2 : 0000002ac2f6ee80 s3 : 0000003fb7ce9c30 s4 : 0000000000000000                                                   
[  182.691781]  s5 : 0000002ac2f6ee80 s6 : 0000003fffe424c8 s7 : ffffffffffffffff                                                   
[  182.699286]  s8 : 000000000000002d s9 : ffffffffffffffff s10: ffffffffffffffff                                                   
[  182.706789]  s11: 0000000000000006 t3 : 0000003fb7bfc72e t4 : 0000000000000000                                                   
[  182.714293]  t5 : 0000000000000000 t6 : 000000000000002f                                                                         
[  182.719818] status: 8000000201804020 badaddr: ffffffffffffffff cause: 000000000000000d
```

Boot process screen recording:

[![asciicast](https://asciinema.org/a/MxHNPZZ2MG8vPEBSmMNwTz6DY.svg)](https://asciinema.org/a/MxHNPZZ2MG8vPEBSmMNwTz6DY)

### Defect Report

[Fedora-riscv-builder Issue #6](https://github.com/chainsx/fedora-riscv-builder/issues/6)

## Test Judgement Criteria

Successful Test: Actual results match the expected results.

Failed Test: Actual results differ from the expected results.

## Test Conclusion

Test Failed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
