with open('sample.txt', mode ='a') as myfile:
    myfile.write("\nThis is the fourth line")
    
with open('sample.txt', mode ='r') as myfile:
    print(myfile.read())
    

with open('sample2.0.txt', mode ='w') as myfile:
    myfile.write('I just made a NEW FILE lol')