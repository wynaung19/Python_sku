import matplotlib.pyplot as plt
#plt.hist([1,2,2,3,3,3,4,4,5], bins=5) ##bins : 막대 개수 또는 구간
data = [1,2,2,3,3,3,4,4,5]
plt.hist(data, bins=5, width=0.5) # width: 막대 너비 (0~1)
plt.show()
