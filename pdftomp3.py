from pdfminer.high_level import extract_text
from gtts import gTTS
text = (((extract_text('Exemple.pdf').replace("\n",". ")).replace(">",". ")).replace("<",". ")).strip()

mp3 = gTTS(text=text, lang="ru")
mp3.save("BarstarsMP3_Exemple.mp3")

print(text)
