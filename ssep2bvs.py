import requests,re,os
print('''
ssid for exmaple:
    https://www.bilibili.com/bangumi/play/ss34230 (总之就是非常可爱)
    ssid:ss34230
epid for exmaple:
    https://www.bilibili.com/bangumi/play/ep63860 (干物妹小埋)
    epid:ep63860
''')
id=input('ss or ep id:')
if id.find('ss')==0:
    id_type='season_id='
    ida=id.replace('ss','')
else:
    id_type='ep_id='
    ida=id.replace('ep','')
print(id)
url='http://api.bilibili.com/pgc/view/web/season?'+id_type+ida
req=requests.get(url).json()
for bvid in req['result']['episodes']:
    print(bvid['share_copy'])
    print(bvid['bvid'])
    print('----------------------------------------')
    os.system('pause')
os.system('pause')
