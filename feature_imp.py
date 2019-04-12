# feature importance plot.

fig, ax = plt.subplots(figsize=(18,20))
lgb.plot_importance(model, max_num_features=50, height=0.8, ax=ax)
ax.grid(False)
plt.title("Feature Importance", fontsize=15)
plt.show()
