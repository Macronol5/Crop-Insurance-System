def verify(c,policy_no,r_claim,s):
    if policy_no ==c:
        if r_claim=="drought":
            return 0.75*s
        elif r_claim=="storm":
            return 0.6*s
        elif r_claim=="flood":
            return 0.7*s 
        elif r_claim=="natural fire":
            return 0.9*s
        elif r_claim=="hailstorm":
            return 0.85*s
        else:
            print("reason not supported")
    else:
        print("policy no. not found")
        
#v=verify(987,987,"rought",23000)     
#print(v)