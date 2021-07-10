#       -------ALICAN UZUNDEMIR SESLİ ASİSTAN------
#       -------Gerekli dosysları import ediyoruz-------
#       -------Internet bağlantısını sürekli kontrol edin ve py uzantılı dosyayı bir klasör icinde calısıtırın
#       -------Mp3 uzantılı dosya bir bulunduğu dizindeki klasörde olmalı

import speech_recognition as sr #çevrimiçi ve çevrim dışı bir şekilde çalışan konuşma tanıma kütüphanesi
from datetime import datetime #anlık zamanı öğrenmek için
import webbrowser # web browser açmak için
import time #bilgisayrı uyutmak için
from gtts import gTTS #text i ses e çevirmek için
from playsound import playsound#ses dosyasını çalmak için
import random#random bir sayı üretmek için
from random import choice#random bir değer seçmek için
import os#sistem ayarları değiştirmk için
from lxml import html#html dosyasını okumak için
import requests #istek göndermek için
import json # json dosyalarını okumak için
import feedparser #hava  durumunu çekmek için
import colorama #terminal ekranını özelleştirmek için
from colorama import Fore, Back, Style #Gerekli dosya ve sabitleri projemize dahil ettiğimize göre kullanım için gerekli init() fonksiyonunun çağırılması için.

r=sr.Recognizer()#speech recognition ile alınan sesi r adlı değikene atıyoruz
colorama.init()


def record(ask = False):#record adlı bir fonksiyon oluşturuyoruz ve varsayılan olarak ask =false olarak ayarlıyouz
    with sr.Microphone() as source: #mikrofandan gelen veriyi işlem yapabilmek için source e tanımlıyoruz
        if ask:
            speak(ask)
            print(Fore.BLUE)
            print(ask)

        audio = r.listen(source) # dinlenilen source u audio ya atıyoruz
        voice = ''
        try:#
            voice = r.recognize_google(audio,language='tr-TR')#Türkçe dinleme yapıp bunu voice e atıyoruz
        except sr.UnknownValueError:#gelen sesi tanımlayamazsa burası çalışıyor
            
            print(Fore.GREEN)
            print("Sesli Asistan , ne dedin, anlamadım , acaba tekrar edermisin")
            speak("ne dedin, anlamadım , acaba tekrar edermisin")


        except sr.RequestError:# eğerki sistemle alakalı bir hata alırsak burası çalışıyoruz
            speak('Sistemin çalışmıyor')
            print(Fore.GREEN)
            print('Sesli Asistan , Sistemin çalışmıyor')


        return voice #dinlediğimiz voice ı geri döndürüyoruz

def response(voice):#voice ile gelen veriyi sorgululamak için response adında bir fonkiyon
    if 'nasılsın' in voice:# eğer voice nin içinde nasılsın  diye bir değer varsa bunları yap
        #sözler adlı bir dizi tanımlıyoruz
        sozler = ["iyilik benden ya sen",
                "iyi ben peki ya sen",
                "iyi olduğumu duyunca sevineceğini biliyorum",
                "ben bir yapay zekadan ibaretim duygularım yok ama tüm yazılımım düzgün çalışıyor",
                
        ]
        secim=choice(sozler)#sozlerden birini karışık olarak seçilecek

        speak(secim)#seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("Sesli Asistan , "+secim)#seçilen söz yazdırılacak

    if 'Neler yapabilirsin' in voice:# eğer voice nin içinde neler yapabilirsin diye bir değer varsa bunları yap
        
        
        sozler =['seninle sohbet edebilirim' , 
        'saati söyleyebiilirim' , 
        'hava durumunu söylerim' ,
        'googleda arama yaparım' ,
        'sana fıkra anlatabilirim',
         'yada hikaye anlatabilirim ', 
         'youtube dan birşeyler arayabilrim',
         ' peki sen ne yapmamı istersin']
        secim = choice(sozler)
        speak(secim)
        
        
        print(Fore.GREEN)
        print('seninle sohbet edebilirim' , 
        'saati söyleyebiilirim' , 
        'hava durumunu söylerim' ,
        'googleda arama yaparım' ,
        'sana fıkra anlatabilirim',
         'yada hikaye anlatabilirim ', 
         'youtube dan birşeyler arayabilrim',
         ' peki sen ne yapmamı istersin')

    if 'iyiyim' in voice:# eğer voice nin içinde iyiyim diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("Sesli Asistan , iyi olmana sevindim senin için ne yapabilirim")#Sesli asistanın değini ekrana yazdırmak icin
        speak("iyi olmana sevindim senin için ne yapabilirim")#sesli bir şekilde söylenmesi için
    
    if 'kötüyüm'  in voice:# eğer voice nin içinde kötüyüm diye bir değer varsa bunları yap
        #sozlerOlumsuz adlı bir dizi tanımlıyoruz
        sozlerOlumsuz = ["üzüldüm senin adına ne yapabilirim",
                "sıkma canını gelir gecer",
                "kendini üzme iyi olmaya bak",
                
        ]
        secimolumsuz=choice(sozlerOlumsuz)#sozlerden birini karışık olarak seçilecek

        speak(secimolumsuz)#seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("Sesli Asistan , "+secimolumsuz)#Sesli asistanın değini ekrana yazdırmak icin

    if 'Fıkra anlat' in voice:# eğer voice nin içinde Fıkra anlat diye bir değer varsa bunları yap
        #fıkralar adlı bir dizi tanımlıyoruz
        fıkralar = ["Temel iyice yaşlanmış, yaş doksan beş olmuş. Bir gün Azrail çıkagelmiş. Temel,", 
        "Ne yapsam da paçayı yırsam' diye düşünmeye başlamış. 'Hah buldum. Çocuk taklidi yapayım, beni tanımasın demiş", 
        "Azrail iyice yaklaşınca başlamış ağlamaya; ”Ingaa! Ingaa!..” Azrail Temel'in kulağına eğilmiş ve şöyle demiş;- “atta,atta demis."

                
        ]
        secimfık=choice(fıkralar)#sozlerden birini karışık olarak seçilecek

        speak(secimfık)#seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("Sesli Asistan , "+secimfık)#Sesli asistanın değini ekrana yazdırmak icin

    if 'Hikaye anlat' in voice:# eğer voice nin içinde hikaye anlat diye bir değer varsa bunları yap
        #fıkralar adlı bir dizi tanımlıyoruz
        hikayeler=[
                "Karnını doyurmak için yiyecek bir şeyler bulmaya çıkan kurt, gecenin karanlığında sessiz sessiz yürüyordu. Çok aç olduğu belliydi. Ayın bedenine vuran ışıklarından nerdeyse kemikleri sayılıyordu. Patikaya doğru ilerlerken; iyi beslendiği her halinden belli olan heybetli ve tüyleri oldukça bakımlı bir köpekle karşılaştı. Onun bu haline imrenen kurt",

                "Ne şanslısın! Sana bakacak ve karnını doyuracak insanlar, gece güvenle uyuduğun bir yuvan var. Bu halinden ne kadar da memnun görünüyorsun"
        ]
        secimhikaye=choice(hikayeler)#hikayelerden birini karışık olarak seçilecek

        speak(secimhikaye)#seçilen hikaye seslendiriliecek
        print(Fore.GREEN)
        print("Sesli Asistan , "+secimhikaye)#Sesli asistanın değini ekrana yazdırmak icin

    if 'saat kaç' in voice:# eğer voice nin içinde saat kaç diye bir değer varsa bunları yap
        speak(datetime.now().strftime('%H:%M:%S'))#datetime ile o anki saati alıyor ve bize söylüyor.
        print(Fore.GREEN)
        print("Sesli Asistan , "+datetime.now().strftime('%H:%M:%S'))#datetime ile alınan veriyi ekrana yazdırıyoruz

    if 'arama yap' in voice:# konusan kisi arama yap derse voice içinde bu tanımlanır alttaki satıları çalıştırıyor.
        search = record('ne aramamı istersin')#record ile sesli asistan cevap veriyor ve google sayfasında arama yapıyor.
        url ='https://google.com/search?q='+search#https://google.com/search?q= seski olarak aldıgı veriyi google da aramasını sağlıyoruz.
        webbrowser.get().open(url)#bulduklarını dosya icinde bize açıyor
        speak(search+' için bulduğum sonuçlar')#buldugunu sonucları sesli asistana söyletiyoruz
        print(Fore.GREEN)
        print("Sesli Asistan , "+search+' için bulduğum sonuçlar')#Sesli asistanın değini ekrana yazdırmak icin
    
    if "YouTube'da ara" in voice:#  konusan kisi youtube da ara derse voice içinde bu tanımlanır alttaki satıları çalıştırıyor.
        searchy = record('ne aramamı istersin')#record ile aranmasını istediğimiz kelimeyi yada cümleyi alıp searchy değişkenine tanımlıyouz
        urly ='https://www.youtube.com/watch?v='+searchy#https://google.com/search?q= seski olarak aldıgı veriyi google da aramasını sağlıyoruz.
        webbrowser.get().open(urly)#web browserı açıyouz ve  urly değişkenini dönderiyouz
        speak(searchy+' için bulduğum sonuçlar')#sesli bir şekilde seslendirme yapıyouz
        print(Fore.GREEN)
        print("Sesli Asistan ,  "+searchy+' için bulduğum sonuçlar')#ekrana yazdırma yapıyouz
    
    if 'hava durumu' in voice:# konusan kisi hava durumu derse voice içinde bu tanımlanır alttaki satıları tanımlıyor.
        #feedparser ile link deki veriyi çekip parçalıyouz bunuda parse değişkenine tanımlıyouz
        parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|71100|KIRIKKALE|")
        parse = parse["entries"][0]["summary"]
        parse = parse.split()
        havail=parse[2] #havaiiladlı adlı değişkene parsenin 3.değeri olan il adını tanımlıyoruz
        havadetay=parse[4] #havadetay adlı  değişkene parsenin 5. değeri olan dereceyi tanımlıyoruz
        speak(havail+" için hava"+havadetay+" derece")#sesli söyletiyoruz
        print(Fore.GREEN)
        print("Sesli Asistan , "+havail+" için hava"+havadetay+" derece")#ekrana yazdırıyouz
             
    if 'teşekkür ederim'  in voice:# eğer voice nin içinde teşekkür ederim diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("Sesli Asistan , ne demek herzaman")#Sesli asistanın değini ekrana yazdırmak icin
        speak("ne demek herzaman")#sesli bir şekilde söylenmesi için


    if 'güle güle' in voice:# konusan kisi güle güle derse lattaki satırları çalıştırıyor.
        speak('görüşürüz')#sesli asistan konuşarak görüsürüz diyor
        print(Fore.GREEN)
        print('Sesli Asistan , Görüşürüz')#ekrana yazdırıyouz
        exit()# Programdan çıkış yapıyoruz

def speak(string):#speak adlı bir fonksiyon oluştuyouz 
    tts = gTTS(string,lang='tr')#sesi text e türkçe olarak çevirip tts adlı değişkene tanımlıyouz
    rand=random.randint(1,100)#ses dosyyalarını 1-100 arasında bir sayı ekleyrek kayıt ediyoruz.Her çalıştırığında random bir sayı ile kaydedecek.
    file= 'ses-'+str(rand)+'.mp3'#.mp3 uzantılı bir ses dosyası oluşturup kayıt yapıyoruz
    tts.save(file)#dosyayı kayıt ediyoruz.
    playsound(file)#dosyayı okutuyoruz.
    os.remove(file)#dosyayı siliyouz.






speak('Seni dinliyorum Senin için ne yapabilirim')#ilk açılışta asiatanın bizi karşılaması için.
print(Fore.GREEN) # yazıyı yeşil yazdırıyoruz.
print('Sesli Asistan , Seni dinliyorum Senin için ne yapabilirim')#program başladığında bizi bu şekilde karşılıyor.
time.sleep(1)#1 saniye ara ile çalıştırıyoruz.
while 1:#Soru sorduktan sonra konusmaya devam edebilmek icin sonsuz döngüye alıyoruz.
    voice=record()
    print(Fore.BLUE)
    print(voice)
    response(voice)
    print(Fore.GREEN)
    speak('başka bir isteğin var mı?')
    print('Başka bir istegin var mı?')
