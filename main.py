import requests
import time
import os


def getRes(year, month):
    url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=" + str(year) + "%E5%B9%B4"+ str(month) +"%E6%9C%88&resource_id=39043&ie=utf8&format=json&tn=wisetpl"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        temp = requests.get(url=url, headers=headers)
        resp = temp.text
        return resp
    except BaseException:
        return False

def saveFile(filename, content):
    try:
        basedir = os.path.dirname(__file__)
        with open(file=basedir + "./file/" + filename, mode="x", encoding="utf-8") as f:
            f.write(content)
            f.close()
            return True
    except BaseException:
        return False


if __name__ == "__main__":
    start_year = 1970
    end_year = 2100 + 1
    months = [2, 5, 8, 11]
    for i in range(start_year, end_year):
        for j in range(0, len(months)):
            temp = "{0}年{1}月".format(i, months[j])
            status = saveFile(temp + ".txt", getRes(i, months[j]))
            if status != False:
                print("爬取成功：" + temp)
            else:
                print("出现错误，已退出。")
                exit(0)
            time.sleep(2)
    exit(0)
  
