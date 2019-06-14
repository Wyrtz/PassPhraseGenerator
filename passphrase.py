import linecache
import random

wordsNeededCandidate = input("Hvor lang skal din passphrase være ?\n")
try:
	wordsNeeded = int(wordsNeededCandidate)
except ValueError:
	print("Tal ikke forstået")
	wordsNeeded = 3

def generatePassphrase(numb_of_words:int, name_of_file: str):
	dict_len = file_len(name_of_file)
	password = ""
	for i in range(numb_of_words):
		line_num = random.randint(1,dict_len)
		password += linecache.getline(name_of_file, line_num)
	password = password.replace("\n", "-")
	password = password[0:-1]	
	return password

def file_len(filename:str):
	with open(filename, "r", encoding='utf-8') as file:
		for i, l in enumerate(file):
			pass
	return i + 1

print(f"\nHer har du 5 bud med længde {wordsNeeded}: \n", )
for i in range(5):
	print(generatePassphrase(wordsNeeded, "danish-short-cleaned.txt"))
print("\n")

print(f"\nHer har du 5 bud med længde {wordsNeeded} fra den udvidede ordbog: \n", )
for i in range(5):
	print(generatePassphrase(wordsNeeded, "danish-long-cleaned.txt"))
print("\n")