#โจทย์คิดเกรด นักเรียน 



friend = {'somchai':75,'somsak':70,'sompong':68,'somkiat':89,'somsri':92,
          'saisunee':53,'samorn':58,'smerf':45}


def CheckGrade(friend):
    for f in friend.items():
        if f[1] >= 90:
            print(f[0],'A+')
        elif f[1] >= 80:
            print(f[0],'A')
        elif f[1] >= 75:
            print(f[0],'B+')
        elif f[1] >= 70:
            print(f[0],'B')
        elif f[1] >= 65:
            print(f[0],'C+')
        elif f[1] >= 60:
            print(f[0],'C')
        elif f[1] >= 55:
            print(f[0],'D+')
        elif f[1] >= 50:
            print(f[0],'D')
        else:
            print(f[0],'F')



CheckGrade(friend)


