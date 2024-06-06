# CanMV K230

## Test Environment

### Operating System Information

- Canaan Kendryte K230 Official CanMV Debian SDK
  - Download link: [https://kendryte-download.canaan-creative.com/developer/k230/canmv_debian_sdcard_sdk_1.3.img.gz](https://kendryte-download.canaan-creative.com/developer/k230/canmv_debian_sdcard_sdk_1.3.img.gz)
  - Reference installation document: [https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month08/Week3/CanMV-K230.md](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month08/Week3/CanMV-K230.md)
  
- Canaan Kendryte K230 Official CanMV Ubuntu SDK
  - Download link: [https://kendryte-download.canaan-creative.com/developer/k230/canmv_ubuntu_sdcard_1.3.img.gz](https://kendryte-download.canaan-creative.com/developer/k230/canmv_ubuntu_sdcard_1.3.img.gz)
  - Reference installation document: [https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month08/Week3/CanMV-K230.md](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month08/Week3/CanMV-K230.md)
  
- Fedora 38
  - Download link: [https://github.com/ruyisdk/mkimg-k230-rv64ilp32/releases](https://github.com/ruyisdk/mkimg-k230-rv64ilp32/releases)
  - Reference installation document: [https://developer.canaan-creative.com/k230/dev/zh/CanMV_K230_%E6%95%99%E7%A8%8B.html](https://developer.canaan-creative.com/k230/dev/zh/CanMV_K230_%E6%95%99%E7%A8%8B.html)
  
- RT-Thread
  - Download link: [https://github.com/kendryte/k230_sdk/releases/tag/v1.4](https://github.com/kendryte/k230_sdk/releases/tag/v1.4)
  - Reference installation document: [https://github.com/kendryte/k230_docs/blob/main/zh/01_software/board/K230_SDK_%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md](https://github.com/kendryte/k230_docs/blob/main/zh/01_software/board/K230_SDK_%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md)
  
### Hardware Development Board Information

- Canaan Kendryte K230

## Test Results

| Software Category        | Package Name | Test Result (Test Report)     |
|-------------|----------|------------------|
| Debian Image Boot | N/A      | [Success][K230Debian] (Vendor Image) |
| Ubuntu Image Boot | N/A      | [Success][K230Ubuntu] (Vendor Image) |
| Fedora Image Boot | N/A      | [Success][Fedora]               |
| RT-Thread Image Build and Boot | N/A      | [Success][RT-Thread] (Vendor Image)   |
| NuttX Image Build and Boot     | N/A      | [Success][NuttX]                 |

[K230Debian]: ./Debian/README.md
[K230Ubuntu]: ./Ubuntu/README.md
[Fedora]: ./Fedora/README.md
[RT-Thread]: ./RT-Thread/README.md
[NuttX]: ./NuttX/README.md

> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
