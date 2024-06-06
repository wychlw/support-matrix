
# Milk-V Duo 256m

## Test Environment

### Operating System Information

- BuildRoot & FreeRTOS
  - Download link: [Milk-V Duo BuildRoot SDK with FreeRTOS](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
    - Official BuildRoot SDK provided by Milk-V, including FreeRTOS
  - Installation reference: [Milk-V Duo BuildRoot SDK Installation Guide](https://github.com/milkv-duo/duo-buildroot-sdk)
- Debian
  - Download link: [Debian for SG2002](https://github.com/Fishwaldo/sophgo-sg200x-debian)
  - Installation reference: [Debian Installation Guide](https://github.com/Fishwaldo/sophgo-sg200x-debian)
- RT-Thread
  - Source code link: [RT-Thread on GitHub](https://github.com/RT-Thread/rt-thread)
  - Installation reference: [RT-Thread Installation Guide](https://github.com/RT-Thread/rt-thread/blob/6101f1fd29374ac69c107e3cfeadfa06b0c901f9/bsp/cvitek/cv18xx_risc-v/README.md)

### Hardware Development Board Information

- Milk-V Duo (256M, SG2002)

## Test Results

| Software Category          | Package Name | Test Results (Test Report)                  |
|----------------------------|--------------|--------------------------------------------|
| BuildRoot Image Boot       | N/A          | [Success][BuildRoot]                        |
| FreeRTOS Boot              | N/A          | [Success][FreeRTOS] (included in BuildRoot image) |
| Debian Image Boot          | N/A          | [Success][Debian]                           |
| RT-Thread Image Build & Boot | N/A        | [Success][RT-Thread]                        |
| Zephyr Image Build & Boot  | N/A          | [Success][Zephyr]                          |
  
[BuildRoot]: ./BuildRoot/README.md
[Debian]: ./Debian/README.md
[RT-Thread]: ./RT-Thread/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[Zephyr]: ./Zephyr/README.md

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
