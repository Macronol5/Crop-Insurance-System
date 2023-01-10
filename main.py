from farmer import *
from premium import *
from farmer import typ_crop,name_crop,ld_amount,policy_no
from claimed import policy_num,r_claim
from verification import *
from claimed import *


farmers()

#typp_crop=farmer.typ_crop()
#amount=farmer.ld_amount()
p=premiumm(typ_crop,name_crop,ld_amount)
if (p == -1):
    print(name_crop, "is not supported" )
else:   
     print("you have to pay premium: Rs",p)
     sum_insured=p*11.6
     print("your sum insured is: Rs. ",sum_insured)
c=policy_no

claim()

#c=policy_no
s=sum_insured
v=verify(policy_no,policy_num,r_claim,s)
print("amount you will get is Rs.",v)
    
    

