import eel
import desktop
import translate

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def translate_word(word, before_lang, after_lang):
    translate.translate_word(word, before_lang, after_lang)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)