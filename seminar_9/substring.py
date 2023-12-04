def advanced_zfunc(string):
    n = len(string)                                                                                                                 
    z = [0] * n                                                                                                                     

    left, right, z[0] = 0, 0, n                                                                                                  
    for i in range(1, n):          
        z[i] = max(0, min(z[i-left], right-i+1))                                                                                    
        
        while i + z[i] < n and string[i+z[i]] == string[z[i]]:                                                             
            z[i] += 1 
        right = z[i] + i - 1
        left = i
    return z



def prefix_func(string):
    n = len(string)
    p_values = [0] * n
    for i in range(1, n):
        j = p_values[i-1]
        while j>0 and string[i] != string[j]:
            j = p_values[j-1]
        p_values[i] = j + (string[i] == string[j])
    return p_values
            




        
