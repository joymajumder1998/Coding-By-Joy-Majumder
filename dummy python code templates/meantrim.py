from scipy import stats
a=[20,20,45,45,57,68,70,34,38]
a.sort()
cost=stats.trim_mean(a,0.1)
print(cost)