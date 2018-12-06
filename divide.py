dp={}

def divide (str1, str2, m, n):
    result = 0
    if m == 0:
        dp[str1,str2] = n
        return n
    if n == 0:
        dp[str1, str2] = m;
        return m
    if str1[m-1] == str2[n-1]:
        result = divide(str1, str2, m-1, n-1);
        dp[str1, str2] = result;
    else:
        result = 1 + min(divide(str1, str2, m, n-1),
					 divide(str1, str2, m-1, n),
					 divide(str1, str2, m-1, n-1));
        dp[str1, str2] = result;
    return result

def edit_distance(str1,str2,m,n):
    if (str1,str2) in dp:
        return dp[str1,str2]
    else:
        return divide(str1,str2,m,n)
    

# Driver program 
str1 = "potato"
str2 = "petete"
  
print(edit_distance(str1, str2, len(str1), len(str2)) )
print(dp)
print(edit_distance(str1, str2, len(str1), len(str2)) )
# This code is contributed by Bhavya Jain 

