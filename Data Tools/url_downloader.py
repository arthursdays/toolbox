import os
import requests
from multiprocessing import Pool


def save_url(url, subfoler='.', save_path='data'):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        }
        if not os.path.exists(os.path.join(save_path, subfoler)):
            print("Path {} does not exist, auto creating...".format(os.path.join(save_path, subfoler)))
            os.makedirs(os.path.join(save_path, subfoler))
        filename = url.split('/')[-1]
        print("Saving {}{}{}{}{}".format(save_path, os.sep, subfoler, os.sep, filename))
        savedest = "{}{}{}{}{}".format(save_path, os.sep, subfoler, os.sep, filename)
        data = requests.get(url, headers = headers)
        output = open(savedest, 'wb')
        output.write(data.content)
        output.flush()
        output.close()
    except IOError as e:
        print("IO error: ", e)
    except Exception as e:
        print("Unknown error occured: ", e)


if __name__=="__main__":
    file = open("../../imgurl.txt")
    p = Pool(128)

    while(True):
        url = file.readline()
        kind = file.readline()
        # print(url,kind)
        if not url or not kind: break
        # print("Hello")
        #save_url(url.strip(), subfoler=kind.strip(), save_path="..\\..\\yinxiebing\\derm101")
        p.apply_async(save_url, args=(url.strip(), kind.strip(), "..\\..\\yinxiebing\\derm101", ))

    p.close()
    p.join()
