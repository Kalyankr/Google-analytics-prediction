
#As the data contain some json formated columns, we can use the below code to convert such kind to CSV loaded formot.

json_data=["device","geoNetwork","totals","trafficSource"]
gc.enable()

features = ['channelGrouping', 'date', 'fullVisitorId', 'visitId',\
       'visitNumber', 'visitStartTime', 'device_browser',\
       'device_deviceCategory', 'device_isMobile', 'device_operatingSystem',\
       'geoNetwork_city', 'geoNetwork_continent', 'geoNetwork_country',\
       'geoNetwork_metro', 'geoNetwork_networkDomain', 'geoNetwork_region',\
       'geoNetwork_subContinent', 'totals_bounces', 'totals_hits',\
       'totals_newVisits', 'totals_pageviews', 'totals_transactionRevenue',\
       'trafficSource_adContent', 'trafficSource_campaign',\
       'trafficSource_isTrueDirect', 'trafficSource_keyword',\
       'trafficSource_medium', 'trafficSource_referralPath',\
       'trafficSource_source']


def load_df(csv_path='../input/train_v2.csv'):
    JSON_COLUMNS = ['device', 'geoNetwork', 'totals', 'trafficSource']
    ans = pd.DataFrame()
    dfs = pd.read_csv(csv_path, sep=',',
                     converters={column: json.loads for column in JSON_COLUMNS}, 
                     dtype={'fullVisitorId': 'str'}, # Important!!
                    chunksize = 100000)
    for df in dfs:
        df.reset_index(drop = True,inplace = True)
        for column in JSON_COLUMNS:
            column_as_df = json_normalize(df[column])
            column_as_df.columns = [f"{column}_{subcolumn}" for subcolumn in column_as_df.columns]
            df = df.drop(column, axis=1).merge(column_as_df, right_index=True, left_index=True)

        print(f"Loaded {os.path.basename(csv_path)}. Shape: {df.shape}")
        use_df = df[features]
        del df
        gc.collect()
        ans = pd.concat([ans, use_df], axis = 0).reset_index(drop = True)
        print(ans.shape)
    return ans

train = load_df()
train.shape
