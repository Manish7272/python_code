user_name= "manish"
user_pass= "1212"

for i in range(5):
    if i<4:
        if user_name == input("enter user name : \t"):
            
            # user name is right than check the password
            for j in range(5):
                
        #j<4........................................................
                if j<4:
                    if user_pass == input("Enter Your Password : \t"):
                        print("log in successfull")
                    
                        break
                    else:
                        print(f"Wrong Password, \n you have {4-j} attempts left \n")
            
             # this below break is important
             # break
            
        #j==4 .....................................................
                else:
        
                    print("ALERT !!! THIS IS LAST CHANCE otherwise Your Account will be ' BLOCKED ' ")
            
                    # user name is right than check the password
                    for j in range(5):
                
                        if user_pass == input("Enter Your Password : "):
                            print("log in successfull")
                            break
                            
                        else:
                            print("wrong user Password, your Account is BLOCKED ")
                            break
                    break
            break
  
        else:
            print(f" Wrong user name, \n you have {4-i} attempts left \n")
            
    #  i==4   for user name >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   

    else:
        print("ALERT !!! THIS IS LAST CHANCE otherwise Your Account will be ' BLOCKED ' \n")

        if user_name == input("enter user name : \t"):
            
            # user name is right than check the password
            for j in range(5):
                
        #j<4........................................................
                if j<4:
                    if user_pass == input("Enter Your Password : "):
                        print("log in successfull")
                    
                        break
                    else:
                        print(f" Wrong Password, \n you have {4-j} attempts left \n")
            
             # this below break is important
             # break
            
        #j==4 .....................................................
                else:
        
                    print("ALERT !!! THIS IS LAST CHANCE otherwise Your Account will be ' BLOCKED ' ")
            
                    # user name is right than check the password
                    for j in range(5):
                
                        if user_pass == input("Enter Your Password : "):
                            print("log in successfull")
                            break
                            
                        else:
                            # print(f"Wrong Password, \n you have {4-j} attempts left \n")
                            print("wrong user Password, your Account is BLOCKED ")


                            break
                    break
               
            break
  
        else:
        
            print("wrong user name, your Account is BLOCKED ")
          
        
    