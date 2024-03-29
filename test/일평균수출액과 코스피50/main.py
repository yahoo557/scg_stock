import FinanceDataReader as fdr
import pandas_datareader as pdr
import scipy.stats as scs
import os
import pandas 


# ============== 목표 ==============
# 일평균 수출액과 코스피 50의 상관계수를 시기별로 2차원 배열로 나타낸다.

# 1. csv 데이터를 읽어온다. (2000.02 ~ 2022.09)
data_dir = os.path.dirname(os.path.abspath(__file__))+"/Data/"
export = pandas.read_csv(data_dir+"수출입총괄_20221023000003.csv", encoding='UTF8')

# export = export.values.tolist()[0][1:]


# 2. 코스피 50 각 종목의 월별 시가총액 평균을 구한다.
kospi50_code = [ '005930', '373220', '000660', '207940', '051910', '006400', '005935', '005380', '035420', '000270', 
                '068270', '035720', '005490', '028260', '012330', '105560', '055550', '003670', '034730', '066570',
                '323410', '003550', '032830', '033780', '010130', '015760', '086790', '247540', '017670', '091990',
                '034020', '259960', '009150', '011200', '051900', '329180', '036570', '018260', '010950', '003490', 
                '030200', '009830', '000810', '316140', '377300', '066970', '024110', '011070', '302440', '090430' ]

print(fdr.DataReader('373220', '2000-02-01', '2022-10-05'))
# 3. 각 연도 마다 월별 시가총액의 평균을 구한다.
def getMonthlyTotal(code,year):
    
    if(year == 0):
        kospi_df = fdr.DataReader(code, '2000-02-01', '2022-10-05');
    else:
        kospi_df = fdr.DataReader(code, start , end)
    
    kospi_month = []
    
    # 월별 시가총액평균
    this_month = kospi_df.index[0].month
    cnt = 0
    temp = 0

    
    for i in range(len(kospi_df)):
        if kospi_df.index[i].month == this_month :
            temp += kospi_df['Close'][i]*kospi_df['Volume'][i]/1000000
            cnt += 1
        else :
            kospi_month.append(int(temp/cnt))
            this_month = kospi_df.index[i].month
            cnt = 1
            temp = kospi_df['Close'][i]*kospi_df['Volume'][i]/1000000

    return kospi_month

# 4. 각 연도별 일평균 수출액을 구한다.
def getExportYear(year):
    export = pandas.read_csv(data_dir+"수출입총괄_20221023000003.csv", encoding='UTF8')

    for i in range(1, len(export.columns)):
        if(export.columns[i][:4]==str(year)):
            return export.values.tolist()[0][i:i+12]
       

    
    





# 3,4에서 구한 데이터로 상관계수를 구해서 dataframe에 저장한다.
df = pandas.DataFrame(index=range(2001, 2022), columns=kospi50_code);
for year in range(2001, 2022):
    for code in kospi50_code:
        print("len(getMonthlyTotal(code,str(year))) = ", len(getMonthlyTotal(code,str(year))) )
        print("len(getExportYear(year)) = ", len(getExportYear(year)) )
        # df[year][code] = scs.pearsonr(getMonthlyTotal(code,str(year)), getExportYear(year)).statistic

# print(df)




