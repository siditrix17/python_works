import re
def findcreditcard(raw):
	americaRE=re.findall("3[47][0-9]{13}",raw)
	if americaRE:
		print'[+] found american card:',americaRE[0]
	else:
		print'[+] found nothin!!'
def main():
	tests=[]
	tests.append('i would like yo have 38723612631 apples')
	tests.append('bill my card: 37828224631000 for rs 2400')
	for test in tests:
		findcreditcard(test)
if __name__=="__main__":
 main()


