#!/usr/bin/python3
# By Tedezed
import sys, os, genanki, json
import translator, giphy_tools

def list_html_generator(elements):
    list_html = "<ul>"
    for s in elements:
        ul = "<li>" + str(s) + "</li>"
        list_html += ul
    list_html += "</ul>"
    return list_html

def check_file(file_name):
    print('Check file: %s ' % (file_name))
    f = open(file_name)
    f.close()

def custom_desk(language, dictionary, desk_name, source_json, audio, image):
    custom_model = genanki.Model(
      1091735104,
      'Simple Model with Media',
      fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Type'},
        {'name': 'Pronunciation'},
        {'name': 'Meaning'},
        {'name': 'Sound'},
        {'name': 'Image'},
      ],
      templates=[
        {
          'name': 'Card 1',
          'qfmt': '<h1>{{Question}}<h1\><br>{{Sound}}<br>{{Image}}{{type:Answer}}',
          'afmt': '{{FrontSide}}<hr id="answer">{{Meaning}}Pronunciation: {{Pronunciation}}',
        },
      ])

    custom_deck = genanki.Deck(
      2059400110,
      desk_name)

    with open(source_json) as json_file:
        source_data = json.load(json_file)
    
    list_words_not_found = []
    list_media = []
    for word in source_data['commonWords']:
        file_name_mp3 = "audio_%s/%s.mp3" % (language, word.replace(" ", "_"))
        file_name_gif = "images_%s/%s.gif" % (language, word.replace(" ", "_"))
        dict_word = translator.generate_translation(dictionary, word)
        sound_mp3 = translator.generate_audio(language, word, file_name_mp3, save=True)
        file_name_gif = giphy_tools.get_gif(word, file_name_gif, image)

        if dict_word != []:
            custom_note = genanki.Note(
              model=custom_model,
              fields=[
                  dict_word['word'], 
                  dict_word['meaning'][0], 
                  dict_word['type'], 
                  dict_word['pronunciation'],
                  list_html_generator(dict_word['meaning']),
                  '[sound:%s.mp3]' % (dict_word['word']),
                  '<img src="%s.gif">' % (dict_word['word'])
              ]
            )
            custom_deck.add_note(custom_note)
            check_file(file_name_mp3)
            check_file(file_name_gif)
            list_media.append(file_name_mp3)
            list_media.append(file_name_gif)
        else:
            list_words_not_found.append(word)

    custom_package = genanki.Package(custom_deck)
    custom_package.media_files = list_media
    custom_package.write_to_file('anki_desks_output/%s.apkg' % (desk_name))
    f = open("words_not_found.log", "a")
    f.write("Not found: %s" % (list_words_not_found))
    f.close()

def main():
    #language_to_learn = 'en'
    #dictionary_mother_language = 'fd-eng-spa'
    #desk_name = 'Common English words for Spanish speakers'
    #source_json = 'corpora/data/words/common.json'
    type_desk = sys.argv[1]
    language_to_learn = sys.argv[2]
    dictionary_mother_language = sys.argv[3]
    desk_name = sys.argv[4]
    source_json = sys.argv[5]

    if type_desk == 'audio_image':
        image = True
        audio = True
    elif type_desk == 'audio_only':
        image = False
        audio = True
    else:
        print('[ERROR] Not valid var type_desk parameter (1)')
        exit(1)

    # python3 main.py audio_images en fd-eng-spa 'Common English words for Spanish speakers' corpora/data/words/common.json
    # python3 main.py audio_only en fd-eng-spa 'Common English words for Spanish speakers' corpora/data/words/common.json

    os.system("mkdir -p audio_%s" % (language_to_learn))
    os.system("mkdir -p images_%s" % (language_to_learn))
    os.system("mkdir -p anki_desks_output")

    custom_desk(language_to_learn, dictionary_mother_language, desk_name, source_json, audio, image)

if __name__ == "__main__":
    main()