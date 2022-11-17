# 소비자심리지수는 소비자동향조사의 26개 개별지수 중 소비자의 심리에 대한 종합적인 판단에 유용한 6개
# (현재생활형편CSI, 생활형편전망CSI, 가계수입전망CSI, 소비지출전망CSI, 현재경기판단CSI, 향후경기전망CSI) 개별지수를 활용한 합성지수이다.

# ============== 목표 ==============
# 소비자심리지수와 코스피의 상관관계를 분석하여 상관계수를 계산 

import os
import pandas 
import scipy.stats as scs

# 1. csv 데이터를 읽어온다. (2008.07 ~ 2022.09)
data_dir = os.path.dirname(os.path.abspath(__file__))+"/Data/"
kospi = pandas.read_csv(data_dir+"코스피_지수_20221022235916.csv", encoding='cp949')
costumer = pandas.read_csv(data_dir+"소비자동향조사_전국__월__2008.9__20221025233521.csv", encoding='cp949')

x = kospi.columns.values.tolist()[1:] # 그래프에 사용할 x축 일시


# 2. 상관계수 계산 메소드가 읽을수 있게 dataframe을 list로 변환한다.
kospi = kospi.values.tolist()[0][1:]
costumer = costumer.values.tolist()[0][1:]


# 3. 피어슨, 스피어만, 켄달타우 공식으로 상관계수를 계산한다.
print("피어슨   : ", scs.pearsonr(kospi, costumer).statistic)          #피어슨
print("스피어만 : ", scs.spearmanr(kospi, costumer).correlation)     # 스피어만
print("켄달타우 : ", scs.kendalltau(kospi, costumer).correlation)    # 켄달타우


# 추가) 김영익교수가 자료에 나타낸 소비자심리지수와 코스피 그래프
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(20,5))
ax1 = fig.subplots()
plt.xticks(size = 5, rotation = 45)
ax1.plot( kospi, color='green')
ax2 = ax1.twinx()
ax2.plot( costumer, color= 'red')
plt.show()