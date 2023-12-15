import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\n')
        time.sleep(1)
        t-= 1
    print("\n,stop")
countdown(10)

