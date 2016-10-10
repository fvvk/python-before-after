print("which file should be read?")

with open(input("> ")) as f:
    mylist = [line.rstrip('\n') for line in f]

string= "".join(mylist)

words=string.split()

print("which words context shall i check?")

def context(word):
    for ind,x in enumerate(words):
       if x.strip(",'.!")==word or x.strip(',".!')==word:
           with open('output.txt', 'a') as f:
               print(" ".join(words[ind-8:ind]+words[ind:ind+9]), file=f)

context(input("> "))
