
stri=input("Enter string")
state=0
for i in stri:
    if state==0:
        if i=="a":
            state=0
        elif i=="b":
            state=1
            
            
            
    elif state==1:
        if i=="a":
            state=2
        elif i=="b":
            state=1
    elif state==2:
        if i=="a":
            state=0
        elif i=="b":
            state=3
    elif state==3:
        if i=="a" or i=="b":
            state=3
        
    
            
if state==3:
    print("Given String is accepted")
else:
    print("Give string is rejected")
    
