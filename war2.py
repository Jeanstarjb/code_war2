def descending_order(num):
    
    #Converting the numbers to string
    s = str(num)
    
    #setting intergers into a list of strings
    digits = list(s)
    
    #Incorporate the sort attribute for strings
    digits.sort(reverse = True)
    
    #join the sorted strings
    joined_dig = "".join(digits)
    
    #returning  integer values
    return int(joined_dig)

descending_order(43215)
