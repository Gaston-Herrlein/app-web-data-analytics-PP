import pandas as pd
#import pprint

#Funcion para leer el df de una planilla de excel
def ReadData (root, sheet="Hoja1", fil=[4, 1034], col=[1, 11]):
    archivo_excel = pd.read_excel (root, sheet); 
    archivo_excel = archivo_excel.iloc [fil[0]:fil[1], col[0]:col[1]]; #PARA SESGAR LAS FILAS Y COLUMNAS DE INTERES
    return archivo_excel; 


#Funcion para generar un df con el nombre del codigo y la diferencia de dias en pedidos
def average(df):
    #Para recorrer las columnas
    codigos = []; 
    aux = [];  
    fechas = []; 
    cont=0; #variable para recorrer la lista fecha

    df = df.sort_values (["Codigo","Fecha"]);  #Ordenamos la lista para trabajar

    #Operamos sobre las fechas con el tipo de dato DataTime 
    #Para recorrer todo el dataframe --> "df.shape [0]"
    for index in range (df.shape [0]): 
        if index!=0:    #AGREGAR UN CONDICIONAL MAS PARA QUE FILTRE LOS 0 (ERRORES)
            if df.iloc [index, 0]==df.iloc [(index-1), 0]:
                aux.append (df.iloc [index, 1]-df.iloc [index-1, 1]); 
            else:
                codigos.append (df.iloc [index, 0]); 
                fechas.append([]);  
                for j in range (len(aux)): 
                    fechas[cont].append(aux[j]); 
                cont+=1;  
                aux.clear(); 
        else:
            codigos.append (df.iloc [index, 0]); 
    
        if (index+1) == df.shape [0]: #Cuando llegue a la ultima iteracion
            fechas.append([]); 
            for j in range (len(aux)): 
                fechas[cont+1].append(aux[j]); 
            fechaSalida = pd.DataFrame(fechas, index= codigos); 
    return fechaSalida; 

