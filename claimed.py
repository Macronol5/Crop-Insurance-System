def claim():
    global policy_num,r_claim
    policy_num=input("Enter your policy number: ")
    type_crop=str(input("Enter your crop type: "))
    name_crop=str(input("Enter your crop name: "))
    r_claim=str(input("Enter reason for claim"))
    print("your claim is in process: ")