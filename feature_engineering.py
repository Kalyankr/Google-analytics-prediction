

num_cols = ["totals_hits", "totals_pageviews", "visitNumber", "visitStartTime", 'totals_bounces',  'totals_newVisits']    
for col in num_cols:
    train[col] = train[col].astype(float)
    test[col] = test[col].astype(float)
excluded_features = [
    'date', 'fullVisitorId', 'sessionId', 'totals.transactionRevenue', 
    'visitId', 'visitStartTime', 'nb_sessions', 'max_visits','visit_time','totals_visits'
]

categorical_features = [
    _f for _f in train.columns
    if (_f not in excluded_features) & (train[_f].dtype == 'object')
]

train_val=np.log1p(train_y)

for f in categorical_features:
    train[f], indexer = pd.factorize(train[f])
    test[f] = indexer.get_indexer(test[f])

train["totals_transactionRevenue"].fillna(0, inplace=True)
train_y = train["totals_transactionRevenue"]
train_val=np.log1p(train_y)


# splitting the dataset into  train and test sets for validation.

train_x,test_x,val_x,val_y=train_test_split(train,train_val,test_size=0.2, random_state=42)
trn_x=train_x[categorical_features+num_cols]
tst_x=test_x[categorical_features+num_cols]
test_X=test[categorical_features+num_cols]
