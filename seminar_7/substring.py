def naive_substring(string, substring):
    sub = len(substring)
    st  = len(string)
    answer = [i for i in range(st - sub)  if string[i:i+sub-1] == substring]
    return answer


def naive_zfunc(string):
    n = len(string)
    z = [0] * n
    for i in range(1, n - 1):
        while i + z[i] < n and string[z[i]] == string[i + z[i]]:
            z[i] += 1
    return z

def advanced_zfunc(string):
    n = len(string)                                                                                                                 
    z = [0] * n                                                                                                                     

    left, right, z[0] = 0, 0, n                                                                                                  
    for i in range(1, n):          
        if i < right:                                                                                          
            k = i - left
            if z[k] < right - i:   
                z[i] = z[k]                                                                                  
                continue            
            left = i                                                                                       
        else: left = right = i
        
        while right < n and string[right - left] == string[right]:                                                             
            right += 1 
        z[i] = right - left                                                                                                      
    return z



def prefix_func(string):
    n = len(string)
    p_values = [0] * n
    for i in range(1, n):
        j = p_values[i-1]
        while j>0 and string[i] != string[j]:
            j = p_values[j-1]
        p_values[i] = j + string[i] == string[j]
    return p_values
            




        
