# BuildRoot Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
- Installation Reference: https://github.com/milkv-duo/duo-buildroot-sdk
    - FreeRTOS: https://milkv.io/zh/docs/duo/getting-started/rtoscore

### Hardware Information

- Milk-V Duo 256M
- One USB-A to C or USB C to C cable
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

The RTOS is already included in the BuildRoot SDK.

### Building the mailbox-test binary

Clone the duo-examples repository locally and build it.

```shell
sudo apt install -y wget git make
git clone https://github.com/milkv-duo/duo-examples --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```
#### Packaging the built binary into the image

First, check for the available loop devices:

```shell
sudo losetup -f
```

The output should be:

```shell
$ sudo losetup -f
/dev/loop16
```

Next, mount the downloaded image and copy the compiled binary into the image:

```shell
sudo losetup /dev/loop16 milkv-duo256m-v1.1.0-2024-0410.img
sudo kpartx -av /dev/loop16
sudo mount /dev/mapper/loop16p2 /mnt
cp ~/duo-examples/mailbox-test/mailbox_test /mnt/root/
sudo umount /mnt
sudo kpartx -d /dev/loop1
sudo losetup -d /dev/loop16 
```

Flash the modified image next:

```shell
sudo dd if=milkv-duo256m-v1.1.0-2024-0410.img of=/dev/sdc bs=4M status=progress oflag=direct
```

At this point, the SD card is ready. Insert it into the development board and prepare to boot.

### Logging into the System

Login to the system via serial console.

Default username: `root`
Default password: `milkv`

## Expected Results

The system should boot up successfully. After logging in via the onboard serial console, run the `mailbox_test` binary, and the onboard blue LED should turn on and then off.

(In standby mode, the blue LED should blink.)

## Actual Results

The system boots up properly. Successfully logged in via the onboard serial console, `mailbox_test` runs without issues, and the onboard LED turns on and then off.

### Boot Information

```log
The authenticity of host '192.168.42.1 (192.168.42.1)' can't be established.
ED25519 key fingerprint is SHA256:JrNwim4ZPbnSw+aC9orl+VPBoRBkXxMatEDjRSq8SSw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.42.1' (ED25519) to the list of known hosts.
root@192.168.42.1's password: 
[root@milkv-duo]~# ./mailbox_test 
C906B: cmd.param_ptr = 0x4
C906B: cmd.param_ptr = 0x3
[root@milkv-duo]~# exit

```

Screen recording:
[![asciicast](https://asciinema.org/a/MhkD6TsSDQ9N0w4u2k6VUHn3s.svg)](https://asciinema.org/a/MhkD6TsSDQ9N0w4u2k6VUHn3s)

## Test Judgment Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Successful

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
