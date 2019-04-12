# data can be loaded into the load_df function for converting into csv from json 
# data can be found at (kaggle competitions download -c ga-customer-revenue-prediction) API, the data is in huge amount and can be have memory probelms. for that data can be loaded as chunks and can use effciently.

train_df = load_df()
test=load_df(csv_path='../input/test_v2.csv')
