dp={}
def divide (str1, str2, m, n):
    if (str1 and str2) in dp:
        print("Ya estaba calculado")
        return dp[str1, str2]

    else:
        result = 0
        if m == 0:
            dp[str1,str2] = n
            return n

        if n == 0:
            dp[str1, str2] = m;
            return m

        if str1[m-1] == str2[n-1]:
            result = divide(str1, str2, m-1, n-1)
            print("Calculado1")
            return result
        else:
            result = 1 + min(divide(str1, str2, m, n-1),
                         divide(str1, str2, m-1, n),
                         divide(str1, str2, m-1, n-1));
            print("Calculado2")
            return result
    
     #   dp[str1, str2] = result
      #  print("Calculado")

       # return dp[str1, str2]

# Driver program 
str1 = "constante"
str2 = "pedante"
  
print(divide(str1, str2, len(str1), len(str2)) )
# This code is contributed by Bhavya Jain 

