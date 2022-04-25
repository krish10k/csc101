exp1="a+b"
exp2="x=t1"
dict={"+":"ADD","SUB":"-","*":"MULT","/":"DIV","=":"MOV"}
operator=["+","-","/","*"]
temp=[]
r=0
for i in range(len(exp1)):
    if str(exp1[i]) not in operator:
        register="R"+str(r)
        temp.append(register)
        print(f"MOV : {register} , {exp1[i]}")
        r+=1
for i in range(len(exp1)):    
    if str(exp1[i]) in operator:
        for o,(p,q) in enumerate(dict.items()):
            if exp1[i]==p:
                print(f"{q} : {temp[0]},{temp[1]} ")
print(f"MOV : {exp2[0]} ,R0")
