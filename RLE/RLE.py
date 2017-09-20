import sys

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
	return ''.join([n*c for n,c in mess])
	
	#my first approach is down below. The above is condensed.
	# #in case of no input. Don't do anything
	# if not mess : return ''
	
	# res = []
	
	# #how many elements are there in the list?
	# end=len(mess)
	
	# #use the tuple to traverse through the list of tuples in mess, 
	# #until the end of the list is reached.
	# for t in mess:
		
		# #the number of times the character occurs 
		# #is in the first spot in the tuple. 
		# n=t[0]
		
		# #the character that needs to be printed n number of times is
		# #in the second spot in the tuple
		# char=t[1]
		
		# #write the desired number of chars
		# res.append(n*char)	
			
	# #return a string that is equal to the list 
	# #with no seperation between the elements.  	
	# return ''.join(res)

# def main(argv):
	# if  len(sys.argv)==3:
		# if sys.argv[1]=='-e':
			# with open(sys.argv[2],'r') as f:
				# mess=f.read()
				# print(encode(mess))
		# elif sys.argv[1]=='-d':
			# with open(sys.argv[2],'r') as f:
				# mess=f.read()
				# print(decode(mess))
	# else:
		# print ("RLE.py <coding> <file>")
		# sys.exit(2)
	
	
# if __name__ == "__main__":
   # main(sys.argv[1:])	
