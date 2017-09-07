

def encode(mess):
    if not mess : return ''

    old = mess[0]
    i = 1
    res = []

    for c in mess[1:]:
        if c != old:
            res.append((i,old))
            i = 1
            old = c
        else:
            i += 1
    res.append((i,old))

    return res

#5k4b	
def decode(mess):
	if not mess : return ''
	
	res = []
	tuple=()
	#how many elements are there in the list?
	end=len(mess)
	
	
	for tuple in mess[0:end]:
		count = 1
		n=tuple[0]
		char=tuple[1]
	
		while count <= n: 
			res.append(f'{char}')
			count+=1	
			
		
	return ''.join(res)