def password2(mypw):
 newsymbol = {'i':'!','a':'@','m':'M','B':'8','o':'.'}
 password1 = ""
 for symb in mypw:
   if symb in newsymbol:
     password1 = password1 + newsymbol[symb]
   else:
     password1 = password1 + symb
 password1 = password1 + "q*s"
 return password1
ezpw = input()
complete_password = password2(ezpw)
print(complete_password)
