import pandas as pd
#import pprint

#Funcion para leer el df de una planilla de excel
def ReadData (root, sheet="Hoja1", fil=[4, 1034], col=[1, 11]):
    archivo_excel = pd.read_excel (root, sheet); 
    archivo_excel = archivo_excel.iloc [fil[0]:fil[1], col[0]:col[1]]; #PARA SESGAR LAS FILAS Y COLUMNAS DE INTERES
    return archivo_excel; 


#Funcion para arreglar el df leido
#           df, [" "], [" "],  [" "], [""],   bool,            ["type"]  
def Rename (df, name, rename, value, asTo, remove=False, indexRemove=[""]):
    dataFrame=df;  
    
    for i in range (len(rename)): 
        dataFrame = dataFrame.rename (columns = {name[i]: rename[i]}); 
        
    for i in range (len(value)):
        dataFrame = dataFrame.astype ({value[i]: asTo[i]}); 
    
    if remove==True: 
        dataFrame = dataFrame.drop (indexRemove, axis=1); 
    
    return dataFrame; 


#Funcion para generar un df con el nombre del codigo y la diferencia de dias en pedidos
def Average(df):
    dataFrame = df; 
    #Para recorrer las columnas
    codigos = []; 
    aux = [];  
    fechas = []; 
    cont=0; #variable para recorrer la lista fecha
    dataFrame = dataFrame.sort_values (["Codigo","Fecha"]);  #Ordenamos la lista para trabajar

    #Para recorrer todo el dataframe --> "df.shape [0]"
    for index in range (dataFrame.shape [0]): 
        if index!=0:    #AGREGAR UN CONDICIONAL MAS PARA QUE FILTRE LOS 0 (ERRORES)
            if dataFrame.iloc [index, 0]==dataFrame.iloc [(index-1), 0]:
                aux.append (dataFrame.iloc [index, 1]-dataFrame.iloc [index-1, 1]); 
            else:
                codigos.append (dataFrame.iloc [index, 0]); 
                fechas.append([]);  
                for j in range (len(aux)): 
                    fechas[cont].append(aux[j]); 
                cont+=1;  
                aux.clear(); 
        else:
            codigos.append (dataFrame.iloc [index, 0]); 
    
        if (index+1) == dataFrame.shape [0]: #Cuando llegue a la ultima iteracion
            fechas.append([]); 
            for j in range (len(aux)): 
                fechas[cont+1].append(aux[j]); 
            fechaSalida = pd.DataFrame(fechas, index= codigos); 
    return fechaSalida; 


