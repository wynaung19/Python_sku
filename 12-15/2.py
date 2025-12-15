import matplotlib.pyplot as plt ##Python plotting(그래프를 그리다)
x=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
y1=[15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 14.4]
y2=[26.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]
y3=[34,35,37,34,33,33,32]
plt.title("Temperature of Cities")
plt.plot(x, y1, label="Seoul" )
plt.plot(x, y2, label="Busan" )
plt.plot(x,y3,label="Yangon")
plt.xlabel("day")
plt.ylabel("temparature")
plt.legend(loc="best")
plt.show()
