# Ubuntu 23.10 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 23.10
- Download Link: [here](https://ubuntu.com/download/risc-v)
- Reference Installation Guide: [here](https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched)

### Hardware Information

- HiFive Unmatched Rev A
- One microUSB cable (included with HiFive Unmatched)
- One ATX power supply
- One microSD card (Sandisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Make sure the dip switch is set to boot from the microSD card. If you haven't changed it, the factory default is set to boot from the microSD card.

Dip switch settings should be as follows: `MSEL[3:0]=1011`

### Use the `ruyi` CLI to flash the image to the microSD card

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Login to the system

Login to the system via the onboard serial port (connect to another computer using the microUSB cable).

Default username: `ubuntu`
Default password: `ubuntu`

Upon initial login, the system will prompt you to change the password.

## Expected Results

The system boots up normally and can be accessed via the onboard serial port.

## Actual Results

The system boots up normally, and login via the onboard serial port is successful.

### Boot information

```log
ubuntu@ubuntu:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.5.0-9-generic #9.1-Ubuntu SMP Sat Oct  7 17:18:31 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 23.10"
NAME="Ubuntu"
VERSION_ID="23.10"
VERSION="23.10 (Mantic Minotaur)"
VERSION_CODENAME=mantic
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=mantic
LOGO=ubuntu-logo
ubuntu@ubuntu:~$
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/Rh773h5eOalKZlzjQRFrQDnjY.svg)](https://asciinema.org/a/Rh773h5eOalKZlzjQRFrQDnjY)

## Test Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
