import sys #libreria python para usar argumentos por consola
import timeit #libreria python para poder utilizar el timer

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
        res = edit_distance(str1, str2, len(str1), len(str2))
        
        #Parar timer
        stop = timeit.default_timer()
        
	print("Palabra ["+ str(str1) + "] [" + str(str2) + "] se han realizado " + str(res) + " cambios y tiempo " + str((stop-start)*1000) + "seg")

#print(dp) Imprimir todo el contenedor
# This code is contributed by Bhavya Jain 

