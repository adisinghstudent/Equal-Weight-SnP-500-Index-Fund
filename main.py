import numpy as np
import pandas as pd
import requests
import math
import xlsxwriter


#importing our list of stocks
stocks = pd.read_csv('sp_500_stocks.csv')
print(stocks)