import requests
from bs4 import BeautifulSoup
def blacklist(qq):
    url = 'https://yunhei.qimeng.fun/'
    params = {
        'qq': qq
    }
    html = requests.post(url, params)
    html=html.text
    soup = BeautifulSoup(html,features="lxml")
    qq=soup.find_all('label')[0]
    # print(re.findall(r'\d+', str(qq))[0])
    qq=soup.find_all('label')
    if str(qq[1]) == '<label>上黑等级：</label>':
        qq=soup.find_all('font')
        return [str(qq[1]).replace('<font color="#FF6600">','').replace('</font>','').replace('<font color="#FF6600">','').replace('</font>',''),str(qq[2]).replace('<font color="#FF6600">','').replace('</font>',''),str(qq[3]).replace('<font color="#FF6600">','').replace('</font>','')]
    else:   
        qq=soup.find_all('font')
        return [str(qq[1]).replace('<br/>','').replace('</label>','').replace('<label>','').replace('<font color="blue">','').replace('<font color="green">','').replace('</font>','')]