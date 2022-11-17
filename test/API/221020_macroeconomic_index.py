# Open API 통해 한국은행 경제통계시스템(ECOS) 데이터읽어오기
# https://bjecondata.blogspot.com/2019/08/open-api-ecos-ii.html

import datetime
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


# def ecosDownload(statCode statName, startDate, endDate):
    
