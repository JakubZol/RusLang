# hello function in RusLang

def привет(имя):
	текст = "привет " + имя
	return текст
	
# iterative fibonacci in RusLang

def фиб(н):
	if н == 1:
		return 0
	elif н == 2:
		return 1
	else:
		тмп_1 = 0
		тмп_2 = 1
		for к in range (2, н):
			РЕЗ = тмп_1 + тмп_2
			тмп_1 = тмп_2
			тмп_2 = РЕЗ
			
		return РЕЗ
		
	
print(привет("Сергей"))
for к in range (1, 10):
	if к < 4 or к >= 7:
		print("фиб ")
		print(фиб(к))
	elif к == 9:
		break
	else:
		print("к ")
		print(к)
		continue
		
	
