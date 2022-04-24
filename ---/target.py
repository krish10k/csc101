symbol = {'0':'203','1':'204','2':'202','3':'205','4':'7'
}

literal = {'0':'208','1':'209'
}



intermediate_code = [
        [("AD",'00'),("C",'200')],
        [("IS",'04'),("RG",'01'),("S",'0')],
        [("IS",'04'),("RG",'02'),('S','1')],
        [("S",'2'),("RG",'01'),("L",'0')]
]
a=[]
b=[]

for i in intermediate_code:
    print()
    for t in i:
        
        if(t[0]=='S'):
            a.append(symbol.get(t[1]))
            # print(a)
            li = " ".join([str(elem) for elem in a])
            print(li,end=" ")
            a.pop(0)
        elif (t[0] == "L"):
            b.append(literal.get(t[1]))
            # print(a)
            li_1 = " ".join([str(elem) for elem in b])
            print(li_1,end=" ")
            b.pop(0)
        else:
            print(f"{t[1]} ",end=" ")
