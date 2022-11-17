import FinanceDataReader as fdr
from lxml import etree
import requests
from bs4 import BeautifulSoup


#다음 finance에서 json으로 market_cap 받아온다.
url = "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020101"
response = requests.get(url)
kospi50 = []

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    dom = etree.HTML(str(soup))
    
    # for i in range(1,50):
    #     xpath  = '//*[@id="jsMdiContent"]/div/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{}]/td[1]'.format(i);
    #     print(dom.xpath(xpath))
