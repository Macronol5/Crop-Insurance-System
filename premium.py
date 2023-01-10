from farmer import farmers

def premiumm(type_crop,name_crop,l_amount):
    if(type_crop=="rabi"):
     print(2*l_amount)
     if(name_crop=="wheat"):
        return 500*l_amount
     elif(name_crop=="barley"):
        return 400*l_amount
     elif(name_crop=="mustard"):
        return 420*l_amount
     elif(name_crop=="green pea"):
        return 470*l_amount
     else:
        return -1
    if(type_crop=="kharif"):
     print(2*l_amount)
     if(name_crop=="rice"):
         return 200*l_amount
     elif(name_crop=="soya bean"):
         return 255*l_amount
     elif(name_crop=="cotton"):
         return 600*l_amount
     elif(name_crop=="sugar cane"):
         return 250*l_amount
     else:
         return -1