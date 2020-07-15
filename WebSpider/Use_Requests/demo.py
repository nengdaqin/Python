import re
import pandas as pd
import requests


def get_one_page(url):
    headers = {
        'Cookie': 'uuid_n_v=v1; uuid=CCE3C0B0C51311EAB2AE8B45D9A9C8655B2956FD5BCC401B8BB356B82E9D3199;'
                  ' _csrf=fa5a094a5e2fd185e0d1e5133a657fd924f2ad206e5477d9630981f530955cc5; '
                  '_lxsdk_cuid=173488b169bc8-08f171e9b81e3f-4353760-151800-173488b169bc8; '
                  '_lxsdk=CCE3C0B0C51311EAB2AE8B45D9A9C8655B2956FD5BCC401B8BB356B82E9D3199; '
                  'mojo-uuid=71233a51d2b75e888d8068d8ba85a4f3; '
                  'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1594649942,1594704685; '
                  'mojo-session-id={"id":"ea498b73564cf40b84a259b1567ed602","time":1594704685060}; '
                  '_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; '
                  'mojo-trace-id=3; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1594704687; '
                  '__mta=209083693.1594649942614.1594704685269.1594704687049.5; '
                  '_lxsdk_s=1734bce6818-985-517-74e%7C%7C6',

        'Host': 'maoyan.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return 'Crawl Failed'

def parse_html(html):
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*?star.*?主演：(.*?)</p>'
                         r'.*?上映时间：(.*?)</p>', re.S)
    # pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*?star.*?主演：(.*?)</p>'
    #                      r'.*?releasetime.*?上映时间：(.*?)</p>', re.S)
    results = re.findall(pattern, html)
    return results

html1 = get_one_page("https://maoyan.com/board")
result = parse_html(html1)
print(result)

# data = pd.DataFrame([], columns=['Name', 'Actors', 'Date', 'Region'])
#
# for item in result:
#     rank = item[0]
#     name = item[1]
#     actors = item[2].strip()
#     temp = item[3].split('(')
#     if len(temp) == 1:
#         date = temp[0]
#         data.loc[rank, 'Date'] = date
#     else:
#         date = temp[0]
#         region = temp[1][:-1]
#         data.loc[rank, 'Date'] = date
#         data.loc[rank, 'Region'] = region
#     data.loc[rank, 'Name'] = name
#     data.loc[rank, 'Actors'] = actors
