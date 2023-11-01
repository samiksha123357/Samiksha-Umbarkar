items={1:"samosa",2:"tea",3:"poha",4:"kachori",5:"idali",6:"vadapav"}
price={1:20,2:12,3:25,4:30,5:30,6:20}
it=[]
qu=[]
print("-"*85)
print("\t\t\t\tTaj Hotel")
print("-"*85)

while True:
    print("""              Menu Card
        1.samosa      4.kachori
        2.tea         5.idali
        3.poha        6.vadapav""")
    print("-"*85)

 
    i=eval(input("enter number from menu card:"))
    q=eval(input("Enter Quantity:"))
    it.append(i)
    qu.append(q)
    ch=input("do you want to continue ").lower()
    if ch== "n":
        print("-"*85)
        print("|{:^10}|{:^10}|{:^10}|{:^10}|".format("NAME","QUANTITY","PRICE","AMOUNT"))
        print("-"*85)
        sum=0
        for i in range(len(it)):
            print("|{:^10}|{:^10}|{:^10}|{:^10}|".format(items[it[i]],qu[i],price[it[i]],qu[i]*price[it[i]]))
            print("-"*85)
            sum=sum+qu[i]*price[it[i]]
        print("your total amount is" ,sum, "rs") 
        break



    
    