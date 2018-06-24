price=int(input("enter the price of a donut: Rs. "))
quantity=int(input("enter the no. of donuts: "))
amount=price*quantity

if amount>10000:
    print("give a discount of 10% as amount above Rs.10000 ")
    discount=amount*10/100
    amount=amount-discount
    print("total amount to be paid is Rs.",amount)

elif amount>5000:
    
    print("give discount of 5%")
    discount=amount*5/100
    amount=amount-discount
    print("total amount to be paid is Rs,",amount)
    
elif amount>2000:
      
    print("give discount of 2%")
    discount=amount*2/100
    amount=amount-discount
    print("amount to be paid is Rs.",amount)
    
elif amount>1000:
           
     print("give discount of 1%")
     discount=amount*1/100
     amount=amount-discount
     print("amount to be paid is Rs.",amount)
    
else :
    print("no discount applicable")
    print("amount to be paid is Rs.",amount)
