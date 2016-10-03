# month.py
months="JanFebMarAprMayJunJulAugSepOctNovDec"#写出所有月份的字母
n = input("请输入月份数（1-12）：")#输入月份
pos=(int(n)-1) * 3#定义一个pos的变量，意思为输入的月份－1 * 3为所输入月份的首字母的位置
monthAbbrev=months[pos:pos+3]#定义函数monthAbbrev，索引pos的值后面的三位
print("月份简写是"+monthAbbrev+".")#输出