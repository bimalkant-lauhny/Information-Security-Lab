a = []
h = [0]*26
def findinm(x,y):

	i = 0
	j = 0
	x1 = 0
	y1 = 0
	x2 = 0
	y2 = 0
	while i <5:
		j=0

		while j < 5:

			if a[i][j] == x:

				x1 = i
				y1 = j
			if a[i][j] == y:
				x2 = i
				y2 = j
			j +=1
		i +=1

	return x1, y1, x2, y2

inp = raw_input("Enter text to encrypt: " )
key = raw_input("Enter the key to encrypt: ")

 
i = 0
j = 0
k = 0
al = 'a'
# make the matrix
if(key.find('i')==-1):
	skip = 'j'
else:
	skip = 'i'


while i<5:
	d = []
	j = 0
	while j<5:
		if k<len(key):
			if h[ord(key[k])-97] == 0:
				d.append(key[k])
				h[ord(key[k])-97] = 1
				j+=1
			k+=1
		else:
			if h[ord(al)-97] == 0:
				if al != skip:
					d.append(al)
					j+=1
					h[ord(al)-97] = 1
			al = chr(ord(al)+1)
	a.append(d)
	i+=1

if len(inp)%2 ==1:
	inp = inp + 'x'


i = 0
res = ''
while i < len(inp):
	if inp[i] == inp[i+1]:
		inp = inp[0,i]+'x'+inp[i+1:]
	x1,y1,x2,y2 = findinm(inp[i], inp[i+1])

	if x1 == x2:
		res = res + a[x1][(y1+1)%5] + a[x1][(y2+1)%5]
	elif y1 == y2:
		res = res + a[(x1+1)%5][y1] + a[(x2+1)%5][y1]
	else:
		res = res + a[x1][y2] + a[x2][y1]
	i += 2

print "Encrypted text: ", res

i = 0
res2 = ''
while i < len(res):

	x1,y1,x2,y2 = findinm(res[i], res[i+1])

	if x1 == x2:
		res2 = res2 + a[x1][(y1-1)%5] + a[x1][(y2-1)%5]
	elif y1 == y2:
		res2 = res2 + a[(x1-1)%5][y1] + a[(x2-1)%5][y1]
	else:
		res2 = res2 + a[x1][y2] + a[x2][y1]
	i += 2

print "Decrypted Text: ", res2
