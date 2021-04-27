#!/usr/bin/python3
# By Tedezed
from gtts import gTTS
import os, sys, subprocess, re, pyttsx3
from io import BytesIO
from nltk.corpus import wordnet as wn

server = "localhost"

def generate_audio(language, mytext, file_name, save=False, offline=False):
    try:
        if save:
            f = open(file_name)
            f.close()
            print("Audio in cache: %s" % (file_name))
        else:
            f = open("skME3J.3OPLDDEWWde")
            f.close()
    except IOError:
        if offline:
            engine = pyttsx3.init()
        else:
            myobj = gTTS(text=mytext, lang=language, slow=False)

        if save:
            if offline:
                engine.save_to_file(mytext, file_name)
            else:
                myobj.save(file_name)
        else:
            if offline:
                print("Offline mode not support save file off")
                raise
            else:
                fp = BytesIO()
                myobj.write_to_fp(fp)
                fp.seek(0)
                return fp.read()
        #os.system("vlc %s" % (file_name))

def dict_parse(mytext, server, dict_output):
    #print(dict_output)
    list_output = dict_output.decode("utf-8", "replace").split(server)
    list_output.pop(0)
    list_of_lines = []
    dict_parse_output = {}
    for idx, line in enumerate(list_output):
        list_line = line.replace("  ", "").split("\n")
        list_line.pop(0)
        list_line.pop(len(list_line) -1)
        #print(idx, list_line)
        list_of_lines.append(list_line)
    meaning = []
    if list_of_lines != []:
        for idx, p in enumerate(list_of_lines[0]):
            if idx == 0:
                list_first_line = p.split(" ")
                dict_parse_output["word"] = list_first_line[0]
                dict_parse_output["pronunciation"] = list_first_line[1]
                dict_parse_output["type"] = word_type(mytext)
            else:
                meaning.append(re.sub(r'[0-9]+\. ', '', p))
        dict_parse_output["meaning"] = meaning
        return dict_parse_output
    else:
        return list_of_lines

# def generate_translation(dictionary, mytext):
#     dict_execution = subprocess.r(dict_output).split(server)
#     list_output.pop(0)
#     for idx, line in enumerate(list_output):
#         print(idx, line.split("\\n"))

def generate_translation(dictionary, mytext):
    dict_execution = subprocess.run(["dict", "-d", dictionary, "-f", mytext], stdout=subprocess.PIPE)
    return dict_parse(mytext, server, dict_execution.stdout)

def word_type(mytext):
    list_w = wn.synsets(mytext)
    if list_w == []:
        return 'x'
    type_w = list_w[0].pos()
    if type_w == 'n':
        return 'Noun'
    if type_w == 'v':
        return 'Verb'
    if type_w == 'a':
        return 'Adjetive'
    if type_w == 's':
        return 'Adjetive Satellite'
    if type_w == 'r':
        return 'Adverb'
    return type_w

def main():
    # language = 'en'
    # dictionary = 'fd-eng-spa'
    # mytext = 'Welcome'
    language = sys.argv[1]
    dictionary = sys.argv[2]
    mytext = sys.argv[3]
    
    os.system("mkdir -p audio_%s" % (language))
    file_name = "audio_%s/%s.mp3" % (language, mytext.replace(" ", "_"))

    generate_audio(language, mytext, file_name, True)
    print(generate_translation(dictionary, mytext))

if __name__ == "__main__":
    main()