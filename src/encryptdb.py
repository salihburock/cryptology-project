from cli import *

db = [{"telno": "0531 415 9265",
       "kullaniciadi": u"yiğitgümüş",
       "şifre": u"yiğitinşifresi",
       "eposta": "yigitgumus@gmail.com"},
      {"telno": "0545 234 1044",
       "kullaniciadi": u"ayazgümüş",
       "şifre": u"ayazinşifresi",
       "eposta": "ayazgumus@gmail.com"}]

vk = {
    0: "tels",
    1: "pws",
    2: "ems"
}

def cdm(imail):
    cd()

for i in db:
    l = list(i.values())
    l2 = list(i.keys())
    ln = l[1]
    print(l)
    for j in l[:-1]:
        print(j)
        fname = f'db/{vk[l.index(j)]}/{l[3]}'
        cd(fname+'.mp4', fname+'.key')
print(db)
