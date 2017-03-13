import os
import re

path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src",  "/corpora/clustering_docs/a1.txt")

pattern = '([[])\w+]'
with open(path, 'r') as f:
    lines = f.read()


def remove_Citations():
    for line in lines:
        match = re.search(pattern, line)
        if match:
            new_line = match.group() + '\n'
    removed_citations = re.sub(pattern, '', lines)
    return removed_citations

print(remove_Citations())