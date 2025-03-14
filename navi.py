from datetime import  datetime

name=input("Enter your name:")
lists='''
Rice  Rs 20/kg
Sugar Rs 50/kg
Salt Rs 40/kg
Oil  Rs 100/kg
Paneer Rs 120/kg
Maggi  Rs 90/kg
Boost Rs 70/kg
'''
print(lists)
price=0
pricelist=[]
totalprice=0
FinaFinallprice=0
ilist=[]
qlist=[]
plist=[]

items={
    'rice':20,
    'sugar':50,
    'salt':40,
    'oil':100,
    'paneer':120,
    'maggi':90,
    'boost':70
}
option=int(input("for list of items press 1:"))
if option ==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity= int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("oops your enter item is not available")
    else:
        print("you enter wrong number")
    inp=input("can i bill this items yes or no:")
    if inp=='yes':
        pass
    if finalamount!=0:
        print(25*" ","Navitha Supermarket",25*"=")
        print(28*" ","Mancherial")
        print("Name:",name,30*" ","Date:",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
        for i in range(len(pricelist)):
            print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'FinalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for Visiting")
            print(75*"-")

