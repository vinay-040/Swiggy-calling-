def exorder():
    exorder=int(input("enter extra order"))
    qnt=int(input("enter how many plates"))
    if(exorder>7):
        print("enter VALID menu number to order!!!")
    else:
        for i in range(qnt):
            list1.append(menu1[exorder][0])
            list2.append(menu1[exorder][1])
        print("your order is added to cart!!!")


menu1={
        1:["dosa",69],
        2:["idly",49],
        3:["pizza",199],
        4:["burger",99],
        5:["chicken",89],
        6:["biryani",249],
        7:["icecream",59]
    }
print("\n WELCOME TO HOTEL \n WE ARE THANKFULL TO CHOOSE OUR HOTEL")
print("___________________________________________________________________________________________________________")
print("HERE IS THE MENU:\n \t\t\t",menu1)
print("___________________________________________________________________________________________________________")
list1=[]
list2=[]
order=int(input("enter number in menu"))
quantity=int(input("enter how many plates"))
if order<=7:
    for i in range(quantity):
        list1.append((menu1[order][0]))
        list2.append((menu1[order][1]))
    print("your order is added to cart!!!")
    while(1<2):
        extraorders = input("want more say yes or no")
        if (extraorders == "yes"):
            exorder()
        else:
            break
else:
    print("enter VALID menu number")
count={}
dupli=[]
for i in list1:
    if i not in count:
        count[i]=1
        dupli.append(i)
    else:
        count[i]+=1
n=0
print("___________________________________________________________________________________________________________")
print("YOUR ORDER IS")
for i in dupli:
    print(count[i],"plates of ",dupli[n])
    n+=1
print("___________________________________________________________________________________________________________")
def bill():
    bill=0
    for i in range(len(list1)):
        bill+=list2[i]
    Delv=(bill*10)/100
    GST=(bill*9)/100
    print(f"Total bill       :{bill} $$")
    print(f"Delivery charges :{Delv} $$")
    print(f"GST              :{GST} $$")
    print(f"Grand total      :{bill+Delv} $$")
    print("\nThankyou for your order \n You will get your order soon!!!! \n \t \t 'VISIT AGAIN' ")
bill()
