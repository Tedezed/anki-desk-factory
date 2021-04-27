#!/usr/bin/python3
# By Tedezed
import requests, re, shutil, time

def false_image(word):
    src_file = 'resources/error.gif'
    dst_file = 'resources/%s.gif' % (word)
    shutil.copyfile(src_file, dst_file)
    return dst_file

def get_gif(word, file_name_output, image=True):
    if image:
        try:
            f = open(file_name_output)
            f.close()
            print("Image in cache: %s" % (file_name_output))
            return file_name_output
        except IOError:
            r = requests.get('https://giphy.com/search/%s' % (word))
            match = re.search('https?:\/\/[-a-zA-Z0-9@:%._\/+~#=]{1,256}\.gif', r.text)
            try:
                download_file(file_name_output, match.group())
                return file_name_output
            except:
                time.sleep(2)
                return false_image(word)
    else:
        return false_image(word)

def download_file(filename, url_input):
    r = requests.get(url_input, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print("Save image: %s" % (filename))
    else:
        print("Error image: %s" % (filename))

def main():
    get_gif("dog", "test")

if __name__ == "__main__":
    main()