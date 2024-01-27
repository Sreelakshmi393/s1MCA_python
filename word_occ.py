str = "I am a Python programmer I am a Java programmer am am am am"

word = "am"

words = str.split()
count=0
for i in words:
    if(word == i):
        count=count+1
    
print(count)
