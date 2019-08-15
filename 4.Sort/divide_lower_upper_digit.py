'''
	将小写字母放在前面，大写字母放在中间，数字放在最后，不要求序列有序，只要求稳定

	Author by: Lofues
'''

def divide(s : str):
	if not s: return
	s,index_lower = divide_lower_and_unlower(s)
	s = divide_digit_and_notDigit(s,index_lower)
	return s

def divide_lower_and_unlower(s : str):
	l = list(s)
	i, j = 0,0
	for j in range(len(l)):
		if 'a' <= l[j] <= 'z':
			l[i], l[j] = l[j], l[i]
			i += 1
	s = ''.join(l)
	return s,i

def divide_digit_and_notDigit(s : str, index_lower : int):
	i, j = index_lower, index_lower
	l = list(s)
	for j in range(index_lower,len(l)):
		if 'A' <= l[j] <= 'Z':
			l[i],l[j] = l[j],l[i]
			i += 1
	s = ''.join(l)
	return s


s = 'aSD23bcAfeFD3'
s = divide(s)
print(s)