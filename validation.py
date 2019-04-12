

# Training the model #
pred_test, model, pred_val = run_lgb(trn_x, val_x,tst_x, val_y, test_X)

from sklearn import metrics
pred_val[pred_val<0] = 0
val_pred_df = pd.DataFrame({"fullVisitorId":test_x["fullVisitorId"].values})
val_pred_df["transactionRevenue"] = test_x["totals_transactionRevenue"].values
val_pred_df["PredictedRevenue"] = np.expm1(pred_val)

#print(np.sqrt(metrics.mean_squared_error(np.log1p(val_pred_df["transactionRevenue"].values), np.log1p(val_pred_df["PredictedRevenue"].values))))

val_pred_df = val_pred_df.groupby("fullVisitorId")["transactionRevenue", "PredictedRevenue"].sum().reset_index()

print(np.sqrt(metrics.mean_squared_error(np.log1p(val_pred_df["transactionRevenue"].values), np.log1p(val_pred_df["PredictedRevenue"].values))))
