# GASAPIを作成したので使ってみよう！
import requests
import eel

def translate_word(word, before_lang, after_lang):
    text=word
    #print(word)
    source=before_lang
    target=after_lang

    url="https://script.google.com/macros/s/AKfycbxth9zRnQ3VxnxbN2qxD310uN-yBaDuc8JKggH7UGmNouHQIhST/exec?text="+text+"&source="+source+"&target="+target
    r = requests.get(url)
    eel.view_log_js("翻訳前：{}".format(word))
    eel.view_log_js("翻訳後：{}".format(r.text))


# googleが原因でgoogletransは使えなくなっているとのこと。
# from googletrans import Translator
# translator = Translator()
# result = translator.translate('안녕하세요.', dest="ja")
# print(result[0].text)