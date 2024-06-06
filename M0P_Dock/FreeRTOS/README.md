# FreeRTOS Demo M0P Dock Test Report

## Test Environment

### Operating System Information

- Build System: Ubuntu 22.04.4 LTS
- Source Code Link: https://github.com/sipeed/M0P_BL618_examples
- Reference Installation Document: https://github.com/sipeed/M0P_BL618_examples
    - Environment Setup:
        - https://github.com/bouffalolab/bouffalo_sdk#environment-setup
        - https://bl-mcu-sdk.readthedocs.io/zh_CN/latest/get_started/get_started.html
- Toolchain: https://gitee.com/bouffalolab/toolchain_gcc_t-head_linux

### Hardware Information

- Sipeed M0P Dock (BL618)
- One USB A to C or C to C cable

## Installation Steps

### Prepare Build Environment

```shell
git clone https://gitee.com/bouffalolab/toolchain_gcc_t-head_linux --depth=1
export PATH=$PWD/toolchain_gcc_t-head_linux/bin:$PATH
sudo apt install ninja-build make
git clone https://github.com/sipeed/M0P_BL618_examples.git
cd M0P_BL618_examples
git submodule update --init
cd bouffalo_sdk
# git config --global user.name user
# git config --global user.email user@example.com
git am ../sipeed_support/fixes/m0pdock/*.patch && cd -
cd sipeed_support/examples/m0pdock
# Replace ttyACMx with your actual device name
make flash COMX=/dev/ttyACM0
```

### Build FreeRTOS Demo

```shell
cd M0P_BL618_examples
git submodule update --init
cd bouffalo_sdk
# git config --global user.name user
# git config --global user.email user@example.com
git am ../sipeed_support/fixes/m0pdock/*.patch && cd -
cd sipeed_support/examples/m0pdock/wifi_screen
make # Or: make ninja
```

### Flash Image

```shell
make flash COMX=/dev/ttyACM0 # Replace ttyACMx with your actual device name
```

### Start UDP Server on Development Board

Refer to: https://github.com/sipeed/M0P_BL618_examples/tree/main/sipeed_support/examples/m0pdock/wifi_screen

```shell
bouffalolab />wifi_sta_connect SIPEED_TEST 12345678
bouffalolab />wifi_udp_server
bouffalolab />udp server task start ...
wifi_udp_server [port]
         port: local listen port, default port 5001
udp bind success!
Server ip Address : 0.0.0.0:5001
Press CTRL-C to exit.
recv[2/204800] from 172.49.14.160
recv[10240/204798] from 172.49.14.160
recv[10240/194558] from 172.49.14.160
recv[10240/184318] from 172.49.14.160
recv[10240/174078] from 172.49.14.160
recv[10240/163838] from 172.49.14.160
```

### Startup Information

## Test Criteria

Successful Test: Actual results match expected results.

Failed Test: Actual results do not match expected results.

## Test Conclusion

Test successful.

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
