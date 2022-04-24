
stri=input("Enter string")
state=0
for i in stri:
    if state==0:
        if i=="a":
            state=1
        elif i=="b":
            state=0
            
            
            
    elif state==1:
        if i=="a":
            state=1
        elif i=="b":
            state=2
    elif state==2:
        if i=="a":
            state=1
        elif i=="b":
            state=0
            
if state==2:
    print("Given String is accepted")
else:
    print("Give string is rejected")
    
