# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 7:56
# @Author  : HoPGoldy

import WordToPic

if __name__ == '__main__':
    if WordToPic.transform('test str'):
        print('创建成功')
    else:
        print('创建失败')