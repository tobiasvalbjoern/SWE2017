

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


def decode(mess):
	#in case of no input. Don't do anything
	if not mess : return ''
	
	res = []
	tuple=()
	
	#how many elements are there in the list?
	end=len(mess)
	
	#use the tuple to traverse through the list of tuples in mess, 
	#until the end of the list is reached.
	for tuple in mess[0:end]:
		count = 1
		#the number of times the character occurs 
		#is in the first spot in the tuple. 
		n=tuple[0]
		#the character that needs to be printed n number of times is
		#in the second spot in the tuple
		char=tuple[1]
	
		#append a character until you have printed n characters.
		while count <= n: 
			#append the characters to our list.
			res.append(f'{char}')
			count+=1	
			
	#return a string that is equal to the list 
	#with no seperation between the elements.  	
	return ''.join(res)