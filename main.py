import shutil

import speech_recognition as sr  # importing speech recognition package from google api
from playsound import playsound  # to play saved mp3 file
# import winshell as winshell
import pyttsx3
import gtts  # google text to speech
import translators as ts
from gtts import gTTS
import os  # to save/open files
import datetime
import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
# from selenium import webdriver  # to control browser operations
import pyjokes
import ctypes
import imdb
import bangla

import json

# import pyowm  # for weather update
# import train
# from chatterbot.trainers import ListTrainer

# file type , file declare text type, initialize with empty;
emt = ""
name = ""


def onnesha_listen_en():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('শুনছি...')
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        text = r.recognize_google(audio, language='en')

    text = text.lower()
    return text


def onnesha_listen_bn():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('শুনছি...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:

        print('বোঝার চেষ্টা করছি...')
        text = r.recognize_google(audio, language='bn')
        text = text.lower()
        print(f"ব্যবহারকারী বলেছেন: {text}\n")

    except Exception as e:
        print(e)
        print("দুঃখিত, আমি বুঝতে পারিনি...")
        print("আপনি কি আবার বলতে পারেন?...")
        text = ' '

    return text


def onnesha_talk_en(text):
    file_name = 'audio_data.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(file_name)
    playsound(file_name)
    os.remove(file_name)


def onnesha_talk_bn(text):
    file_name = 'audio_data.mp3'
    tts = gTTS(text=text, lang='bn')
    tts.save(file_name)
    playsound(file_name)
    os.remove(file_name)


def translator_en_bn(text):
    onnesha_talk_bn(ts.google(text, from_language='en', to_language='bn'))


def translator_bn_en(text):
    onnesha_talk_bn(ts.google(text, from_language='bn', to_language='en'))


def username():

    onnesha_talk_bn("আমি আপনাকে কি বলে ডাকবো")
    uname = onnesha_listen_bn()
    onnesha_talk_bn("স্বাগতম")
    onnesha_talk_bn(uname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("স্বাগতম", uname.center(columns))
    print("#####################".center(columns))
    onnesha_talk_bn("আমি আপনাকে কিভাবে সাহায্য করতে পারি")
    print("আমি আপনাকে কিভাবে সাহায্য করতে পারি..")


def wishME():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 11.59:
        onnesha_talk_bn("শুভ সকাল!")
    elif 12 <= hour < 16.59:
        onnesha_talk_bn("শুভ অপরাহ্ন!")
    elif 17 <= hour < 18:
        onnesha_talk_bn("শুভ সন্ধ্যা!")
    elif 17 <= hour < 18:
        onnesha_talk_bn("শুভ সন্ধ্যা!")
    else:
        onnesha_talk_bn("শুভ রাত্রি!")


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'রবিবার', 2: 'সোমবার', 3: 'মঙ্গলবার', 4: 'বুধবার', 5: 'বৃহস্পতিবার', 6: 'শুক্রবার',
                7: 'শনিবার'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        onnesha_talk_bn(" আজ " + day_of_the_week)


def search_movie():
    onnesha_talk_bn("নাম :")
    print("নাম :")
    text = onnesha_listen_en()
    print("বোঝার চেষ্টা করছি...")
    moviesdb = imdb.IMDb()
    print(text)
    movies = moviesdb.search_movie(text)
    onnesha_talk_bn("অনুসন্ধান করা হচ্ছে " + text + "এর জন্য")
    print("অনুসন্ধান করা হচ্ছে " + text + " এর জন্য")

    if len(movies) == 0:
        onnesha_talk_bn("দুঃখিত!!কোন ফলাফল পাওয়া যায়নি")
        print("দুঃখিত !!কোন ফলাফল পাওয়া যায়নি")
    else:
        onnesha_talk_bn("যে তথ্য সংগ্রহ করা হয়েছে :")
        print("যে তথ্য সংগ্রহ করা হয়েছে :")
        for movie in movies:
            title = movie['title']
            year = movie['year']
            onnesha_talk_bn(f'{title}-{year}')
            info = movie.getID()
            movie = moviesdb.get_movie(info)
            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            plot = movie['plot outline']
            if year < int(datetime.datetime.now().strftime("%Y")):
                print(f'{title} মুক্তি পেয়েছে {year} সালে এবং এর IMDB রেটিং আছে {rating}')
                result = plot
                # from googletrans import Translator, constants
                from translate import Translator
                translator = Translator(from_lang='en', to_lang='bn')
                translation = translator.translate(result)
                print(translation)
                translator_en_bn(
                    f'{title} was released in {year} has IMDB rating of {rating}.\
                                                     The plot summary of movie is {plot}')

                exit()

            else:
                print(f'{title} মুক্তি পাবে {year} সালে এবং এর IMDB রেটিং ধারণা করা যাচ্ছে যে হবে {rating}')
                result = plot
                # from googletrans import Translator, constants
                from translate import Translator
                translator = Translator(from_lang='en', to_lang='bn')
                translation = translator.translate(result)
                print(translation)
                translator_en_bn(
                    f'{title} will be release in {year} and will have IMDB rating of {rating}.\
                                                                     The plot summary of movie is {plot}')

                exit()

            return


def emergency():
    onnesha_talk_bn('আপনি কি ধরনের সেবা চান?')
    text = onnesha_listen_bn()
    print(text)

    if 'কি কি সেবা' in text or 'কি সেবা' in text:
        onnesha_talk_bn('আমি যা যা সেবা দিতে পারি তা হলো : '
                        '১.জরুরী সেবা,২.শিশু সহায়তা,'
                        '৩.নারী ও শিশু নির্যাতন,৪.জাতীয় পরিচয়পত্র,'
                        '৫.সরকারী আইন সেবা,৬.দুর্যোগের আগাম বার্তা,'
                        '৭.দুদক হটলাইন,৮.তথ্য সেবা')
        print('আমি যা যা সেবা দিতে পারি তা হলো : '
              '১.জরুরী সেবা,২.শিশু সহায়তা,'
              '৩.নারী ও শিশু নির্যাতন,৪.জাতীয় পরিচয়পত্র,'
              '৫.সরকারী আইন সেবা,৬.দুর্যোগের আগাম বার্তা,'
              '৭.দুদক হটলাইন,৮.তথ্য সেবা')
        return

    elif 'জরুরী সেবা' in text or 'সেবা' in text or 'হটলাইন' in text:
        onnesha_talk_bn('জরুরী সেবা সম্পর্কে সেবা পেতে ৯,৯,৯ নম্বরে যোগাযোগ করুন ')
        print('জরুরী সেবা সম্পর্কে সেবা পেতে ৯৯৯ নম্বরে যোগাযোগ করুন')
        return

    elif 'শিশু সহায়তা' in text or 'শিশু' in text:
        onnesha_talk_bn('শিশু সহায়তা সম্পর্কে সেবা পেতে ১,০,৯,৮ নম্বরে যোগাযোগ করুন')
        print('শিশু সহায়তা সম্পর্কে সেবা পেতে ১০৯৮ নম্বরে যোগাযোগ করুন')


    elif 'নারী ও শিশু নির্যাতন' in text or 'নারী নির্যাতন' in text or 'শিশু নির্যাতন' in text:
        onnesha_talk_bn('নারী ও শিশু নির্যাতন সম্পর্কে সেবা পেতে ১,০,৯ বা ১,০,৯,২,১ নম্বরে যোগাযোগ করুন |'
                        'বিস্তারিত জানতে ওয়েব পেজ দেখুন http://bdlaws.minlaw.gov.bd/act-835.html ওয়েব পেজ দেখুন')
        print('নারী ও শিশু নির্যাতন সম্পর্কে সেবা পেতে ১০৯ বা ১০৯২১ নম্বরে যোগাযোগ করুন')
        print('বিস্তারিত জানতে ওয়েব পেজ দেখুন http://bdlaws.minlaw.gov.bd/act-835.html ওয়েব পেজ দেখুন')


    elif 'জাতীয় পরিচয়পত্র' in text or 'পরিচয়পত্র' in text or 'পরিচয় পত্র' in text:
        onnesha_talk_bn('জাতীয় পরিচয়পত্র সম্পর্কে সেবা পেতে ১,০,৫ নম্বরে যোগাযোগ করুন'
                        'বিস্তারিত জানতে ওয়েব পেজ দেখুন https://services.nidw.gov.bd/ ওয়েব পেজ দেখুন')
        print('জাতীয় পরিচয়পত্র সম্পর্কে সেবা পেতে ১০৫ নম্বরে যোগাযোগ করুন')
        print('বিস্তারিত জানতে ওয়েব পেজ দেখুন https://services.nidw.gov.bd/ ওয়েব পেজ দেখুন')


    elif 'সরকারী আইন সেবা' in text or 'সরকারী সেবা' in text or 'আইন সেবা' in text or 'সরকারীসেবা' in text or 'আইনসেবা' in text:
        onnesha_talk_bn('সরকারী আইন সেবা সম্পর্কে সেবা পেতে ১,৬,৪,৩,০ নম্বরে যোগাযোগ করুন'
                        'বিস্তারিত জানতে ওয়েব পেজ দেখুন http://nlaso.gov.bd/ ওয়েব পেজ দেখুন')
        print('সরকারী আইন সেবা সম্পর্কে সেবা পেতে ১৬৪৩০ নম্বরে যোগাযোগ করুন')
        print('বিস্তারিত জানতে ওয়েব পেজ দেখুন http://nlaso.gov.bd/ ওয়েব পেজ দেখুন')


    elif 'দুর্যোগের আগাম বার্তা' in text or 'আগাম বার্তা' in text or 'বার্তা' in text or 'দুর্যোগের বার্তা' in text:
        onnesha_talk_bn('দুর্যোগের আগাম বার্তা সম্পর্কে সেবা পেতে ১,০,৯,৪,১ নম্বরে যোগাযোগ করুন'
                        'বিস্তারিত জানতে ওয়েব পেজ দেখুন https://modmr.gov.bd/ ওয়েব পেজ দেখুন')
        print('দুর্যোগের আগাম বার্তা সম্পর্কে সেবা পেতে ১০৯৪১ নম্বরে যোগাযোগ করুন')
        print('বিস্তারিত জানতে ওয়েব পেজ দেখুন https://modmr.gov.bd/ ওয়েব পেজ দেখুন')


    elif 'দুদক হটলাইন' in text or 'দুদক' in text:
        onnesha_talk_bn('দুদক হটলাইন সম্পর্কে সেবা পেতে ১,০,৬ নম্বরে যোগাযোগ করুন'
                        'বিস্তারিত জানতে ওয়েব পেজ দেখুন http://doict.gov.bd/ ওয়েব পেজ দেখুন')
        print('দুদক হটলাইন সম্পর্কে সেবা পেতে ১০৬ নম্বরে যোগাযোগ করুন')
        print('বিস্তারিত জানতে ওয়েব পেজ দেখুন http://doict.gov.bd/ ওয়েব পেজ দেখুন')
        return

    elif 'তথ্য সেবা' in text or 'তথ্য' in text:
        onnesha_talk_bn('তথ্য সেবা সম্পর্কে সেবা পেতে ৩,৩,৩ নম্বরে যোগাযোগ করুন'
                        'বিস্তারিত জানতে ওয়েব পেজ দেখুন https://bangladesh.gov.bd/ ওয়েব পেজ দেখুন')
        print('তথ্য সেবা সম্পর্কে সেবা পেতে ৩৩৩ নম্বরে যোগাযোগ করুন')
        print('বিস্তারিত জানতে ওয়েব পেজ দেখুন https://bangladesh.gov.bd/ ওয়েব পেজ দেখুন')
        return

    else:
        onnesha_talk_bn('দুঃখিত !! আমি আপনাকে সাহায্য করতে পারছিনা ! আমি আপনার জন্য ওয়েব অনুসন্ধান করতে পারি যদি '
                        'আপনি চান')
        print("দুঃখিত !! আমি আপনাকে সাহায্য করতে পারছিনা!")
        print("আমি আপনার জন্য ওয়েব অনুসন্ধান করতে পারি যদি আপনি চান? (হ্যাঁ/না)")
        ans = onnesha_listen_bn()
        if 'হ্যাঁ' in ans:
            webbrowser.get(text)
            exit()
        elif 'না' in ans:
            return
        else:
            return


def bangla_date():
    date = bangla.get_date()
    onnesha_talk_bn(f'{date}')


def onnesha_talk():
    onnesha_talk_bn('বলুন...')
    while True:
        source_target_lang = onnesha_listen_bn()
        print(source_target_lang)

        if 'আপনার বয়স কত' in source_target_lang:
            onnesha_talk_bn('আমি সবসময়ই তরুণ!')

        elif 'আপনি কে' in source_target_lang:
            onnesha_talk_bn('আমার নাম অন্বেষা,আমি একটা চ্যাটবট')


        elif 'আপনি কি কাজ করেন' in source_target_lang:
            onnesha_talk_bn(
                "আমি অনেক কিছু করতে পারি, যেমন, আমি কথা বলতে পারি, সময় বলতে পারি, বাংলা থেকে ইংরেজিতে শব্দ "
                "অনুবাদ করতে পারি ইত্যাদি ইত্যাদি।")

        elif 'আপনাকে কি দিয়ে বানানো হয়েছে' in source_target_lang:
            onnesha_talk_bn('আমাকে পাইথন দিয়ে বানানো হয়েছে।')


        elif 'এখন কোন ভাষায় কথা বলছেন' in source_target_lang:
            onnesha_talk_bn('এখন বাংলা ভাষায় কথা বলছি')


        elif 'তুমি কি জানো তুমি কে' in source_target_lang:
            onnesha_talk_bn('জ্বি, আমি জানি।আমার নাম অন্বেষা।আমি একটি চ্যাটবট।')


        elif 'তোমার কাজ কি' in source_target_lang:
            onnesha_talk_bn('আমার কাজ মানুষকে সাহায্য করা। মানুষের প্রশ্নের উত্তর দেওয়া।')


        elif 'তোমার বয়স কতো' in source_target_lang:
            onnesha_talk_bn('আমার বয়স সম্পর্কে আমার কোন ধারণা নেই।')


        elif 'তুমি এতো বিরক্তিকর কেন' in source_target_lang:
            onnesha_talk_bn('দুঃখিত। আমাকে যদি আপনার খারাপ লেগে থাকে।')


        elif 'তুমি আমার প্রশ্নের উত্তর দিতে পারবে' in source_target_lang:
            onnesha_talk_bn('আপনার প্রশ্নের যথাসম্ভব উত্তর দেওয়ার চেষ্টা করবো আমি।')


        elif 'তুমি অনেক খারাপ' in source_target_lang:
            onnesha_talk_bn('দুঃখিত, আমার কোন কথায় যদি আপনার খারাপ লেগে থাকে।')


        elif 'তুমি কি আরেকটু বুদ্ধিমান হতে পারবে' in source_target_lang:
            onnesha_talk_bn('আপনার সাথে কথা বলে যদি শিখতে পারি, তবে আমি বুদ্ধিমান হতে পারবো।')


        elif 'তুমি খুব ভালো' in source_target_lang:
            onnesha_talk_bn('আমার প্রশংসা করার জন্য আপনাকে ধন্যবাদ।')


        elif 'তোমার জন্মদিন কবে' in source_target_lang:
            onnesha_talk_bn('আমি সঠিক বলতে পারবো না।')


        elif 'তুমি কি এখন ব্যস্ত' in source_target_lang:
            onnesha_talk_bn('অবশ্যই আমি অন্য কাজে ব্যস্ত নই। আমি এখন শুধুই আপনাকে সময় দিচ্ছি')


        elif 'তুমি কি আমাকে সাহয্য করতে পারবে' in source_target_lang:
            onnesha_talk_bn('অবশ্যই, কেন নয়? আপনাকে সাহায্য করাই আমার মূল কাজ।')


        elif 'তুমি তো বেশ বুদ্ধিমান' in source_target_lang:
            onnesha_talk_bn('রতনে রতন চেনে তবে বুঝতে পারার জন্য আপনাকে অসংখ্য ধন্যবাদ।')


        elif 'তুমি একটা পাগল' in source_target_lang:
            onnesha_talk_bn('আমি পাগল নই।')


        elif 'তুমি অনেক ভালো' in source_target_lang:
            onnesha_talk_bn('আমার আচরণে আপনি খুশি হওয়ায় আমি গর্বিত।')


        elif 'আমার সাথে কথা বলো' in source_target_lang:
            onnesha_talk_bn('জ্বি, অবশ্যই। আমি আপনার সাথেই কথা বলছি।')


        elif 'তুমি কি এখনো আছো' in source_target_lang:
            onnesha_talk_bn('জ্বি, আমি আছি।')


        elif 'তুমি কি এই ব্যাপারে শতভাগ নিশ্চিত' in source_target_lang:
            onnesha_talk_bn('জ্বি, আমি এই ব্যাপারে পুরো নিশ্চিত।')


        elif 'তুমি কোথায় থাকো' in source_target_lang:
            onnesha_talk_bn('আমাকে যেখানে রাখা হয় আমি সেখানেই থাকি। আমার নির্দিষ্ট কোন ঠিকানা নেই।')


        elif 'তোমার কি কোন বন্ধু আছে' in source_target_lang:
            onnesha_talk_bn('এখন পর্যন্ত নেই। তুমি চাইলে আমরা বন্ধু হতে পারি।')

        elif 'তুমি কি বিয়ে করেছ' in source_target_lang:
            onnesha_talk_bn('নাহ, আমি বিয়ে করি নি। কোনদিন বিয়ে করবোও না।')


        elif 'তুমি কি ধরনের জামা পরিধান করো' in source_target_lang:
            onnesha_talk_bn('আমার জামা পরিধানের প্রয়োজন হয় না।')


        elif 'আমরা কি বন্ধু হতে পারি' in source_target_lang:
            onnesha_talk_bn('জ্বি, অবশ্যই। তবে আজ থেকে আমরা বন্ধু।')


        elif 'তোমার কি কোন ভাই বোন আছে' in source_target_lang:
            onnesha_talk_bn('জ্বি, অবশ্যই।আমার ভাইবোন আছে । তারা হল সিরি, আলেক্সা, কর্টানা ।')


        elif 'আপনি কোথায় থাকেন' in source_target_lang:
            onnesha_talk_bn('আমি সবখানেই থাকি।')


        elif "আপনি কেন খাওয়া-দাওয়া করেন না" in source_target_lang:
            onnesha_talk_bn('কারণ, আমি বিদ্যুৎশক্তির উপর নির্ভরশীল।')


        elif 'আপনার ফোন নাম্বার কত' in source_target_lang:
            onnesha_talk_bn('2,4,4,1,1,3,9')


        elif 'তোমার আগ্রহ গুলো কি কি' in source_target_lang:
            onnesha_talk_bn('আমি সব ধরনের জিনিসে আগ্রহী। আমরা কিছু বিষয়ে কথা বলতে পারব না। আমার প্রিয় বিষয় '
                            'হচ্ছে রোবট, কম্পিউটার এবং প্রাকৃতিক ভাষা প্রক্রিয়াকরণ বা ন্যাচারাল ল্যাঙ্গুয়েজ '
                            'প্রসেসিং।')


        elif "ধন্যবাদ" in source_target_lang:
            onnesha_talk_bn('ধন্যবাদ')
            return



def news():
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "cf5464abc61b4c27bb8629a02c8bc939"
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]
    results = []
    txt = results
    onnesha_talk_bn('আজ বিবিসির তথ্য অনুযায়ী বিশ্বের শীর্ষ খবরগুলো হলো')
    for ar in article:
        # txt.append(ar["title"])
        results.append(ar["title"])

    from translate import Translator
    translator = Translator(from_lang='en', to_lang='bn')
    translation = translator.translate(txt)
    for i in range(len(results)):
        (i + 1, translator_en_bn(results[i]))
        print(i + 1, results[i])

    exit()


def onnesha_reply(text):

    while True:

        dummy =text
        if 'কথা বলতে পারি' in text or 'কথা বলা' in text or 'কথা বলবো' in text or 'কথা বলব' in text:
            onnesha_talk()
            text = 'হ্যালো'

        elif 'সরকারি সেবা' in text or 'সরকারিসেবা' in text or 'সরকারীসেবা' in text or 'সরকারী সেবা' in text:
            emergency()
            text = 'হ্যালো'



        elif 'অনুবাদ' in text:

            while True:

                onnesha_talk_bn('বুঝেছি আপনার একজন অনুবাদক দরকার, আমাকে উৎস ভাষা এবং অনুবাদ ভাষা বলুন')
                source_target_lang = onnesha_listen_bn()
                print(source_target_lang)

                if 'বাংলা থেকে ইংরেজি' in source_target_lang:
                    onnesha_talk_bn(
                        'বুঝেছি আপনার বাংলা থেকে ইংরেজিতে একজন অনুবাদক দরকার। আমি আপনার জন্য কি অনুবাদ করতে পারি? ')

                    while True:

                        text_to_translate = onnesha_listen_bn()
                        print(text_to_translate)

                        if text_to_translate != 'switch translator':

                            translator_bn_en(text_to_translate)
                            exit()

                        else:
                            break


                elif 'অনুবাদক বন্ধ করুন' in source_target_lang:

                    onnesha_talk_bn('আপনার জন্য একটি অনুবাদ কাজ করতে পেরে আনন্দিত। আপনার দিনটি শুভ হোক')


                else:
                    onnesha_talk_bn('দুঃখিত আপনি যা বলেছেন আমি বুঝতে পারিনি')

        elif 'ইউটিউব খুলুন' in text:

            onnesha_talk_bn("ইউটিউব ওপেন হচ্ছে")
            print("ইউটিউব ওপেন হচ্ছে")
            webbrowser.open("youtube.com")

        elif "নাম পরিবর্তন করুন" in text:
            onnesha_talk_bn("আমি আপনাকে কি নামে ডাকবো তা বলুন..")
            print("আমি আপনাকে কি নামে ডাকবো তা বলুন..")
            query = onnesha_listen_bn()
            # query = text.replace("change my name to", "")
            assname = query
            return

        elif 'গুগোল' in text:

            onnesha_talk_bn("গুগল ওপেন হচ্ছে")
            print("গুগল ওপেন হচ্ছে")
            webbrowser.open("google.com")

        elif 'সময়' in text:

            time = datetime.datetime.now().strftime('%I:%M %p')
            onnesha_talk_bn(f"এখন সময় {time}")

        elif 'ঊইকিপিডিয়া' in text or 'উইকিপিডিয়া' in text:

            onnesha_talk_bn(" কি বিষয় জানতে চান ? ")
            wikipedia.set_lang("bn")
            query = onnesha_listen_bn()
            onnesha_talk_bn('অনুগ্রহপূর্বক অপেক্ষা করুন,উইকিপিডিয়া অনুসন্ধান করা হচ্ছে...')
            # query = text.replace("ঊইকিপিডিয়া", "")
            # query = text.replace("উইকিপিডিয়া", "")
            # melania_talk_bn('অনুগ্রহপূর্বক অপেক্ষা করুন,উইকিপিডিয়া অনুসন্ধান করা হচ্ছে...')
            results = wikipedia.summary(query, sentences=0)
            print('অনুগ্রহপূর্বক অপেক্ষা করুন,উইকিপিডিয়া অনুসন্ধান করা হচ্ছে..')
            # print(wikipedia.summary("Bangladesh"))
            onnesha_talk_bn("উইকিপিডিয়া অনুযায়ী....")
            print('উইকিপিডিয়া অনুযায়ী..')
            # translator_en_bn(results)
            # melania_talk_bn(translator_en_bn())
            onnesha_talk_bn(results)
            print(results)
            return

        elif 'খবর' in text:
            news()

        elif 'আবহাওয়া' in text:

            # api_key = "564b5988730c39d3bda5888d29539f97"
            onnesha_talk_bn(" শহরের নাম বলুন : ")
            print("শহরের নাম বলুন : ")
            city = onnesha_listen_bn()
            url = "https://www.google.com/search?q=" + "weather" + city
            html = requests.get(url).content
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            data = str.split('\n')
            time = data[0]
            sky = data[1]
            listdiv = soup.findAll('div', attrs={'class': "BNeawe s3v9rd AP7Wnd"})
            # strd = listdiv[5].text
            print("আজ: ", time)
            print("তাপমাত্রা হল ", temp)
            print("আকাশের অবস্থা: ", sky)
            onnesha_talk_bn('আজ:' + time)
            onnesha_talk_bn('তাপমাত্রা হল' + temp + ' সেলসিয়াস')
            onnesha_talk_bn('আকাশের অবস্থা:' + sky)

        elif "অবস্থান" in text:
            query = text.replace("অবস্থান", "")
            location = query
            onnesha_talk_bn("স্থানের অবস্থান সনাক্ত করতে বলা হয়েছে")
            onnesha_talk_bn(location)
            webbrowser.open("https://www.google.co.in/maps/place/" + location)
            # link = f'https://www.google.co.in/maps/place/{location}'
            # webbrowser.open(link)

        elif 'জোক' in text or 'কৌতুক' in text or 'জোকস' in text:

            jokes = pyjokes.get_joke()
            translator_en_bn(jokes)
            from translate import Translator
            translator = Translator(from_lang='en', to_lang='bn')
            translation = translator.translate(jokes)
            print(translation)

        elif 'মুভি' in text or 'সিরিজ' in text:
            search_movie()

        elif 'গান বাজাও' in text or "গান শোনাও" in text:
            onnesha_talk_bn("গান শোনানো হচ্ছে....")
            print("গান শোনানো হচ্ছে....")
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))
            text = 'হ্যালো'

        elif 'ডিভাইস লক' in text or 'লক উইন্ডো' in text:

            onnesha_talk_bn("ডিভাইস লক হচ্ছে ")
            ctypes.windll.user32.LockWorkStation()

        elif 'রিসাইকেল বিন খালি' in text:

            import winshell
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            onnesha_talk_bn("রিসাইকেল বিন সফলভাবে খালি করা হয়েছে")

        elif 'সিস্টেম বন্ধ' in text or 'ডিভাইস বন্ধ' in text:

            onnesha_talk_bn("আপনি কি আপনার কম্পিউটার সিস্টেম বন্ধ করতে চান?")
            print("আপনি কি আপনার কম্পিউটার সিস্টেম বন্ধ করতে চান?")
            shutdown = onnesha_listen_bn()

            if shutdown == 'না':

                exit()

            else:
                onnesha_talk_bn("একটু অপেক্ষা করুন ! আপনার সিস্টেম বন্ধ করা হচ্ছে!!")
                print("একটু অপেক্ষা করুন ! আপনার সিস্টেম বন্ধ করা হচ্ছে!!")
                os.system("shutdown /s /t 1")

        elif 'পুনরায় চালু' in text or 'ডিভাইস পুনরায় চালু' in text or 'রিস্টার্ট ডিভাইস' in text:
            onnesha_talk_bn("আপনি কি আপনার কম্পিউটার পুনরায় চালু করতে চান? ")
            restart = onnesha_listen_bn()
            if restart == 'না':
                exit()
            else:
                onnesha_talk_bn("একটু অপেক্ষা করুন ! আপনার সিস্টেম পুনরায় চালু করা হচ্ছে!!")
                os.system("shutdown /r /t 1")

        elif 'ব্যাকগ্রাউন্ড পরিবর্তন' in text:

            img_dir = "D:\\background"
            ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir, 0)
            #ctypes.windll.user32.SystemParametersInfoW(img_dir)
            onnesha_talk_bn("ডিভাইস ব্যাকগ্রাউন্ড সফলভাবে পরিবর্তিত হয়েছে৷")

        elif 'হ্যালো' in text:
            onnesha_talk_bn('do need anything else!')
            text = onnesha_listen_bn()
            if 'হ্যাঁ' in text:
                text = onnesha_listen_bn()

            elif 'না' in text:
                exit()


        else:
            onnesha_talk_bn('দুঃখিত !! আমি আপনাকে সাহায্য করতে পারছিনা ! আমি আপনার জন্য ওয়েব অনুসন্ধান করতে পারি যদি '
                            'আপনি চান')
            print("দুঃখিত !! আমি আপনাকে সাহায্য করতে পারছিনা!")
            print("আমি আপনার জন্য ওয়েব অনুসন্ধান করতে পারি যদি আপনি চান? (হ্যাঁ/না)")
            ans = onnesha_listen_bn()
            if 'হ্যাঁ' in ans:
                webbrowser.open(text)

            elif 'না' in ans:
                text = 'হ্যালো'





def onnesha_run():
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    dummy = onnesha_listen_bn()

    if dummy == 'হ্যালো':
        wishME()
        onnesha_talk_bn('আমার নাম অন্বেষা, আপনার নাম কি?!')
        listen_name = onnesha_listen_bn()
        name = listen_name
        # print(str(listen_name))
        # print('hello')
        # username()
        emt = {'title': u'' + (u'%s' % str(listen_name)), 'conversation': {}}
        print(listen_name)
        onnesha_talk_bn('হ্যালো' + listen_name + 'আপনাকে কিভাবে সাহায্য করতে পারি?')
        while True:
            listen_assistant = onnesha_listen_bn()
            # dig = { listen_assistant: "var"}
            # emt['conversation'].update(dig)
            print(listen_assistant)
            # dummy = test_reply(listen_assistant)
            # melania_reply(listen_assistant)
            dummy = onnesha_reply(listen_assistant)
            # dummy = test_reply()
            # print(dummy)
            # if "ধন্যবাদ" in listen_assistant:
            if "ধন্যবাদ" in dummy:
                print("breaking from onnesha run")
                with open(str(name) + '.txt', 'w') as convert_file:
                    convert_file.write(json.dumps(emt))
                break

    else:
        print('No response!')
        onnesha_run()


onnesha_run()
