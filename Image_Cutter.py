import cv2
import os
import multiprocessing
import numpy as np
import pandas as pd
import re

file = open("..\\yinxiebing\\yinxiebing.csv", encoding='utf8')
your_data_path = '..\\yinxiebing\\img_data'


file.readline()
# lines = file.readlines()
# print (lines)


def cut_image(line):
    # print(line)
    # print(line.split(","))
    img_name = line.split(',')[1]
    img = cv2.imread(os.path.join(your_data_path, img_name))
    # print(line.split('"[')[1].split(']"')[0])
    parse_info = line.split('"[')[1].split(']"')[0]
    # print(line.split(',')[-2])
    dr_id = line.split(',')[-2]

    # state=''
    # x=0
    # y=0
    # w=0
    # h=0

    # print (parse_info)

    for record in parse_info.split('],["'):
        # print("{}: {}_{}".format(img_name, record, record.count('],[')))
        # if record.count('],[') == 1:
        #     print(record)
        #     state = record.split('"",')[0].split('"')[-1]
        #     x = (int)(record.split('[[')[1].split(',')[0])
        #     y = (int)(record.split('],[')[0].split(',')[-1])
        #     w = (int)((float)(record.split('],[')[1].split(',')[0]))
        #     h = (int)((float)(record.split(']]')[0].split(',')[-1]))
        #     print("Saving {}...".format(os.path.join("..\\yinxiebing\\cut_images",
        #                                         "{}_{}_{}_{},{}_{},{}.jpg".format(
        #                                             img_name.split('.jpg')[0],
        #                                             state,
        #                                             dr_id,
        #                                             x,
        #                                             y,
        #                                             w,
        #                                             h))))
        #
        #     cv2.imwrite(os.path.join("..\\yinxiebing\\cut_images",
        #                         "{}_{}_{}_{},{}_{},{}.jpg".format(
        #                             img_name.split('.jpg')[0],
        #                             state,
        #                             dr_id,
        #                             x,
        #                             y,
        #                             w,
        #                             h)),
        #                 img[y:y+h, x:x+w])
        if record.count('],[') > 1:
            record_list = record.split(',[[')[1].split(']],')[0].split('],[')
            # print(record_list)
            state = record.split('"",')[0].split('"')[-1]
            min_x = (int)(record_list[0].split(',')[0])
            min_y = (int)(record_list[0].split(',')[1])
            max_x = (int)(record_list[0].split(',')[0])
            max_y = (int)(record_list[0].split(',')[1])
            for point in record_list:
                min_x = (int)(point.split(',')[0]) if ((int)(point.split(',')[0]) < min_x) else min_x
                min_y = (int)(point.split(',')[1]) if ((int)(point.split(',')[1]) < min_y) else min_y
                max_x = (int)(point.split(',')[0]) if ((int)(point.split(',')[0]) > max_x) else max_x
                max_y = (int)(point.split(',')[1]) if ((int)(point.split(',')[1]) > max_y) else max_y
            # print('[{},{}],[{},{}]'.format(min_x, min_y, max_x, max_y))
            print("Saving {}...".format(os.path.join("..\\yinxiebing\\cutted_images",
                                                    "{}_{}_{}_{},{}_{},{}.jpg".format(
                                                        img_name.split('.jpg')[0],
                                                        state,
                                                        dr_id,
                                                        min_x,
                                                        min_y,
                                                        max_x - min_x,
                                                        max_y - min_y))))

            cv2.imwrite(os.path.join("..\\yinxiebing\\cutted_images",
                                    "{}_{}_{}_{},{}_{},{}.jpg".format(
                                        img_name.split('.jpg')[0],
                                        state,
                                        dr_id,
                                        min_x,
                                        min_y,
                                        max_x - min_x,
                                        max_y - min_y)),
                            img[min_y:max_y, min_x:max_x])

if __name__ == '__main__':
    print("Parent process {}".format(os.getpid()))
    p = multiprocessing.Pool(24)

    for line in file.readlines():
        # p.apply_async(cut_image, args=(line, ))
        cut_image(line)
    print("Waiting all subprocesses done...")

    # p.close()
    # p.join()
    print("All subprocesses done!")


