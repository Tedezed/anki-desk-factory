#!/bin/bash
sudo apt-get install dict dictd dict-freedict-eng-spa dict-freedict-spa-eng espeak -y
pip3 install gTTS==2.2.2 nltk==3.6.1 genanki==0.10.1 pyttsx3==2.90 --user
python3 -c "import nltk; nltk.download('wordnet')"
curl -SL https://download.freedict.org/dictionaries/eng-spa/0.3.1/freedict-eng-spa-0.3.1.dictd.tar.xz -o ~/freedict-eng-spa-0.3.1.dictd.tar.xz
cd ~/ && tar -xf ~/freedict-eng-spa-0.3.1.dictd.tar.xz
sudo cp /usr/share/dictd/freedict-eng-spa.dict.dz /usr/share/dictd/freedict-eng-spa.dict.dz_old
sudo mv ~/eng-spa/eng-spa.dict.dz /usr/share/dictd/freedict-eng-spa.dict.dz
sudo systemctl restart dictd
rm -rf ~/eng-spa
dict -D