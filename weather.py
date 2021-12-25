import requests,bs4

#ここに取得したい地域のURLを指定。(東京であれば /13/4410.html、広島であれば /34/6710.html)

LOCALE  = [
        {"area":"広島","url":"/34/6710.html"},
        {"area":"東京","url":"/13/4410.html"},
        ]


#URL = "https://weather.yahoo.co.jp/weather/jp/34/6710.html"
URL = "https://weather.yahoo.co.jp/weather/jp" + LOCALE[0]["url"]
TIMEOUT = 10
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"}


#サイトにアクセスする
try:
    result = requests.get(URL, timeout=TIMEOUT, headers=HEADERS)
    result.raise_for_status()
except Exception as e:
    print("ERROR_DOWNLOAD:{}".format(e))
else:
    soup    = bs4.BeautifulSoup(result.content,"html.parser")

    data    = soup.select(".forecastCity")
    print(data)

    print("==========================================")

    """
    #.select()で使うのはCSSセレクタ。JavaScriptが発動しないので、場合によってはCSSセレクタコピペしても抜き取れないことがあるので注意。
    elems   = soup.select(".forecastCity > table > tr > td:nth-child(1) > div > .pict")
    print(elems)

    for elem in elems:
        print(elem.text.strip())
    """

    #".forecastCity > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > p:nth-child(2)"

    message = LOCALE[0]["area"] + "の今日と明日の天気\n\n"


    message += "今日\n"

    #今日の天気の取得
    today_weather_elem  = soup.select("div.forecastCity > table > tr > td:nth-child(1) > div > p.pict")

    for t in today_weather_elem:
        print(t.text.strip())
        message += t.text.strip() + "\n"


    #今日の最高気温の取得
    today_temp_high_elem    = soup.select("div.forecastCity > table > tr > td:nth-child(1) > div > ul.temp > li.high")

    for t in today_temp_high_elem:
        print(t.text.strip())
        message += "最高気温:" + t.text.strip() + "\n"

    #今日の最低気温の取得
    today_temp_low_elem     = soup.select("div.forecastCity > table > tr > td:nth-child(1) > div > ul.temp > li.low")

    for t in today_temp_low_elem:
        print(t.text.strip())
        message += "最低気温:" + t.text.strip() + "\n\n"


    message += "明日\n"

    #明日の天気の取得
    tommorow_weather_elem   = soup.select("div.forecastCity > table > tr > td:nth-child(2) > div > p.pict")

    for t in tommorow_weather_elem:
        print(t.text.strip())
        message += t.text.strip() + "\n"

    #明日の最高気温の取得
    tommorow_temp_high_elem = soup.select("div.forecastCity > table > tr > td:nth-child(2) > div > ul.temp > li.high")

    for t in tommorow_temp_high_elem:
        print(t.text.strip())
        message += "最高気温:" + t.text.strip() + "\n"

    #明日の最低気温の取得
    tommorow_temp_low_elem  = soup.select("div.forecastCity > table > tr > td:nth-child(2) > div > ul.temp > li.low")

    for t in tommorow_temp_low_elem:
        print(t.text.strip())
        message += "最低気温:" + t.text.strip() + "\n\n"




print(message)



"""
import sendgrid
from sendgrid.helpers.mail import *

SENDGRID_API    = ""

sg          = sendgrid.SendGridAPIClient(api_key=SENDGRID_API)
from_email  = Email("送信元のメールアドレス")
to_email    = To("宛先のメールアドレス")
subject     = "メールの件名"
content     = Content("text/plain", message)
mail        = Mail(from_email, to_email, subject, content)
response    = sg.client.mail.send.post(request_body=mail.get())
"""


