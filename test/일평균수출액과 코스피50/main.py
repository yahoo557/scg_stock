import FinanceDataReader as fdr
import pandas_datareader as pdr
import scipy.stats as scs
from pykrx import stock
import datetime 
import os
import pandas
# ============== 목표 ==============
data_dir = os.path.dirname(os.path.abspath(__file__))+"/Data/"
# kospi = pandas.read_csv(data_dir+"코스피_지수_20221022235916.csv", encoding='cp949')
export = pandas.read_csv(data_dir+"수출입총괄_20221023000003.csv", encoding='cp949')

# 일평균 수출액과 코스피 50의 상관계수를 시기별로 2차원 배열로 나타낸다.
kospi50_code = [ '005930', '373220', '000660', '207940', '051910', '006400', '005935', '005380', '035420', '000270', 
                '068270', '035720', '005490', '028260', '012330', '105560', '055550', '003670', '034730', '066570',
                '323410', '003550', '032830', '033780', '010130', '015760', '086790', '247540', '017670', '091990',
                '034020', '259960', '009150', '011200', '051900', '329180', '036570', '018260', '010950', '003490', 
                '030200', '009830', '000810', '316140', '377300', '066970', '024110', '011070', '302440', '090430' ]

def getMonthlyTotal(code):
    kospi_df = fdr.DataReader( 'code', '2001', '202209')
    kospi_month = []
    
    # 월별 시가총액평균
    ㄴthis_month = kospi_df.index[0].month
    cnt = 0
    temp = 0
    for i in range(len(kospi_df)):
        if kospi_df.index[i].month == this_month :
            temp += kospi_df['Close'][i]*kospi_df['Volume'][i]
            cnt += 1
        else :
            print(int(temp/cnt))
            kospi_month.append(int(temp/cnt))
            this_month = kospi_df.index[i].month
            cnt = 1
            temp = kospi_df['Close'][i]*kospi_df['Volume'][i]
    return kospi_month


result_matrix = []
for code in kospi50_code:
    
    print("피어슨   : ", scs.pearsonr(getMonthlyTotal(code), export).statistic)


