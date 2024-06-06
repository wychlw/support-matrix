
# Milk-V Duo S

## Test Environment

### Operating System Information

- BuildRoot & FreeRTOS
  - Download link: [Milk-V Duo BuildRoot SDK](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
    - Official BuildRoot SDK provided by Milk-V, includes FreeRTOS
  - Installation guide: [Milk-V Duo BuildRoot SDK Installation](https://github.com/milkv-duo/duo-buildroot-sdk)
- Apache NuttX RTOS
  - Source code links
    - NuttX: [NuttX Source Code](https://github.com/lupyuen2/wip-nuttx/tree/sg2000)
    - NuttX Apps: [NuttX Apps Source Code](https://github.com/lupyuen2/wip-nuttx-apps/tree/sg2000)
  - Installation guide: [NuttX SG2000 Installation](https://github.com/lupyuen/nuttx-sg2000)

### Hardware Development Board Information

- Milk-V Duo S (512M, SG2000)

## Test Results

| Software Category       | Package Name | Test Results (Test Report) |
|-----------------------|--------------|-------------------------|
| BuildRoot Image Boot     | N/A          | [Basic][BuildRoot]     |
| FreeRTOS Boot            | mailbox-test | [Basic][FreeRTOS]      |
| Apache NuttX Build & Boot| N/A          | [Basic, WIP][NuttX]    |
| Zephyr Image Build & Boot| N/A          | [Basic][Zephyr]        |

[BuildRoot]: ./BuildRoot/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[NuttX]: ./NuttX/README.md
[Zephyr]: ./Zephyr/README.md

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
