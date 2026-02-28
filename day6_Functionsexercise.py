# EXERCISE FINAL DAY 6
# Challenge: Combining Functions

# Create a function called `analyze_list` that:
# Receives a list
# Returns a dictionary with:
# "total" → number of elements
# "even" → number of even numbers
# "mayor" → largest number

def analyze_list (list1):
     if not list1:
        return {"total": 0, "even": 0, "mayor": None}
    
     total = len(list1)
    
     count1 = 0
     for n in list1:
        if n % 2 == 0:
            count1 += 1
     even = count1
     mayor = max(list1)
    
     return {"total": total, "even": even, "mayor": mayor}
   
print(analyze_list([3, 8, 2, 10, 5]))
    