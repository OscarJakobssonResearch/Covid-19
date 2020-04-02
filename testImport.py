import pdfplumber
import string
pdf = pdfplumber.open('Norway/2020.03.16.pdf')
#pdf = pdfplumber.open('Greece/gov-greece-22-03-2020.pdf')
page = pdf.pages[0]
#page = pdf.pages[4]
text = page.extract_text()
#print(text)

#print(len(text))
pdf.close()

def OpenPdf(FilePath,PageNumber):
	pdf = pdfplumber.open(FilePath)
	page = pdf.pages[PageNumber]
	text = page.extract_text()
	#print(text)

	pdf.close()
	return(text)

def findNumberInPdf2(text,StartPhrase,EndPhrase,NumberLength):

	result1 = text.find(EndPhrase)
	StepsBackForNumber=NumberLength
	#print(result1)
	SampleText=text[result1-StepsBackForNumber-len(StartPhrase):len(text)]
	print(SampleText)
	StartPhrase=StartPhrase
	result2 = SampleText.find(StartPhrase)
	#print(result2)
	if(result2==-1):
		# add alternative phrases here 
		#print(StartPhrase.lower())
		result2 = SampleText.find(StartPhrase.lower())
	#print(text[result1-StepsBackForNumber-len(StartPhrase)+result2:result1])
	StringForData=text[result1-StepsBackForNumber-len(StartPhrase)+result2+len(StartPhrase):result1]
	#print(StringForData)
	StringForData=StringForData.replace(" ", "")
	#print(int(StringForData))
	return(int(StringForData))


def findNumberInPdf(text,StartPhraseList,EndPhraseList,NumberLength):
	EndPhrase=EndPhraseList[0]
	StartPhrase=StartPhraseList[0]
	for attempt_no in range(len(EndPhraseList)):
		try:			
			result1 = text.find(EndPhrase)
			StepsBackForNumber=NumberLength
			SampleText=text[result1-StepsBackForNumber-len(StartPhrase):len(text)]
			#print(SampleText)
			StartPhrase=StartPhrase
			result2 = SampleText.find(StartPhrase)
			#print(result2)
			StringForData=text[result1-StepsBackForNumber-len(StartPhrase)+result2+len(StartPhrase):result1]
			#print(len(StringForData))
			StringForData=StringForData.replace(" ", "")
			#print(int(StringForData))
			int(StringForData)
			return(int(StringForData))
		except ValueError as error:
			EndPhrase=EndPhraseList[attempt_no+1]
			StartPhrase=StartPhraseList[attempt_no+1]
			#print(EndPhrase)
			if attempt_no < (len(EndPhraseList)-1):
				pass
				#print("Error: Invalid number")
			else:
				raise error


def findNumberInPdfPortugal(text,StartPhraseList,EndPhraseList,NumberLength):
	EndPhrase=EndPhraseList[0]
	StartPhrase=StartPhraseList[0]
	for attempt_no in range(len(EndPhraseList)):
		try:			
			result1 = text.find(EndPhrase)
			StepsBackForNumber=NumberLength
			SampleText=text[result1-StepsBackForNumber-len(StartPhrase):len(text)]
			#print(SampleText)
			StartPhrase=StartPhrase
			result2 = SampleText.find(StartPhrase)
			#print(result2)
			StringForData=text[result1-StepsBackForNumber-len(StartPhrase)+result2+len(StartPhrase):result1]
			#print(len(StringForData))
			# Data gives two numbers, tested and total number tested side by side, we choose the second one
			if(attempt_no==0):
				StringForDataSplit=StringForData.split()
				StringForDataSplitDone=StringForDataSplit[1].replace(" ", "")
			else:
				StringForDataSplitDone=StringForData.replace(" ", "")	
			#print(int(StringForData))
			int(StringForDataSplitDone)
			return(int(StringForDataSplitDone))
		except ValueError as error:
			EndPhrase=EndPhraseList[attempt_no+1]
			StartPhrase=StartPhraseList[attempt_no+1]
			#print(EndPhrase)
			if attempt_no < (len(EndPhraseList)-1):
				pass
				#print("Error: Invalid number")
			else:
				raise error

'''
for i in range(16,32):
	#print(i)
	print(findNumberInPdf(OpenPdf('Norway/2020.03.%d.pdf'%i,0),['Totalt','totalt','Totalt'],['er rapportert testet','er rapportert testet','personer er rapportert testet'],100))
	#print(findNumberInPdf2(OpenPdf('Norway/2020.03.%d.pdf'%i,0),'Totalt','er rapportert testet',100))

print('Confirmed')
for i in range(16,32):
	#print(i)
	print(findNumberInPdf(OpenPdf('Norway/2020.03.%d.pdf'%i,0),['totalt','Totalt er det varslet','Det er totalt meldt'],['tilfeller, hvorav','personer med påvis','tilfeller til MSIS'],100))
	#print(findNumberInPdf2(OpenPdf('Norway/2020.03.%d.pdf'%i,0),'Totalt','er rapportert testet',100))
'''

'''
for i in range(20,26):
	#print(i)
	print(findNumberInPdf(OpenPdf('Greece/covid-gr-daily-report-202003%d.pdf'%i,4),['έχουνσυνολικάελεγχθεί'],['κλινικάδείγματα,εκτωνοποί'],100))
'''



#OpenPdf('Portugal/gov-portugal-21-03-2020.pdf',0)

#print(findNumberInPdfPortugal(OpenPdf('Portugal/gov-portugal-%d-03-2020.pdf'%25,0),['Total de casos','Total de casos'],['confirmados suspeito','suspeitos'],20))

for i in range(16,30):
	print(findNumberInPdfPortugal(OpenPdf('Portugal/gov-portugal-%d-03-2020.pdf'%i,0),['Total de casos','Total de casos'],['confirmados suspeito','suspeitos'],20))





'''
result1 = text.find('er rapportert teste')
print("Substring 'er rapportert teste':", result1)
print(text[result1:len(text)])
StepsBackForNumber=20
SampleText=text[result1-StepsBackForNumber:len(text)]
print(SampleText)
StartPhrase='Totalt'
result2 = SampleText.find(StartPhrase)
print(text[result1-StepsBackForNumber+result2:result1])
StringForData=text[result1-StepsBackForNumber+result2+len(StartPhrase):result1]
print(StringForData)
StringForData=StringForData.replace(" ", "")
print(int(StringForData))


StartPhrase='Totalt'
EndPhrase='er rapportert teste'

result1 = text.find(EndPhrase)
#print("Substring 'er rapportert teste':", result1)
#print(text[result1:len(text)])
StepsBackForNumber=10
SampleText=text[result1-StepsBackForNumber:len(text)]
print(SampleText)
SampleText=text[result1-StepsBackForNumber-len(StartPhrase):len(text)]
print(SampleText)
StartPhrase=StartPhrase
result2 = SampleText.find(StartPhrase)
print(text[result1-StepsBackForNumber-len(StartPhrase)+result2:result1])
StringForData=text[result1-StepsBackForNumber-len(StartPhrase)+result2+len(StartPhrase):result1]
print(StringForData)
StringForData=StringForData.replace(" ", "")
print(int(StringForData))
'''

#result = text.find('Totalt')
#print("Substring 'Totalt':", result)
#print(text[result:len(text)])

#quote = 'Let it be, let it be, let it be'

#result = text.find('er rapportert testet')
#print("Substring 'er rapportert testet':", result)
#print(text[result:len(text)])
#result = quote.find('small')
#print("Substring 'small ':", result)

# How to use find()
#if  (quote.find('be,') != -1):
#  print("Contains substring 'be,'")
#else:
#  print("Doesn't contain substring")


#import urllib2

'''
def main():
    download_file("http://mensenhandel.nl/files/pdftest2.pdf")

def download_file(download_url):
    response = urllib2.urlopen(download_url)
    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == "__main__":
    main()
'''    



'''
	Error=True
	while Error is True:
		try:
			EndPhrase=EndPhraseList[0]
			result1 = text.find(EndPhrase)
			StepsBackForNumber=NumberLength
			#print(result1)
			SampleText=text[result1-StepsBackForNumber-len(StartPhrase):len(text)]
			#print(SampleText)
			StartPhrase=StartPhrase
			result2 = SampleText.find(StartPhrase)
			#print(result2)
			if(result2==-1):
				# add alternative phrases here 
				#print(StartPhrase.lower())
				result2 = SampleText.find(StartPhrase.lower())
			#print(text[result1-StepsBackForNumber-len(StartPhrase)+result2:result1])
			StringForData=text[result1-StepsBackForNumber-len(StartPhrase)+result2+len(StartPhrase):result1]
			#print(StringForData)
			StringForData=StringForData.replace(" ", "")
			#print(int(StringForData))
			int(StringForData)
			Error=False
		except ValueError:
			print('Error')
			EndPhrase=EndPhraseList[1]
			break
	return(int(StringForData))
	'''