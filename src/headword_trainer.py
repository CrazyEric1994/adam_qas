import os

path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src", "/corpora/")
fp = open(path+"train_5500.label.txt", "r")
fp_train = open(path+"train_5500_headword.txt", "w")

for record in fp:
    training_data = record.split(" ", 1)
    if training_data[1].startswith("What"):
        print(training_data)
        fp_train.write(training_data[0]+" "+training_data[1])
fp_train.close()