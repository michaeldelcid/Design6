#Displays current time every 10 seconds

import time
while True:
    try:
        nowtime = time.time()
        print(time.asctime(time.localtime(nowtime)))
        time.sleep(10)
    except KeyboardInterrupt:
        exit()
