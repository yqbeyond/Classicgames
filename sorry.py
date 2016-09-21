#-*- encoding: utf-8 -*-
count = 100000
sorry = u'对不起'
num_map = {
        0: u'零',
        1: u'一',
        2: u'二',
        3: u'三',
        4: u'四',
        5: u'五',
        6: u'六',
        7: u'七',
        8: u'八',
        9: u'九',
        }

name_map = {
        0: u'',
        1: u'十',
        2: u'百',
        3: u'千',
        4: u'万',
        8: u'亿',
        }

def get_digits (num):
    res = []
    while num != 0:
        res.append(num % 10)
        num /= 10
    return res

for i in range(1, count + 1): 
    digits = get_digits(i)
    digits_len = len(digits)
    msg = ""
    flag = False
    for i in range(0, digits_len):
        if i % 4 == 0:
            msg = name_map[i] + msg
        if digits[i] == 0 and flag == False:
            msg = u'零' + msg
            flag = True
            continue
        if digits[i] != 0:
            msg = num_map[digits[i]] + name_map[i % 4] + msg
            flag = False

    if msg[:2] == u'一十':
        msg = msg[1:]
    if msg[-1] == u'零':
        msg = msg[:-1]
    msg = u'第' + msg + u'遍： ' + sorry
    print msg
        
