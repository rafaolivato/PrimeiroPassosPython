def éPrimo(k): 
    divisor = 2 
    primo = True 
    teste = k 
 
    if k == 1:
        primo = False
    
    elif k == 2:
        primo = True
        
    else: 
        if k > 2:
            while k > divisor and primo: 
                teste = k%divisor 
                divisor = divisor + 1 
                if teste == 0: 
                    primo = False 
                     
                    
            else: 
                if primo == True: 
                    
                    return primo
 
 
def maior_primo(k):
    x = k
    while not éPrimo(x):
        x = x - 1
    return x
