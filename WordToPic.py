# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 7:51
# @Author  : HoPGoldy

from PIL import Image, ImageDraw, ImageFont


def transform(word='Hello World', size=(300, 150), font_size=68, save_path='./result.jpg'):
    try:
        img = Image.new("RGB", size, "#FFFFFF")
        drawer = ImageDraw.Draw(img)

        font = ImageFont.truetype('simhei.ttf', font_size + 5)
        img_width, font_width = 0, 0
        while img_width <= font_width:
            font_size -= 5
            font = ImageFont.truetype('simhei.ttf', font_size)
            img_width, img_height = img.size
            font_width, font_height = font.getsize(word)

        drawer.text([((img_width - font_width)/2), ((img_height - font_height)/2)], word, fill='#000000', font=font)
        img.save(save_path)

        return True
    except:
        return False
