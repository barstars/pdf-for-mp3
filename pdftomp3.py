from pdfminer.high_level import extract_text
#text = (((extract_text("C:/Users/MUCHASCH/Downloads/IdentityCard-041228551255-20231207130502 (1).pdf").replace("\n",". ")).replace(">",". ")).replace("<",". ")).strip()

text = (extract_text("C:/Users/MUCHASCH/Downloads/IdentityCard-041228551255-20231207130502 (1).pdf").replace("\n",". ")).strip()


print(text)