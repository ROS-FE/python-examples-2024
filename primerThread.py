from threading import Thread
import time


def thrF(parameter):
    for i in range(10):
        print(f"{parameter} Thread: {i}")
        time.sleep(1)



def main():
    thr = Thread(target=thrF, args=(33, ), daemon=True)
    thr.start()
    time.sleep(3)
    print("Glavna F")
    thr.join()

if __name__=="__main__":
    main()