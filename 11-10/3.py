import operator

trainDic,trainList = {},[]

trainDic = {'thomas':"토마스","Edward":"에드워드"}

trainList =sorted(trainDic.items(),key = operator.itemgetter(0))

print(trainList)
