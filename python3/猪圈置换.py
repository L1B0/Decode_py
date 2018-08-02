dic = {'a':'j','b':'k','c':'l','d':'m','e':'n','f':'o','g':'p','h':'q','i':'r','j':'a','k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'w','t':'x','u':'y','v':'z','w':'s','x':'t','y':'u','z':'v'}
s=raw_input("input:")
null=''
for i in range(0,len(s)):
    if (s[i]<='Z' and s[i]>='A') or (s[i]<='z' and s[i]>='a'):
        null+=dic[s[i]]
    else:
        null+=s[i]
print null