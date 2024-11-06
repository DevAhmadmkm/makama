import datetime
user1=input(f"welcome user\nplease enter name: ")
welcomemsg=int(input(f"welcome to ahmad library\nselect 1 to proceed: "))
if welcomemsg == 1:
    sign_in=datetime.datetime.now().date()
    print(f"welcome user you signed in: ",sign_in.strftime("%h\%m\%d\%y"),"enter to continue")
    sex=input("male or female: ")
    phonenumber=input("please enter phone number: ")
    print("WELCOME") 
else:
    print("invalid user ID")
    

def Books():
        index=int(input(f"welcome please choose your desired course\n1.science  2.commercial "))
        if index==1:
             print("please choose your sub section")
        elif index==2:
             print("please choose your sub section")
        else:
             print("invalid selection")
       
        
             
        index=int(input(f"select sub science sections:\n1.sub_section_A1 2. sub_section_A2\n3. sub_section_A3  4. sub_section_A4"))
        if index==1:
            print(f"welcome\nyou have selected the science section for 100 level: ")
            science=(input('please select the name of the book you want to read: '))
            if science is True:
                print("https://www.wikipidea.com") 
            else:
                print("book selected successful")
       
        
        elif index==2:
            print("you have selected the science section for 100 level")
            science=(input('please select the name of the book you want to read: '))
            if science is True:
                print("https://www.wikipidea.com")
            else:
                print("book selected successful")

        elif index==3:
                 print("you have selected the science section for 100 level")
                 science=(input('please select the name of the book you want to read: '))
                 if science is True:
                     print("https://www.wikipidea.com")
                 else:
                    print("book selected successful")
            
        elif index==4:
              print("you have selected the science section for 100 level")
              science=(input('please select the name of the book you want to read: '))
              if science is True:
                     print("https://www.wikipidea.com")
              else:
                    print("book selected successful")
        else:
            print("invalid selection")
        
    

        indexB=int(input(f"select sub commercial sections:\n1.sub_section_A1 2. sub_section_A2\n3. sub_section_A3  4. sub_section_A4"))
        if indexB==1:
            print(f"welcome\nyou have selected the comeercial section for 100 level: ")
            commercial=(input('please select the name of the book you want to read: '))
            if commercial is True:
                print("https://www.wikipidea.com")
            else:
                print("book selected successful")

        elif indexB==2:
            print(f"welcome\nyou have selected the comeercial section for 100 level: ")
            commercial=(input('please select the name of the book you want to read: '))
            if commercial is True:
                print("https://www.wikipidea.com")
            else:
                print("book selected successful")

        elif indexB==3:
            print(f"welcome\nyou have selected the comeercial section for 100 level: ")
            commercial=(input('please select the name of the book you want to read: '))
            if commercial is True:
                print("https://www.wikipidea.com")
            else:
                print("book selected successful")

        elif indexB==4:
            print(f"welcome\nyou have selected the comeercial section for 100 level: ")
            commercial=(input('please select the name of the book you want to read: '))
            if commercial is True:
                print("https://www.wikipidea.com")
            else:
                print("book selected successful")
        else:
             print("invalid selection")

def sign_out():
    user1=input(f"please enter name: ")
    sign_out=int(input(f"sign_out from ahmad library\nselect 1 to proceed: "))
    if sign_out == 1:
        sign_out=datetime.datetime.now().date()
        print(f"user you signed out: ",sign_out.strftime("%h\%m\%d\%y"),"enter to continue")
    if sign_out is True:
         sign_out()
    else:
         print("see you later")
    
         

            


Books()
sign_out()
