import hashlib
_max = 16**7

part = _max//100

_hash = "0d589b50de0c394cd1f8decd329687a5e4e3d8727895088b228f65693d119cbb"


import sys


begg = 0x5ae7656

if len(sys.argv)>1:
    begg = int(sys.argv[1])*part


userId = "d854fa46-e500-4889-b6ff-2b6c67891254".encode()

import gc # garbage collector

for i in range(begg,_max):

    bruteOption = hex(i)[2:].rjust(7,"0")
    #print(bruteOption)
    
    curr = c.replace(b"___USER_ID___",userId).replace(b"___REPORT_ID___",bruteOption.encode())

    
    currhash = hashlib.sha256(curr).hexdigest()
    if currhash == _hash:
        print("found:", bruteOption, i, currhash)
        exit()
    
    if i%part == 0:
        print(int(i//part),"%")
    if i%(part*5) == 0:
        gc.collect() # garbage collector
