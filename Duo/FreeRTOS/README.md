# BuildRoot Milk-V Duo Test Report

## Test Environment

### Operating System Information

- Build System: Ubuntu 22.04.3 LTS x86_64
- System Version: Duo-V1.0.9
- Download Link: [GitHub Milk-V Duo Buildroot SDK Releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
- Reference Installation Document: [GitHub Milk-V Duo Buildroot SDK](https://github.com/milkv-duo/duo-buildroot-sdk)
    - FreeRTOS: [Milk-V DUO Getting Started RTOS Core](https://milkv.io/zh/docs/duo/getting-started/rtoscore)

### Hardware Information

- Milk-V Duo 64M
- 1 USB power adapter
- 1 USB-A to C or USB C to C cable
- 1 microSD card
- 1 USB to UART debugger (e.g. CH340, CH341, FT2232, etc.)
- 3 DuPont wires
- Pre-soldered debugging pins on Milk-V Duo main unit
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps


### Build the mailbox-test binary

Pull the duo-examples repository to your local machine and build it.

```shell
sudo apt install -y wget git make
git clone https://github.com/milkv-duo/duo-examples --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```
#### Package the built binary into the image

First, check for the available loop devices:

```shell
sudo losetup -f
```

The output should display:

```shell
$ sudo losetup -f
/dev/loop16
```

Next, mount the downloaded image and copy the compiled binary into the image:

```shell
sudo losetup /dev/loop16 milkv-duo-v1.0.9-2024-0226.img
sudo kpartx -av /dev/loop16
sudo mount /dev/mapper/loop16p2 /mnt
cp ~/duo-examples/mailbox-test/mailbox_test /mnt/root/
sudo umount /mnt
sudo kpartx -d /dev/loop1
sudo losetup -d /dev/loop16 
```

Flash the modified image:

```shell
sudo dd if=milkv-duo-v1.0.9-2024-0226.img of=/dev/sdc bs=4M status=progress oflag=direct
```

At this point, the SD card is ready. Insert it into the development board and prepare for booting.

### Log into the System

Log into the system via serial terminal.

## Expected Results

The system should boot up normally, login via onboard serial terminal, run the `mailbox_test` binary, and have the onboard blue LED turn on and then off.

(Standby status: blue LED blinking)

## Actual Results

The system boots up correctly, successfully logs in via onboard serial terminal, `mailbox_test` runs as expected, and the onboard LED turns on and then off.

### Boot Information

```log
[    7.841103] sync_task_init:177(): sync_task_init vi_pipe 1
[    7.847065] sync_task_init:177(): sync_task_init vi_pipe 2
[    7.853504] vi_core_probe:252(): isp registered as cvi-vi
[    7.907831] cvi_dwa_probe:487(): done with rc(0).
[    7.937525] cv180x-cooling cv180x_cooling: elems of dev-freqs=6
[    7.943796] cv180x-cooling cv180x_cooling: dev_freqs[0]: 850000000 500000000
[    7.951586] cv180x-cooling cv180x_cooling: dev_freqs[1]: 425000000 375000000
[    7.959250] cv180x-cooling cv180x_cooling: dev_freqs[2]: 425000000 300000000
[    7.966985] cv180x-cooling cv180x_cooling: Cooling device registered: cv180x_cooling
[    8.002672] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    8.010370] end jpu_init result = 0x0
[    8.132269] cvi_vc_drv_init result = 0x0
[    8.147188] sh (166): drop_caches: 3
Starting app...

[root@milkv-duo]~# ls
mailbox_test
[root@milkv-duo]~# ./mailbox_test 
RT: [30.619843]prvQueueISR
RT: [30.622192]recv cmd(19) from C906B, param_ptr [0x00000002]
RT: [30.627922]recv cmd(19) from C906B...send [0x00000004] to C906B
C906B: cmd.param_ptr = 0x4
RT: [34.634965]prvQueueISR
RT: [34.637311]recv cmd(19) from C906B, param_ptr [0x00000003]
RT: [34.643042]recv cmd(19) from C906B...send [0x00000004] to C906B
C906B: cmd.param_ptr = 0x3
[root@milkv-duo]~#
```

Screen recording:

[![asciicast](https://asciinema.org/a/IANV6OK3PCAMO3L7hcx11ngck.svg)](https://asciinema.org/a/IANV6OK3PCAMO3L7hcx11ngck)

## Test Evaluation Criteria

Test Success: Actual results align with expected results.

Test Failure: Actual results do not match expected results.

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
