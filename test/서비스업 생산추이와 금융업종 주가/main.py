# 김영익교수의 책중 서비스업 생산 추이와 금융업종 주가의 상관관계를 나타낸그림
# ============== 목표 ==============
# 서비스업 생산 추이의 전년동월비 3개월 이동평균 와 코스피의 상관관계를 분석하여 상관계수를 계산 

import os
import pandas 
import scipy.stats as scs

# 1. 데이터를 불러온다 2001.01 ~ 2022.09
data_dir = os.path.dirname(os.path.abspath(__file__))+"/Data/"
bank_kospi = pandas.read_csv(data_dir+"코스피_산업별_주가지수_20221026160822.csv", encoding='cp949')
service = pandas.read_csv(data_dir+"산업별_서비스업생산지수__2015100.0__20221026161353.csv", encoding='cp949')


# 2. 상관계수 계산 메소드가 읽을수 있게 dataframe을 list로 변환한다.
bank_kospi = bank_kospi.values.tolist()[0][1:]
service = service.values.tolist()[0][1:]


# 3. 서비스업 생산 추이의 전년동월비 3개월 이동평균값을 구한다.
res = []
for index in range(14,len(service)):
    month3 = 0
    for dk in range(-2, 0):
        month3 += service[index+dk] - service[index-12+dk]
    res.append(round(month3/3, 2))


# 4. 피어슨, 스피어만, 켄달타우 공식으로 상관계수를 계산한다.
print("피어슨   : ", scs.pearsonr(bank_kospi, res).statistic)          #피어슨
print("스피어만 : ", scs.spearmanr(bank_kospi, res).correlation)     # 스피어만
print("켄달타우 : ", scs.kendalltau(bank_kospi, res).correlation)    # 켄달타우


# 추가) 김영익교수가 자료에 나타낸 서비스생산지수 전년동월 3개월 이동평균과 금융업계 주가
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(20,5))
ax1 = fig.subplots()
plt.xticks(size = 5, rotation = 45)
ax1.plot( res , color='green')
ax2 = ax1.twinx()
ax2.plot( bank_kospi, color= 'red')
plt.show()