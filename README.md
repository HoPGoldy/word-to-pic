# word-to-pic
使用PIL库将一段文本转换为图片

## 依赖安装

本项目依赖于PIL库

cd至根目录下使用cmd键入下列命令来安装依赖

```pip3 install -r requirements.txt```

## 运行测试用例

cd至根目录下使用cmd键入如下命令

```python run.py```

若输出**创建成功**并在根目录下找到内容为**test str**的result.jpg文件则表明运行成功

## 方法说明

### transform(word, size, font_size, save_path)

参数：

1. word(字符串类型): 想要转换的字符串 **默认**：Hello World

2. size(元组类型): 图片的大小 **默认**：300 * 150

3. font_size(整数类型): 字体大小，若该大小下的文本长度超过图片长度，则自动适配至适合大小 **默认**：68

4. save_path(字符串类型): 想要保存到的路径 **默认**：./result.jpg

返回值:

1. True: 创建成功

2. False: 创建失败
