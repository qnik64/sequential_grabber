from urllib.request import urlopen
from urllib.error import HTTPError, URLError


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
        return True
    except HTTPError as e:
        if 404 == e.code:
            print("file ", name, " not found.")
            return False
        print("An HTTP error occurred on ", url, " error type: ", e)
        return False
    except URLError as e:
        print("An URL error occurred on ", url, " error type: ", e)
        return False


def sequence(start, stop, url_common_part):
    successes = 0
    for i in range(start, stop):
        pict_name = str(i) + ".jpg"
        if grab_picture(url_common_part + pict_name, pict_name, "./data"):
            successes += 1
    print(successes, " files saved ", stop - start - successes, " files skipped")



