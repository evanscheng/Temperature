#comment
name = input('please input name:')
print('Hi', name)


#casting transfer 輸入的東西皆視為str/str與int不可比較
age = input('input your age:')
age = int(age)
if age >= 20 :
	print('you can vote!')

#攝氏轉華氏溫度,讓使用者輸入攝氏,印出華氏
#公式 華氏=攝氏＊9/5+32

ce = input('input cel:')
ce = int(ce)
fa = ce * 9 / 5 + 32
print('Fa:', fa)
