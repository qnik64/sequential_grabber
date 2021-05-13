from urllib.request import urlopen
from urllib.error import URLError


def save_file(filename, content):
    f = open(filename, 'wb')
    f.write(content)
    f.close()


def grab_picture(url, name, directory):
    try:
        url_response = urlopen(url)
        filename = directory + "/" + name
        save_file(filename, url_response.read())
        print("file ", name, " saved.")
    except URLError as e:
        print("An URL error occurred on ", url, " error type: ", e)


pict_name = 'github-mark.png'
grab_picture("https://github.githubassets.com/images/modules/open_graph/" + pict_name, pict_name, "./")
