# Zephyr HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- Host: Arch Linux
- Board: Zephyr RTOS
- Reference Installation Document: [https://docs.zephyrproject.org/latest/boards/riscv/index.html](https://docs.zephyrproject.org/latest/boards/riscv/index.html)

### Hardware Information

- HiFive Unmatched Rev A
- One microUSB cable (included with HiFive Unmatched)
- One ATX power supply

> If you are not using Arch but another distribution, please refer to the Zephyr [official documentation](https://docs.zephyrproject.org/latest/develop/getting_started/index.html) for environment setup.

## Installation Steps

### Dependency Package Installation

Requires `paru` or `yay`, AUR Helper, to be already installed.

```bash
# yay -S python-west zephyr-sdk openocd
paru -S python-west zephyr-sdk openocd pyocd
```

### Compilation of Sample Program

```bash
cp /usr/share/zephyr-sdk/zephyrrc ~/.zephyrrc
# 若不是从 AUR 安装，注意 SDK 路径
sudo cp /opt/zephyr-sdk/sysroots/x86_64-pokysdk-linux/usr/share/openocd/contrib/60-openocd.rules /etc/udev/rules.d/
sudo udevadm control --reload
python3 -m venv ~/zephyrproject/.venv
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
source ~/zephyrproject/.venv/bin/activate
west init ~/zephyrproject/
cd ~/zephyrproject/
west update
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
west build -p always -b hifive_unmatched samples/hello_world
```

### Running the Sample Program

Connect the micro USB cable to the Host PC and power on the HiFive Unmatched.

Start a new terminal, open the serial port using tools like minicom/screen:

```bash
sudo minicom -D /dev/ttyUSB1 -b 115200
```

> No need to insert a microSD card. If a microSD card is inserted, manually interrupt the boot process by pressing any key after entering U-Boot.

Start a new terminal, launch `openocd`:

```bash
openocd -c 'bindto 0.0.0.0' \
        -f ~/zephyrproject/zephyr/boards/riscv/hifive_unmatched/support/openocd_hifive_unmatched.cfg
```

Start a new terminal, perform remote debugging with `gdb`:

```bash
# 若不是从 AUR 安装，注意 SDK 下的 gdb 路径
/opt/zephyr-sdk/riscv64-zephyr-elf/bin/riscv64-zephyr-elf-gdb ~/zephyrproject/zephyr/build/zephyr/zephyr.elf \
--batch -ex 'target extended-remote localhost:3333' \
-ex 'load' -ex 'monitor resume' -ex 'monitor shutdown' -ex 'quit'
```

## Expected Results

The system boots up normally and displays the Hello World message.

## Actual Results

The system boots up normally and displays the Hello World message.

Output:

```
*** Booting Zephyr OS build v3.6.0-rc3-8-ga48c958c8fb8 ***
Hello World! hifive_unmatched
```

![alt text](image.png)

## Reference Documentation / Credits

- [Zephyr on HiFive Unmatched](https://github.com/KevinMX/PLCT-Tarsier-Works/blob/main/misc/month10/Zephyr_Unmatched.md)
- [SiFive HiFive Unmatched - Zephyr Project](https://docs.zephyrproject.org/latest/boards/riscv/hifive_unmatched/doc/index.html)
- [Getting Started Guide - Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)
- [Getting Started with Zephyr RTOS v1.13.0 On RISC-V - SiFive Blog](https://www.sifive.cn/blog/getting-started-with-zephyr-rtos-v1.13.0-on-risc-v)

## Test Judgment Criteria

Test Passed: Actual results match the expected results.

Test Failed: Actual results do not match the expected results.

## Test Conclusion

Test Passed.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
