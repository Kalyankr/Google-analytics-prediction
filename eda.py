

train["totals_transactionRevenue"] = train["totals_transactionRevenue"].astype('float')
total_revenue=train.groupby("fullVisitorId")["totals_transactionRevenue"].sum().reset_index()
plt.figure(figsize=(8,6))
plt.scatter(range(total_revenue.shape[0]), np.sort(np.log1p(total_revenue["totals_transactionRevenue"].values)))
plt.xlabel('index', fontsize=12)
plt.ylabel('TransactionRevenue', fontsize=12)
plt.show()


def chats(data):
    trace = go.Bar(y=data.index[::-1],
                   x=data.values[::-1],
                   showlegend=False,
                   orientation = 'h',
    )
    return trace
data=train.groupby("device_browser")["totals_transactionRevenue"].agg(["size","count","mean"])
data.columns=["count", "count of non-zero revenue", "mean"]
data=data.sort_values(by="count",ascending=False)
trace1=chats(data["count"].head(10))
trace2=chats(data["count of non-zero revenue"].head(10))
trace3=chats(data["mean"].head(10))


data=train.groupby("device_deviceCategory")["totals_transactionRevenue"].agg(["size","count","mean"])
data.columns=["count", "count of non-zero revenue", "mean"]
data=data.sort_values(by="count",ascending=False)
trace4=chats(data["count"].head(10))
trace5=chats(data["count of non-zero revenue"].head(10))
trace6=chats(data["mean"].head(10))


data=train.groupby("device_operatingSystem")["totals_transactionRevenue"].agg(["size","count","mean"])
data.columns=["count", "count of non-zero revenue", "mean"]
data=data.sort_values(by="count",ascending=False)
trace7=chats(data["count"].head(10))
trace8=chats(data["count of non-zero revenue"].head(10))
trace9=chats(data["mean"].head(10))


# Creating two subplots
fig = tools.make_subplots(rows=3, cols=3, vertical_spacing=0.04, 
                          subplot_titles=["Device Browser - Count", "Device Browser - Non-zero Revenue Count", "Device Browser - Mean Revenue",
                                          "Device Category - Count",  "Device Category - Non-zero Revenue Count", "Device Category - Mean Revenue", 
                                          "Device OS - Count", "Device OS - Non-zero Revenue Count", "Device OS - Mean Revenue"])

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 1, 3)
fig.append_trace(trace4, 2, 1)
fig.append_trace(trace5, 2, 2)
fig.append_trace(trace6, 2, 3)
fig.append_trace(trace7, 3, 1)
fig.append_trace(trace8, 3, 2)
fig.append_trace(trace9, 3, 3)

fig['layout'].update(height=1200, width=1200, paper_bgcolor='rgb(233,233,233)', title="Device Plots")
py.iplot(fig, filename='device-plots')



#country
network_Country=train.groupby("geoNetwork_country")["totals_transactionRevenue"].agg(["size","count","mean"])
network_Country.columns=["Country_count", "Country_count of non-zero revenue", "mean"]
network_Country=network_Country.sort_values(by="Country_count",ascending=False)
trace1=chats(network_Country["Country_count"].head(10))
trace2=chats(network_Country["Country_count of non-zero revenue"].head(10))
trace3=chats(network_Country["mean"].head(10))



#continent
network_continent=train.groupby("geoNetwork_continent")["totals_transactionRevenue"].agg(["size","count","mean"])
network_continent.columns=["Continent_count", "Continent_count of non-zero revenue", "mean"]
network_continent=network_continent.sort_values(by="Continent_count",ascending=False)
trace4=chats(network_continent["Continent_count"].head(10))
trace5=chats(network_continent["Continent_count of non-zero revenue"].head(10))
trace6=chats(network_continent["mean"].head(10))


network_continent=train.groupby("geoNetwork_networkDomain")["totals_transactionRevenue"].agg(["size","count","mean"])
network_continent.columns=["networkDomain_count", "networkDomain_count of non-zero revenue", "mean"]
network_continent=network_continent.sort_values(by="networkDomain_count",ascending=False)
trace7=chats(network_continent["networkDomain_count"].head(10))
trace8=chats(network_continent["networkDomain_count of non-zero revenue"].head(10))
trace9=chats(network_continent["mean"].head(10))

fig = tools.make_subplots(rows=3, cols=3, vertical_spacing=0.08, horizontal_spacing=0.15, 
                          subplot_titles=["Traffic Source - Count", "Traffic Source - Non-zero Revenue Count", "Traffic Source - Mean Revenue",
                                          "Traffic Source Medium - Count",  "Traffic Source Medium - Non-zero Revenue Count", "Traffic Source Medium - Mean Revenue"
                                          ])

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 1, 3)
fig.append_trace(trace4, 2, 1)
fig.append_trace(trace5, 2, 2)
fig.append_trace(trace6, 2, 3)
fig.append_trace(trace7, 3, 1)
fig.append_trace(trace8, 3, 2)
fig.append_trace(trace9, 3, 3)

fig['layout'].update(height=1000, width=1200, paper_bgcolor='rgb(233,233,233)', title="Traffic Source Plots")
py.iplot(fig, filename='geoNetwork-plots')


#traffic_source
traffic_source=train.groupby("trafficSource_source")["totals_transactionRevenue"].agg(["size","count","mean"])
traffic_source.columns=["traffic_source_count", "traffic_source_count of non-zero revenue", "mean"]
traffic_source=traffic_source.sort_values(by="traffic_source_count",ascending=False)
trace1=chats(traffic_source["traffic_source_count"].head(10))
trace2=chats(traffic_source["traffic_source_count of non-zero revenue"].head(10))
trace3=chats(traffic_source["mean"].head(10))



#medium
traffic_medium=train.groupby("trafficSource_medium")["totals_transactionRevenue"].agg(["size","count","mean"])
traffic_medium.columns=["traffic_medium_count", "traffic_medium_count of non-zero revenue", "mean"]
traffic_medium=traffic_medium.sort_values(by="traffic_medium_count",ascending=False)
trace4=chats(traffic_medium["traffic_medium_count"].head(10))
trace5=chats(traffic_medium["traffic_medium_count of non-zero revenue"].head(10))
trace6=chats(traffic_medium["mean"].head(10))




fig = tools.make_subplots(rows=2, cols=3, vertical_spacing=0.08, horizontal_spacing=0.15, 
                          subplot_titles=["Traffic Source - Count", "Traffic Source - Non-zero Revenue Count", "Traffic Source - Mean Revenue",
                                          "Traffic Source Medium - Count",  "Traffic Source Medium - Non-zero Revenue Count", "Traffic Source Medium - Mean Revenue"
                                          ])

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 1, 3)
fig.append_trace(trace4, 2, 1)
fig.append_trace(trace5, 2, 2)
fig.append_trace(trace6, 2, 3)


fig['layout'].update(height=1000, width=1200, paper_bgcolor='rgb(233,233,233)', title="Traffic Source Plots")
py.iplot(fig, filename='geoNetwork-plots')


import datetime
def scatter_plot(data):
    trace = go.Scatter(
        x=data.index[::-1],
        y=data.values[::-1],
        showlegend=False,
        #mode = 'lines+markers',
    )
    return trace
train['date'] = train['date'].apply(lambda x: datetime.date(int(str(x)[:4]), int(str(x)[4:6]), int(str(x)[6:])))
date_trans=train.groupby("date")["totals_transactionRevenue"].agg(["size","count"])
date_trans.columns = ["count", "count of non-zero revenue"]
date_trans = date_trans.sort_index()

trace1=scatter_plot(date_trans["count"])
trace2=scatter_plot(date_trans["count of non-zero revenue"])
fig = tools.make_subplots(rows=2, cols=1, vertical_spacing=0.08,
                          subplot_titles=["Date - Count", "Date - Non-zero Revenue count"])
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 2, 1)
fig['layout'].update(height=800, width=800, paper_bgcolor='rgb(233,233,233)', title="date-plots for count & Revenue")
py.iplot(fig, filename='date-plots')
