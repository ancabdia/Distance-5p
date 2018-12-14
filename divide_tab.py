import sys #libreria python para usar argumentos por consola
import timeit #libreria python para poder utilizar el timer

# A Dynamic Programming based Python program for edit 
# distance problem 
def editDistDP(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
  
            # If first string is empty, only option is to 
            # isnert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n]
	
#1- Leemos el fichero de datos
file = open(sys.argv[1], "r") #abrir fichero en modo lectura
palabras = [] #array para guardar las palabras
while(1):
	linea = file.readline().strip() # palabra1;palabra2
	if not linea:
		break
	palabra = linea.split(";")
	palabras.append(palabra)

for i in palabras: #Mostrar palabras y resultado
    #Inicializar timer
    start = timeit.default_timer()
	
    str1 = i[0]
    str2 = i[1]
    res = editDistDP(str1, str2, len(str1), len(str2))
        
	#Parar timer
    stop = timeit.default_timer()
        
    print("Palabra ["+ str(str1) + "] [" + str(str2) + "] se han realizado " + str(res) + " cambios y tiempo " + str((stop-start)*1000) + "seg")

#print(dp) Imprimir todo el contenedor
# This code is contributed by Bhavya Jain 


