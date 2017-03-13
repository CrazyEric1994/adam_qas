import sys
import wikipedia
import time
import os

path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src",  "/corpora/data/")
sub = ['Cricket', 'Tennis']


def create():
    for i in range(len(sub)):
        print("creating new  file")
        # name = input("enter the name of file:")
        page = wikipedia.page(sub[i])
        obj = page.content
        try:
            name = sub[i]+"."+"txt"
            file = open(name, 'a')
            file.write(obj)
            file.close()
        except:
            print("error Occurred")
            sys.exit(0)
start_time = time.time()
create()
end_time = time.time()
print(end_time - start_time)