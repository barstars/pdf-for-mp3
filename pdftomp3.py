from pdfminer.high_level import extract_text
from gtts import gTTS
#text = (((extract_text("C:/Users/MUCHASCH/Downloads/IdentityCard-041228551255-20231207130502 (1).pdf").replace("\n",". ")).replace(">",". ")).replace("<",". ")).strip()

text = (extract_text("Exemple.pdf").replace("\n",". ")).strip()

mp3 = gTTS(text=text, lang="en")
mp3.save("BarstarsMP3_Exemple.mp3")

print(text)
