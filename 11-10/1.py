em = "email"
s = {'name':"WaiYanNaung",'id':20251310,em:'w@wyn.onl'}
s2 = {'name':'Hsu Wai','id':20291310,em:'gf@waiyannaung.com'}

print(s['name'])
print(s['email'])
print(s.keys())
print(s.get("id"))

print(s2.keys())

for i in s2:
    print(s2.get(i))
