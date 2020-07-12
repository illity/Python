import PyPDF2, re
file = open('C:/Users/-/Downloads/lusiadas.pdf','rb')
print(PyPDF2.PdfFileReader(file).numPages)
#print(text)
full=''
for page in range(1,PyPDF2.PdfFileReader(file).numPages):
 text = PyPDF2.PdfFileReader(file).getPage(page).extractText()
 text=re.sub('www\.nead\.unama\.br', '',text)
 formated=re.findall('[a-zà-ù][A-ZÀ-Ù]|,[a-zA-Zà-ùÀ-Ù]|;[A-ZÀ-Ù]|\:[A-ZÀ-Ù]|\.[A-ZÀ-Ù]|[A-ZÀ-Ù][A-ZÀ-Ù]|[a-zà-ù]\(|\)[A-ZÀ-Ù]|[0-9][A-ZÀ-Ù]|;.|:.|\.-|\u00ab[A-ZÀ-Ù]|\u00bb[A-ZÀ-Ù]|\?[A-ZÀ-Ù]|![a-zA-Zà-ùÀ-ù]| -|,\(|\.\(',text)
 #print(formated)
 #print(text)
 for i in formated:
  #print(i)
  #print('\\'+i if (i[0]=='.' or i[0]==')') else i[0]+'\\'+i[1] if i[1]=='(' else i)
  text=re.sub('\\'+i[0]+'\\'+i[1] if (i[0]=='.' and i[1]=='(') else'\\'+i if (i[0]=='.' or i[0]==')' or i[0]=='?') else i[0]+'\\'+i[1] if i[1]=='(' else i,i[0]+'\n'+i[1],text)
 #print(text)
 full=full+text
full_lines=full.split('\n')
for line in full_lines:
 if len(line)>50:
  print(line)
  r=input('replace:')
  open('new.txt','a').write(line.replace(r.replace(' ',''),r.replace(' ','\n'))+'\n')
 else: open('new.txt','a').write(line+'\n')