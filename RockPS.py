import random;
import os;

os.system('cls');
userpoint=0;
syspoint=0;

#first to 5 point wins
while(syspoint<5 and userpoint<5):
    values=["rock","paper","scissors"];

    print("Choose your weapon no \n1.Rock\n2.Paper\n3.Scissors\n");
    uservalue=int(input());
    if(uservalue<0 or uservalue>2):
        print("Sorry the weapon you entered will be added in future\n")
        continue;

    uservalue-=1;#value index starts from 0
    sysvalue=random.randint(0,2);
    print("user weapon= "+values[uservalue]);
    print("systems weapon= "+values[sysvalue]);

    #comparing values of system and user: 3 cases1
    #case 1: both value equal
    #case 2 : System wins
    #case 3 : user wins 
    if(uservalue==sysvalue):
        print("Same pitch! Tie");
        print("user point=",userpoint);
        print("system points=",syspoint,"\n");  
    elif((sysvalue==0 and uservalue==2) or (sysvalue==1 and uservalue==0) or (sysvalue==2 and uservalue==1)):
        syspoint+=1;
        print("system gained points\n");
        print("user point=",userpoint);
        print("system points=",syspoint,"\n");     
    else:
        userpoint+=1;
        print("user gained points\n");
        print("user point=",userpoint);
        print("system points=",syspoint,"\n");  

if(userpoint==5):
    print("Hooray, You won");
else:
    print("Sorry, System won");
   
