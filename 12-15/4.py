import matplotlib.pyplot as plt
plt.title("IDK lol")
labels=["JavaScript","Java","PHP","C","Python"]
Y=[35,30,20,10,5]
explode=[0, 0.05, 0, 0,0] ## 0.1 : 원밖으로 10% 튀어나옴
plt.pie(Y, labels=labels, explode=explode)
plt.show()
