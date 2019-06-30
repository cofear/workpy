
def llist(s):
	return [i.split() for i in s.split('\n') if len(i) > 0]

def hump(s):
	a = [i for i in uline(s).split('_') if len(i) > 0]
	return a[0].lower()+''.join(i.capitalize() for i in a[1:])

def uline(s):
	b = ''
	a = str(s)
	for i, v in enumerate(a):
		b += '_'+v if v.isupper() and a[i-1].islower() else v
	return '_'.join([i.lower() for i in b.split('_') if len(i) > 0])
