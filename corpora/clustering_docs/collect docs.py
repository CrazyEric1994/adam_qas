import sys
import wikipedia
import time

def create():
    print("creating new  file")
    name = input("enter the name of file:")
    page = wikipedia.page(name)
    obj = page.content
    try:
        name = name+"."+"txt"
        file = open(name,'a')
        file.write(obj)
        file.close()
    except:
        print("error occured")
        sys.exit(0)
start_time = time.time()
create()
end_time = time.time()
print(end_time - start_time)