table = '''ZWAXJGDLUBVIQHKYPNTCRMOSFE
KPBELNACZDTRXMJQOYHGVSFUWI
BDMAIZVRNSJUWFHTEQGYXPLOCK
RPLNDVHGFCUKTEBSXQYIZMJWAO
IHFRLABEUOTSGJVDKCPMNZQWXY
AMKGHIWPNYCJBFZDRUSLOQXVET
GWTHSPYBXIZULVKMRAFDCEONJQ
NOZUTWDCVRJLXKISEFAPMYGHBQ
QWATDSRFHENYVUBMCOIKZGJXPL
WABMCXPLTDSRJQZGOIKFHENYVU
XPLTDAOIKFZGHENYSRUBMCQWVJ
TDSWAYXPLVUBOIKZGJRFHENMCQ
BMCSRFHLTDENQWAOXPYVUIKZGJ
XPHKZGJTDSENYVUBMLAOIRFCQW'''
key = (2, 5, 1, 3, 6, 4, 9, 7, 8, 14, 10, 13, 11, 12)
cipher = 'HCBTSXWCRQGLES'
table = table.split()
table = [table[key[x] - 1] for x in range(14)]
key = [table[x].index(cipher[x]) for x in range(len(cipher))]
for i in range(len(table)):
    table[i] = table[i][key[i]:] + table[i][:key[i]]
    print table[i]
for i in range(26):
    s = ''
    for j in range(len(table)):
             s += table[j][i]
    print s
flag = 'FLAG{XSXSBUGKUADMIN}'
print flag
