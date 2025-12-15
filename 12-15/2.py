import matplotlib.pyplot as plt ##Python plotting(그래프를 그리다)
x=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
y1=[15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
y2=[20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]
plt.plot(x, y1, x, y2)
plt.xlabel("day")
plt.ylabel("temparature")
plt.show()
