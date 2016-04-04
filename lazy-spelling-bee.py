word_map = {}
def count_lazy_bee(word, i):	
	if i==len(word)-1:
		print ""
		pass
	else:
		print word[i-1],
		count_lazy_bee(word, i+1)
		print word[i],
		count_lazy_bee(word, i+1)
		print word[i+1],
		count_lazy_bee(word, i+1)

if __name__=="__main__":
	word = "abc"
	count_lazy_bee(word, 0)