name=input("enter the name")
if name=="mamta":
    print(name,"is correct")
    place=input("enter the place")
    if place=="rajsthan":
        print(place,"is correct")
        age=input("enter the age")
        if age=="17":
            print(age,"is correct") 
            graduation=input("enter the graduation")
            if graduation=="graduate":
                print(graduation,"is correct")
                hobby=input("enter the hobby")
                if hobby=="reading":
                    print(hobby,"is correct")
                    mother=input("enter the mother name")
                    if mother=="radha":
                        print(mother,"is correct")
                        father=input("enter the father name")
                        if father=="veerbhan":
                            print(father,"is correct")
                        else:
                            print("name is not correct")
                    else:
                        print("name is not correct")
                else:
                    print("no")
            else:
                print("no")
        else:
            print("no")
    else:
        print("place is not correct")
else:
    print("name is wrong")