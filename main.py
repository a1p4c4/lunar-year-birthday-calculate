import requests
import json


def getRes(year, month):
    url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=" + str(year) + "%E5%B9%B4"+ str(month) +"%E6%9C%88&resource_id=39043&ie=utf8&format=json&tn=wisetpl"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36"}
    try:
        temp = requests.get(url=url, headers=headers)
        resp = json.loads(temp.text)
        if len(resp['data']) == 0:
            return False
        else:
            return resp
    except(BaseException):
        return False


def getLunarBirthday(data, syear, smonth, sday):
    temp = []
    for i in range(0, len(data['almanac'])):
        if data['almanac'][i]['year'] == str(syear) and data['almanac'][i]['month'] == str(smonth) and data['almanac'][i]['day'] == str(sday):
            temp.append(data['almanac'][i]['lMonth'])
            temp.append(data['almanac'][i]['lDate'])   
            return  temp
        else:
            continue


def getSolarBirthday(data, lmonth, lday):
    for i in range(0, len(data['almanac'])):
        if data['almanac'][i]['lMonth'] == str(lmonth) and data['almanac'][i]['lDate'] == str(lday):
            return "{0}年{1}月{2}日".format(data['almanac'][i]['year'], data['almanac'][i]['month'], data['almanac'][i]['day'])
        else:
            continue


if __name__ == "__main__":
    sbirthday = input("输入国历出生日期（格式 yyyy-mm-dd 无前导零）：").split("-")
    target = input("输入目标年份（格式 yyyy）：")

    start = getRes(sbirthday[0], sbirthday[1])
    if start != False:
        lbirthday = getLunarBirthday(start['data'][0], sbirthday[0], sbirthday[1], sbirthday[2])
        print("农历：{0}月{1}".format(lbirthday[0], lbirthday[1]))

    end = getRes(target, sbirthday[1])
    if end != False:
        result = getSolarBirthday(end['data'][0], lbirthday[0], lbirthday[1])
        print(result)
