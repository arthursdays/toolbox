import cv2
import os
import numpy as np
from multiprocessing import Pool

srcdir = '..\\yinxiebing\\cut_images'
dstdir = '..\\yinxiebing\\augmented_gaussian_noise_weighted'


def gaussianNoise(srcdir, dstdir, imgfile, sigma):
    if os.path.isfile('{}_g{}.jpg'.format(os.path.join(dstdir, imgfile.split('.')[0]), sigma)):
        print('{}_g{}.jpg already exists'.format(os.path.join(dstdir, imgfile.split('.')[0]), sigma))
    else:
        image = cv2.imread(os.path.join(srcdir, imgfile))
        hsl_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
        h, l, s = cv2.split(hsl_image)
        row, col, ch = image.shape
        mean = 0
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        lvalue = np.zeros(image.shape, np.float16)
        for i in range(row):
            for j in range(col):
                lvalue[i, j, :] = l[i, j]/320

        # print(gauss)
        # print(lvalue)
        # cv2.imshow('normal', image)
        noisy = image + np.multiply(gauss, lvalue)
        # noisy = image + gauss
        noisy = noisy.astype(np.uint8)
        print('Saving {}_g{}.jpg ...'.format(os.path.join(dstdir, imgfile.split('.')[0]), sigma))
        # cv2.imshow('noisy', noisy)
        cv2.imwrite('{}_g{}.jpg'.format(os.path.join(dstdir, imgfile.split('.')[0]), sigma), noisy)


if __name__ == '__main__':
    p = Pool(12)
    print('Parent process (#{}) started'.format(os.getpid()))
    for imgfile in os.listdir(srcdir):
        for sigma in range(0, 51, 5):
            p.apply_async(gaussianNoise, args=(srcdir, dstdir, imgfile, sigma))
            # gaussianNoise(srcdir, dstdir, imgfile, sigma)
    p.close()
    p.join()

    # gaussianNoise(srcdir, dstdir, "2009_7_14 076_JinZhanQiBanKuai_2_28,19_2032,1276.jpg", 49)
    # cv2.waitKey(0)
    print("All processes done!")
    # cv2.imshow('noisy image', gaussianNoise(image, 50))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()