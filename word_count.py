with open ("file") as file:
    wordcount={}
    for word in file.read().split():
        wordcount[word] = wordcount.get(word,0) + 1

    for k,v in wordcount.items():
        print k, v