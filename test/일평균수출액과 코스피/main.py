# ============== 목표 ==============
# 거시경제 지표와 주가의 상관관계를 분석하여 상관계수를 계산 

import os
import pandas 
import scipy.stats as scs


# 1. csv 데이터를 읽어온다. (2000.02 ~ 2022.09)
data_dir = os.path.dirname(os.path.abspath(__file__))+"/Data/"
kospi = pandas.read_csv(data_dir+"코스피_지수_20221022235916.csv", encoding='cp949')
export = pandas.read_csv(data_dir+"수출입총괄_20221023000003.csv", encoding='cp949')

x = kospi.columns.values.tolist()[1:] # 그래프에 사용할 x축 일시


# 2. 상관계수 계산 메소드가 읽을수 있게 dataframe을 list로 변환한다.
kospi = kospi.values.tolist()[0][1:]
export = export.values.tolist()[0][1:]


# 3. 피어슨, 스피어만, 켄달타우 공식으로 상관계수를 계산한다.
print("피어슨   : ", scs.pearsonr(kospi, export).statistic)          #피어슨
print("스피어만 : ", scs.spearmanr(kospi, export).correlation)     # 스피어만
print("켄달타우 : ", scs.kendalltau(kospi, export).correlation)    # 켄달타우


# 추가) 김영익교수가 자료에 나타낸 일평균 수출량과 코스피 그래프
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(20,5))
ax1 = fig.subplots()
plt.xticks(size = 5, rotation = 45)
ax1.plot( kospi, color='green')
ax2 = ax1.twinx()
ax2.plot( export, color= 'red')
plt.show()