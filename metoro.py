import requests
import json


URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
TIMEOUT = 10
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"}


#サイトにアクセスする
try:
    result = requests.get(URL, timeout=TIMEOUT, headers=HEADERS)
    result.raise_for_status()
except Exception as e:
    print("ERROR_DOWNLOAD:{}".format(e))
else:
    print(result.content)

    content = result.content

    print(type(content))

    #jsonのbyteデータを辞書型に変換
    print(json.loads(content))

