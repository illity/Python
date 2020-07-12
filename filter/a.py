import PyPDF2, re
file = open('C:/Users/-/Downloads/lusiadas.pdf','rb')
print(PyPDF2.PdfFileReader(file).numPages)
#print(text)
full=''
for page in range(1,PyPDF2.PdfFileReader(file).numPages-194):
 text = PyPDF2.PdfFileReader(file).getPage(page).extractText()
 text=re.sub('www\.nead\.unama\.br', '',text)
 print('oi')
 formated=re.findall('[a-z][A-Z]|,[A-Z]|;[A-Z]|\:[A-Z]|\.[A-Z]|[A-Z][A-Z]|[a-z]\(|\)[A-Z]|[0-9][A-Z]|;.|:.|\.-|\u00ab[A-Z]',text)
 #print(formated)
 #print(text)
 for i in formated:
  #print(i)
  #print('\\'+i if (i[0]=='.' or i[0]==')') else i[0]+'\\'+i[1] if i[1]=='(' else i)
  text=re.sub('\\'+i if (i[0]=='.' or i[0]==')') else i[0]+'\\'+i[1] if i[1]=='(' else i,i[0]+'\n'+i[1],text)
 #print(text)
 full=full+text
full_lines=full.split('\n')
for line in full_lines:
 if len(line)>50: print(line)