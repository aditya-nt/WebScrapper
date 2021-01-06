import requests
from bs4 import BeautifulSoup
import json



data = {}
data['shlok'] = []

verse = [0,47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]


for i in range(18,19):
    for j in range(1,verse[i]+1):
        # vgm_url = 'https://www.gitasupersite.iitk.ac.in/srimad?enable_autoplay=1&&language=dv&field_chapter_value='+str(i)+'&field_nsutra_value='+str(j)
        # html_text = requests.get(vgm_url).text
        # soup = BeautifulSoup(html_text, 'html.parser')
        # subc = soup.find_all('font')
        # subc1 = subc[1]
        # c = subc1.text.split('।।')
        # shloktext = c[0]
        # c2 = c[len(c)-2]
        # # print(subc1.text)
        # ch,sh = 1,2# c2.split('.')
        data['shlok'].append({
            # 'text': subc1.text,
            'chapter_no': i,
            'shlok_no': j
        })
        print(i,".",j)

with open('data3.json', 'w') as outfile:
    json.dump(data, outfile)


