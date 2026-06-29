from  deep_translator import GoogleTranslator 
TEXT  = "привет"
translate =  GoogleTranslator(source='auto' , target= 'en').translate(TEXT)
print(translate)