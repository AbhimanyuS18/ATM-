# atm project 
amount = 2000
print("WELCOME TO THE SBI ATM".center(100,"*"))
print("1 = check balance\n".center(100," "),"2 = deposit cash\n ","3 = tranfer cash\n ".center(100," ")," 4 = widhrow cash")
rupees = input("what do you want")
pin = input("please! enter the PIN")
if pin == "1234":
    if rupees == "1":
        print("Welcome to the ATM deshboard")
        print("your total balance is", amount)
        # cash deposit code start here 
    elif rupees == "2":
        print("please! enter the cash which you want to deposit")
        print(" 100 ke note =\n","200 ke note =\n","500 ke note =\n","2000 ke note =")
        _500 = int(input())
        _200 = int(input())
        _100 = int(input())
        _2000 = int(input())
        add = _500*500+_200*200+_100*100+_2000*2000
        print("ok! your cash deposit are sucessfully")
        checkamount = input("do you want to check your balance after the cash deposit yes / NO ")
        if checkamount.lower() == "yes":
            print("your total amount is", amount + add)
        # cash transfer code start here 
    elif rupees == "3":
        print("do tou want to transfer the cash yes / NO")
        rupees2 = input()
        if rupees2 == "yes":
            print("please! enter the account number")
            rupees3 = int(input())
            if rupees3 >=10 :
                print("enter the cash")
                rupees4 = int(input())
                print("your transcation is sucessfully")
                print("do you want to check balance after the transation  Yes / No ")
                rupees5 = input()
                if rupees5.lower() == "yes":
                    print("total balance = ", amount-rupees4)
            else:
                print("please! enter the valid account number")
   
        # cash widhrow code start here     
    elif rupees == "4":
               
        print("enter the amount")
        rupees7 = int(input())
        print("please! choose the note")
        print("1 = 500")
        print("2 = 200")
        print("3 = 100")
        print("4 = 2000")
                   
        note =input()
        
        cheelar = rupees7%10                 
        if note == "1" :
                        a = rupees7//500
                        b=rupees7-(a*500)
                        c=b//100
                        if cheelar == 0:
                            
                            print("500 ke note is = " ,a, "\n100 ke note = " ,c,"\nAnd total amount is =",rupees7)
                            print("widhrow sucessfully")
                        
                        elif cheelar != 0:
                            print("500 ke note is = " ,a, "\n100 ke note = " ,c,"\n")
                            print("but! cheelar is not available in ATM, so sorry,you don't get your cheelar \nAnd total amount   = ", rupees7)
                            print("widhrow sucessfully")
        elif note == "2":
                        a = rupees7//200
                        b = rupees7-(a*200)
                        c = b//100
                        if cheelar == 0:
                            print("200 ke note is = " ,a, "\n100 ke note = " ,c,"\nAnd your amount is=",rupees7)
                            print("widhrow sucessfully")
                        elif cheelar == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                            print("200 ke note is = " ,a, "\n100 ke note = " ,c)
                            print("but! cheelar is not available in ATM, so sorry,you don't get your cheelar \nAnd total amount   = ", rupees7)
                            print("widhrow sucessfully")
                        
        elif note == "3":
                        a = rupees7//100
                        if cheelar == 0:
                            print("100 ke note = " ,a,"\n And total amount =",rupees7)
                            print("widhrow sucessfully")
                        elif cheelar == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                            print("100 ke note = " ,a,"\n")
                            print("but! cheelar is not available in ATM, so sorry,you don't get your cheelar \nAnd total amount   = ", rupees7)
                            print("widhrow sucessfully")
        elif note == "4":
                        a = rupees7//2000
                       
                        b = rupees7-(a*2000)
                        
                        c = (b//100)
                        d=rupees7-(b+(c*100))
                        num = "1234567890"
                        if cheelar == 0:
                            print("2000 ke note is = " ,a, "\n100 ke note = " ,c,"\nAnd your amount is=",rupees7)
                            print("widhrow sucessfully")
                        elif cheelar !=0:
                            
                            print("2000 ke note is = " ,a, "\n100 ke note = " ,c,"\nAnd your amount is=",rupees7)
                            print("but! cheelar is not available in ATM, so sorry,you don't get your cheelar \nAnd total amount   = ", rupees7)

                            print("widhrow sucessfully")
                        # if cheelar == 0:
                        #     print("2000 ke note is = " ,a, "\n100 ke note = " ,c)
                        #     print("widhrow sucessfully")
                        # elif cheelar == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                        #     print("2000 ke note is = " ,a, "\n100 ke note = " ,c)
                        #     print("but! cheelar is not available in ATM, so sorry,you don't get your cheelar \nAnd total amount   = ", rupees7)
                        #     print("widhrow sucessfully")
                        # else:
                            #     print("2000 ke note is = " ,a, "\n100 ke note = " ,c)
                        #     print("widhrow sucessfully")
                        # elif cheelar == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                        #     print("2000 ke note is = " ,a, "\n100 ke note = " ,c)
                        #     print("but! cheelar is not available in ATM, so sorry,you don't get your cheelar \nAnd total amount   = ", rupees7)
                        #     print("widhrow sucessfully")
                            # print("sorry, The amount is less than 2000")
        else:
                        print("please! enter the right option")        
else:
    print("please! enter the valid PIN")
