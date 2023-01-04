from gtts import gTTS
import os
#text reader for arabic language

MyText = "كل يوم ق لاللهم أِنَّ كُلًَ عَمَلٍ أَعمَلهُ من الواجب والمَندوب* وكُلَّ تَركٍ أَترُكُهُ من الحرام والمكروه كُلهُ قُربَةً لِوَجهِكَ الكَريم»"
Language = "ar"

output = gTTS(text=MyText, lang=Language, slow=False)

output.save("texttospeec.mp3")
os.system("start texttospeec.mp3")
