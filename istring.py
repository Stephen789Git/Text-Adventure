from string import punctuation,letters
import wordLib

class setString:
    text = []
    punct = []

    def __init__(self, string):
        print string
        self.text = string.upper().split()
        self.punct = []
        for word in self.text:
            if word.isalnum() == False:
                i = self.text.index(word)
                self.text.pop(i)
                self.text.insert(i,word.translate(None,punctuation))
                self.punct.append(word.translate(None,self.text[i]))
            else:
                self.punct.append("")
        print self.text
        print self.punct
        if "," in self.punct:
            i = self.punct.index(",")
            f = sListStrings(self.punct[i+1:],",")
            
            if f != -1:
                print self.text[i+1:i+f+2]
            else:
                print self.text[i+1:]

    def get_action(self):
        dl = []
        for word in self.text:
            if thesaurize(word) != '':
               dl.append(thesaurize(word))
        return dl
        
                
def sListStrings(l,s):
    for strings in l:
        i = -1
        if s in strings:
            i = strings.index(s)
        if i != -1:
            return i
    return -1

def thesaurize(word):
    if wordLib.thesaurus.has_key(word):
                return wordLib.thesaurus[word]
    return ''

def pigString(s):
	out = s.split()
	put = ""
	for thing in out:
		put += thing[1:] + thing[0] + "ay "
	return put

def cheechong(s):
	out = s.split()
	put = ""
	fil = letters.translate(None,"AaEeIiOoUu")
	for thing in out:
		for letter in thing:
			if (letter in fil):
				put += letter+"ong"
			else:
				put += letter
		put += " "
		
	return put

def inflation(s):
	out = s.lower().split()
	put = ""
	for thing in out:
		if ('one' in thing):
                    thing.replace('one','two')
		elif ('once' in thing):
                    thing.replace('once','twice')
                elif ('two' in thing):
                    thing.replace('two','three')
                elif ('twice' in thing):
                    thing.replace('twice','thrice')
                elif ('to' in thing):
                    thing.replace('to','three')
                elif ('three' in thing):
                    thing.replace('three','four')
                elif ('thrice' in thing):
                    thing.replace('thrice','four times')
                elif ('four' in thing):
                    thing.replace('four','five')
                elif ('for' in thing):
                    thing.replace('for','five')
                elif ('five' in thing):
                    thing.replace('five','six')
                elif ('six' in thing):
                    thing.replace('six','seven')
                elif ('seven' in thing):
                    thing.replace('seven','eight')
                elif ('eight' in thing):
                    thing.replace('eight','nine')
                elif ('ate' in thing):
                    thing.replace('ate','nine')
                elif ('nine' in thing):
                    thing.replace('nine','ten')
                elif ('ten' in thing):
                    thing.replace('ten','eleven')
                elif ('eleven' in thing):
                    thing.replace('eleven','twelve')
                elif ('twelve' in thing):
                    thing.replace('twelve','thirteen')
                put += thing+' '
        return put
