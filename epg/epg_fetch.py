import requests
import lzma

class MyException(Exception):
    pass

urls = ['http://www.xmltvepg.nl/rytecERO.xz',
    'http://epgspot.com/rytec_epg/rytecERO.xz']

for url in urls:
    res = requests.get(url)
    if res.status_code == 200:
        print(f'{res.url} - Połączono')
        break
    else:
        continue
if res.status_code != 200:
    raise MyException('Błąd pobierania')


open('rytecERO.xz', 'wb').write(res.content)
t = lzma.open('rytecERO.xz').read()

epg = open('adult.xml', 'wb')
print('Zakończono tworzenie xml')
epg.write(t)