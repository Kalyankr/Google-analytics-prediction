import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import datetime as datetime
import json
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
%matplotlib inline

from plotly import tools
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GroupKFold
from sklearn import model_selection, preprocessing, metrics
import lightgbm as lgb
from sklearn import metrics
import gc
gc.enable()
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999
import os
print(os.listdir("../input"))
