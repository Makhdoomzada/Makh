 


# 
# * `linear_search(l, item, issorted=False)` -- where `l` is a list of numeric values, `item` is a numeric value to search for in the list, and `issorted` is `True` if list is sorted from least to greatest. The function returns the *index* into the list corresponding to value of `item` and `None` if the value is not present in the list. The *linear search* (Sec 13.1) method is to be used for searching for the value. 
# * `binary_search(l, item, issorted=False)` -- where `l` is a list of numeric values, `item` is a numeric value to search for in the list, and `issorted` is `True` if list sorted from least to greatest. The function returns the *index* into the list corresponding to value of `item` and `None` if the value is not present in the list. The *binary search* (Sec 13.2) method is to be used for searching for the value.
# 
# where each function returns the `None` value if invalid input arguments were provided. You may *only* use the following methods of the `list` class: `list.copy()` and `list.sort()`. 

# In[ ]:


def binary_search(l, item, issorted=False):
    if (issorted==True):
        x = 0 
        i = len(l) - 1
        while (l[(x + i) // 2] <= (len(l)-1)):
            if l[(x + i) // 2] == item:
                break
            elif (l[(x + i) // 2] > item):
                j = j + 1
            elif(l[(x + i) // 2] < item):
                x = x + 1
        else:
            for i in range(len(l)):
                 if (l[i] == item):
                    return i
    return(None)

        
def linear_search(l, item, issorted=False):
    for i in range(len(l)):
        if item==l[i]:
            return(i)    
    return (None)
    

