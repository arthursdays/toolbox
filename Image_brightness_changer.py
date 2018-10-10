import cv2
import os
import multiprocessing

srcdir = '..\\yinxiebing\\cut_images'
destdir = '..\\yinxiebing\\augmented_hsv'


def changeBrightness(imgpath):
    img=cv2.imread(imgpath)
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for value in range(0, 101, 20):
        h, s, v = cv2.split(hsv)
        v2 = v.copy()
        u_lim = 255 - value
        l_lim = value
        v[v > u_lim] = 255
        v2[v2 < l_lim] = 0
        v[v <= u_lim] += value
        new_hsv_p = cv2.merge((h, s, v))
        v2[v2 >= l_lim] -= value
        new_hsv_n = cv2.merge((h, s, v2))
        # new_hsv = hsv[:, :, 2] + 2
        print('Saving {}_({}).jpg ...'.format(
            os.path.join(destdir,
                         imgpath.split('\\')[-1].split('.')[0]),
            value))
        cv2.imwrite('{}_({}).jpg'.format(
            os.path.join(destdir,
                         imgpath.split('\\')[-1].split('.')[0]),
            value),
            cv2.cvtColor(new_hsv_p, cv2.COLOR_HSV2BGR))
        if value != 0:
            print('Saving {}_(-{}).jpg ...'.format(
                os.path.join(destdir,
                             imgpath.split('\\')[-1].split('.')[0]),
                value))
            cv2.imwrite('{}_(-{}).jpg'.format(
                os.path.join(destdir,
                             imgpath.split('\\')[-1].split('.')[0]),
                value),
                cv2.cvtColor(new_hsv_n, cv2.COLOR_HSV2BGR))


if __name__ == "__main__":
    print("Parent process {}".format(os.getpid()))
    p = multiprocessing.Pool(24)

    for img in os.listdir(srcdir):
        p.apply_async(changeBrightness, args=(os.path.join(srcdir, img), ))
        # changeBrightness(os.path.join(srcdir, img))

    print("Waiting all subprocesses done...")

    p.close()
    p.join()
    print("All subprocesses done!")
