
import itertools

def get_tuple(line, i, par=False):
	if par:
		length = 0
		tup = []
		for c in line[i:]:
			tup.append(c)
			length += 1
			if c == ")":
				break
		return (("".join(tup),), length)
	else:
		return (tuple(line[i]), 1)

def extract_tup(line):
	ret = []
	i = 0
	while i!=len(line):
		res = get_tuple(line, i, line[i]=="(")
		tup = res[0]
		i += res[1]
		ret.append(tup)
	return ret

def listerize(ls_tup):
	return [tuple(c for c in tup[0][1:-1]) if len(tup[0])!=1 else tuple(c for c in tup[0][0]) for tup in ls_tup]

def product(ls_tup):	
	return ["".join(list(p)) for p in itertools.product(*ls_tup)]

def get_valid(ls_prod, ls_valid):
	return [prod for prod in ls_prod if prod in ls_valid]

if __name__=="__main__":
	from sys import stdin
	from readfile import readfile

	# in_str = readfile("input.txt")

	info = stdin.readline().rstrip("\n").split(" ")
	L = int(info[0])
	D = int(info[1])
	N = int(info[2])
	valid_words = []
	for i in range(D):
		valid_words.append(stdin.readline().rstrip("\n"))
	ls_word = []
	for i in range(N):
		ls_word.append(stdin.readline().rstrip("\n"))
	ls_ans = []
	for word in ls_word:
		ans = extract_tup(word)
		ans = product(listerize(ans))
		ans = get_valid(ans, valid_words)
		ans = len(ans)
		ls_ans.append(ans)
	i = 1
	for ans in ls_ans:		
		print "Case #%d: %d"%(i, ans)
		i += 1