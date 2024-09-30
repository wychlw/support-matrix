# Test template

这里是测试模板，用于测试文档的自动生成。

目前以下的board有这个模板：
- BPI-F3

## 说明

模板如下：

### front matter

```yaml
# Definations for README metadata

definitions:
  status_enum:
    type: string
    enum: &STATUS_ENUM
      - none
      - wip
      - cft
      - cfh
      - cfi
      - partial
      - basic
      - good

# General info
sys: string        # System name
sys_ver: string    # System version
sys_var: string?   # System variant

# Doc info
status: *STATUS_ENUM
last_updated: timestamp   # Last update

# image info
image_link: string   # Image link
username: string     # Username
password: string     # Password
```

### 替换

`[[asciicast]]`

替换为一个asciinema的链接。

`[[version]]`

替换为版本号。

`[[image_link]]`

替换为镜像链接。

`[[image_file_zip]]`

替换为镜像文件名（压缩文件）。

`[[image_file_img]]`

替换为镜像文件名（img文件）。

`[[username]]`

替换为用户名。

`[[password]]`

替换为密码。

`[[info]]`

替换为系统信息输出
