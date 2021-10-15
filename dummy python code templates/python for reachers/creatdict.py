text="I am Joy. I am a student of computer science. I love compuer science."
text=text.lower()
skip=[".",","]
word_dict={}
for i in text:
    if(i in skip):
        text=text.replace(i,"")
for word in text.split(" "):
    if(word in word_dict):
        word_dict[word]+=1
    else:
        word_dict[word]=1
print(word_dict)
