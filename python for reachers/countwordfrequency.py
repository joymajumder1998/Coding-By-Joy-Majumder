from collections import Counter

text="I am joy Maumder. I am a student of computer science. Computer Science is my favourite subject. I love computer science."
text=text.lower()
skips=[".",","]
for char in text:
    if(char in skips):
        text=text.replace(char,"")
word_count=Counter(text.split(" "))
print(word_count)
