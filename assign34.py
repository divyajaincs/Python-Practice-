def check_baggage(b):
    if b  in range(0,41):
        return True
    else:
        return False
def check_immigration(e):
    if e in range(2001,2025):
        return True 
    else:
        return False
def check_security(noc):
    if noc is True:
        return True
    else:
        return False        
def traveller():
    t_id=1001
    t_name="Jim"
    baggageamount=35
    expiryyear=2019
    nocstatus=True
    check1=check_baggage(baggageamount)
    check2=check_immigration(expiryyear)
    check3=check_security(nocstatus)
    if(check1 is True and check2 is True and check3 is True):
        print("traveler_id=%d"%t_id)
        print("traveler_name=%s"%t_name)
        print("Allow to Traveller fly!")
    else:
        print("traveler_id=%d"%t_id)
        print("traveler_name=%s"%t_name)
        print("Detain Traveller to Re-checking!")    
 
if __name__=="__main__":
    traveller()        