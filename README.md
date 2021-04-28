# Anki Desk Factory

Easy automate desk generator for Anki with input in json

Resume:
- Input words in format json (Example @dariusk [corpora common words of English](https://github.com/dariusk/corpora/blob/master/data/words/common.json) around 900 words)
- Translation in your language using [freedict](https://freedict.org/downloads/) in mode offline
- TTS using [gTTS](https://gtts.readthedocs.io/en/latest/) online or [pyttsx3](https://github.com/nateshmbhat/pyttsx3) in mode offline
- Scraping gif for each word
- Generate desk in only one command

Execution examples:
```
python3 main.py (TYPE DESK) (LANGUAGE TO LEARN) (FREE DICT WITH LANGUAJE TO LEAND -> YOUR MOTHER LANGUAGE) (TITLE) (LIST OF WORDS IN JSON)
```

```
python3 main.py audio_only en fd-eng-spa 'Common English words for Spanish speakers' corpora/data/words/common.json
```

```
python3 main.py audio_images en fd-eng-spa 'Common English words for Spanish speakers' corpora/data/words/common.json
```

## Share desks

If you want to share your desks created with this tool you can do it in the shared repository with a PR (Limit 100MB)

[https://github.com/Tedezed/anki-desk-factory-share](https://github.com/Tedezed/anki-desk-factory-share)

### List

English-Spanish:
- [Common English words for Spanish speakers](https://github.com/Tedezed/anki-desk-factory-share/raw/master/English-Spanish/Common%20English%20words%20for%20Spanish%20speakers.apkg)

## BONUS
- https://github.com/kerrickstaley/genanki
- https://www.reddit.com/r/Anki/comments/9wimp2/genanki_create_anki_decks_with_python/
- https://eshapard.github.io/anki/open-the-anki-database-from-python.html
- https://github.com/dariusk/corpora
