import sys
import wikipedia
import time
import os

path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src",  "/corpora/data/")


def fetch(query):
    result_set = wikipedia.search(query)
    for term in range(len(result_set)):
            page = wikipedia.page(result_set[term])
            page_title = page.title
            page_content = page.content
            try:
                name = page_title+"."+"txt"
                file = open(name, 'a')
                file.write(page_content)
                file.close()
            except:
                print("Error Occurred")
                sys.exit(0)

start_time = time.time()
query = input("Enter search terms :")
fetch(query)
end_time = time.time()
print("Total time :", end_time - start_time)








