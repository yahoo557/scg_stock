import datetime
from pandas_datareader import data, wb

start = datetime.datetime(2012,10,22)
end = datetime.datetime(2022, 10, 22)
kospi = data.DataReader("^KS11", "yahoo",start, end)
print(kospi)
