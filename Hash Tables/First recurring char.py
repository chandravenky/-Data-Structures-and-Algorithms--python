

def first_recurring_char(input_array):
    
    
    wip_hash={}
    for item in input_array:
        
        if item in wip_hash:
            
            return item
        
        wip_hash[item] = 1
    
    return None


#first_recurring_char([2,5,1,2,3,5,1,2,4])


#first_recurring_char([2,1,1,2,3,5,1,2,4])
#first_recurring_char([2,3,4,5])

