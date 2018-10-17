import os

data_path = '..\\yinxiebing\\cut_images\\'

typedict = {
    'DianDiZhuang': 0,
    'FanXiangXing': 0,
    'GuanJieBingXing': 0,
    'HongPiBingXing': 0,
    'JiaYinXieBing': 0,
    'NongBaoXing': 0,
    'TouPiYinXieBing': 0,
    'JinZhanQiBanKuai': 0,
    'WenDingQiDaBanKuai': 0,
    'WenDingQiXiaoBanKuai': 0,
    'XiaoTuiQiBanKuai': 0,
}

for file in os.listdir(data_path):
    atype = file.split('_')[-4]
    # print(atype)
    if atype in typedict:
        typedict[atype] += 1
    print(typedict)
