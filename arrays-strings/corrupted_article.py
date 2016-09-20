article = "todayapersonworearaincoat"

dictionary = {"today", "a", "person", "wore", "rain", "coat"}
def isWord(word):
	if word in dictionary:
		return True
	return False

def fixArticle(article, final):
	index = 0
	print final
	if not article:
		return None

	print ' '.join(final[::-1])
	while not isWord(article[index:]):
		index += 1
	final.append(article[index:])
	fixArticle(article[:index], final)
	
fixArticle(article, [])
