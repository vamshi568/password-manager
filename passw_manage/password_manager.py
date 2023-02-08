import random
def generate_password():
    charectors=[]
    length_of_passw=int(input('How long the password should be: '))
    for i in range(length_of_passw):
        char_number=random.randint(48,122)
        charectors.append(chr(char_number))
        
        
    random.shuffle(charectors)
    return("".join(charectors))


    
def add():
    account=input('Enter your account name: ')
    psw=input('For generating the random password press (R) or enter the your own password: ')
    if psw=='R' or psw=='r':
        main_pass=generate_password()
    else:
        main_pass=psw
    
    count=0
    doesnt_exist=True
    stored_file=open("password.txt")
    lines=stored_file.readlines()
    for i in lines:
        bla=i.split('|')
        account_name_=bla[0].strip()
        if account_name_==account:
            lines[count]=(account +' | '+main_pass+'\n')
            doesnt_exist=False
            stored_file=open("password.txt",'w')
            for line in lines:
                stored_file.write(line)
            stored_file.close()
            break
        count+=1
    stored_file.close()
    
    if doesnt_exist:
        stored_file=open("password.txt",'a')

        stored_file.write(account +' | '+main_pass+'\n')
        stored_file.close()
    print('Your details are stored')
    
def read():
    f=open("password.txt")

    
    for i in f.readlines():
        data=i.strip()
        account,passw=data.split('|')
        print('Account Name: '+account +'|'+'Password:'+passw)
    f.close()


while True:
    user_input=input('Do you wanna add a password or read a password(View,Add) or press Q to quit(Q):')
    user_value=user_input.lower()
    if user_value=='view':
        read()
    elif user_value=='add':
        add()
    elif user_value=='q':
        break
    else:
        print('Invalid entry')
        continue







