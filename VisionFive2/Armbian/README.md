# Armbian VisionFive 2 Version Test Report

## Test Environment

### Operating System Information

- System Versions: Armbian Noble Minimal & Armbian Jammy Xfce
- Download Link: [https://www.armbian.com/visionfive2/](https://www.armbian.com/visionfive2/)
- Installation Guide: [https://www.armbian.com/visionfive2/](https://www.armbian.com/visionfive2/)

### Hardware Information

- StarFive VisionFive 2
- 1 x USB Power Adapter
- 1 x USB-A to C or C to C cable
- 1 x microSD card
- 1 x USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- 3 x DuPont wires
- Optional: Monitor/Capture card & HDMI cable (for testing Jammy version Xfce desktop)

## Installation Steps

### Extracting and Flashing Image to microSD Card

Assuming `/dev/sdc` is the storage card.

```bash
wipefs -af /dev/sdc
# Jammy Xfce
xzcat Armbian_community_24.5.0-trunk.278_Visionfive2_jammy_edge_5.15.0_xfce_desktop.img.xz | sudo dd of=/dev/sdc iflag=fullblock status=progress bs=4M
# Edge minimal
xzcat Armbian_community_24.5.0-trunk.278_Visionfive2_noble_edge_5.15.0_minimal.img.xz | sudo dd of=/dev/sdc iflag=fullblock status=progress bs=4M
```

### Boot Mode Selection

StarFive VisionFive 2 offers multiple boot modes, which can be configured using onboard DIP switches before powering on; the board itself is also labeled.

To boot the openKylin image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require firmware updates in the Flash beforehand. If booting fails, please refer to the official documentation for firmware upgrading: [Updating SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### Logging into the System

Log into the system via serial console.

Upon booting up, the system will prompt the user to manually configure the username, password, timezone, language, etc.

For Xfce version, configuration must be completed before entering the desktop. Configuration can be done via serial console or, if a keyboard and monitor are connected, via keyboard.

## Expected Outcome

The system should boot up successfully and allow login through the graphical interface or serial console.

## Actual Outcome

Both Xfce and Minimal versions of the system boot up successfully, and login can be achieved through the graphical interface or serial console.

### Boot Information

```log
root@visionfive2:~# uname -a
Linux visionfive2 5.15.0-edge-starfive2 #1 SMP Fri Mar 1 15:21:08 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
root@visionfive2:~# cat /etc/os-release 
PRETTY_NAME="Armbian_community 24.5.0-trunk.278 noble"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://github.com/armbian/build"
SUPPORT_URL="https://community.armbian.com/"
BUG_REPORT_URL="https://github.com/armbian/community/issues"
PRIVACY_POLICY_URL="https://duckduckgo.com/"
UBUNTU_CODENAME=noble
LOGO="armbian-logo"
ARMBIAN_PRETTY_NAME="Armbian_community 24.5.0-trunk.278 noble"
root@visionfive2:~# 
```

Xfce Version Screen Recording (From flashing image to system login):

![asciicast](https://asciinema.org/a/pCI6icBzsw2UrqNN5kL20LUxH)

Xfce Screenshot:

![alt text](image.png)

Screen Recording for Xfce:

[https://github.com/ruyisdk/support-matrix/assets/17025286/14c27bbd-5477-426b-a3e4-85cca5f5eabd](https://github.com/ruyisdk/support-matrix/assets/17025286/14c27bbd-5477-426b-a3e4-85cca5f5eabd)

Minimal Version Screen Recording (From flashing image to system login):

![asciicast](https://asciinema.org/a/kLOG9FnxGs9AnXpZqpjDJeiNo)

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
