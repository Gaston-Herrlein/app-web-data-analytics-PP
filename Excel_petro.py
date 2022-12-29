import pandas as pd
#import pprint

Control_Panol = "/home/gaston/Documentos/Gaston/Proyectos_Programacion/Excel_Petro/Datos/Control pañol P2.xls"; 
Control_Llegada_Pedidos = "/home/gaston/Documentos/Gaston/Proyectos_Programacion/Excel_Petro/Datos/control llegada de pedidos.xlsx"; 


def ReadData (root, sheet="Hoja1", fil=[4, 1034], col=[1, 11]):
    archivo_excel = pd.read_excel (root, sheet); 
    archivo_excel = archivo_excel.iloc [fil[0]:fil[1], col[0]:col[1]]; #PARA SESGAR LAS FILAS Y COLUMNAS DE INTERES
    return archivo_excel; 


#fil = int (input ("Ingrese el numero de filas: ")); 
#col = int (input ("ingrese el numero de columnas: ")); 

DataBase = ReadData (Control_Panol, "ProductosStock"); 
DataBase = DataBase.rename (columns = {"Dar click en GUARDAR cada vez que se carga un movimiento ": "Codigo", "Unnamed: 2": "Clase", "Unnamed: 3": "Categoria", "Unnamed: 4": "Fabricante","Unnamed: 5": "Nombre","Unnamed: 6": "Descripcion","Unnamed: 7": "Aclaracion","Unnamed: 8": "Valor inicial","Unnamed: 9": "Ingreso","Unnamed: 10": "Salida"}); 
Database = DataBase.astype ({"Codigo": "int32", "Valor inicial": "float64", "Ingreso":"float64", "Salida":"float64"}); 


Salida = ReadData (Control_Panol, "Salidas", [4,513], [1,11]); 
Salida = Salida.drop (["Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7"], axis=1); 
Salida = Salida.rename (columns = {"Dar click en GUARDAR cada vez que se carga un movimiento": "Codigo", "Unnamed: 8": "Fecha", "Unnamed: 9": "Cantidad"}); 
Salida = Salida.astype ({"Codigo": "int32", "Cantidad": "float64"}); 


Entrada = ReadData (Control_Panol, "Entradas",[4,822], [1,11]); 
Entrada = Entrada.drop (["Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7"], axis=1); 
Entrada = Entrada.rename (columns = {"Dar click en GUARDAR cada vez que se carga un movimiento": "Codigo", "Unnamed: 8": "Fecha", "Unnamed: 9": "Cantidad"}); 
Entrada = Entrada.astype ({"Codigo": "int32", "Cantidad": "float64"}); 


Pedidos = ReadData (Control_Llegada_Pedidos, fil=[2,2399], col=[0,13]); 
Pedidos = Pedidos.drop (["seguimiento pedidos", "Unnamed: 3", "Unnamed: 5", "Unnamed: 6", "Aerosol Lubricante Deslizante Antiadherente Silox de Rolls x 220 gr  (Celeste)", "Unnamed: 9", "Unnamed: 11"], axis=1); 
Pedidos = Pedidos.rename (columns = {"Unnamed: 0": "Codigo", "Unnamed: 2": "Fecha Pedido", "Unnamed: 4": "Cantidad", "Unnamed: 8": "Estado", "Unnamed: 10": "¿Recibidos?", "Unnamed: 12": "Demora"}); 
Pedidos = Pedidos.astype ({"Codigo": "int32", "Cantidad": "float64"}); 

#print (DataBase); 
#DataLong = DataBase.shape [1]; 

codigos = Salida.iloc [:513, 0]; 
print (codigos);   
#ESTE FOR SE PODRIA METER EN UNA FUNCION PARA REUTILIZARLO CON EL df DE ENTRADA 
#Para recorrer las columnas
"""
for index in range (Salida.shape [1]):
    #Aca tiene que ir un algoritmo que encuentre los codigos repetidos y agrupe sus posiciones en una lista para operar mas facil sobre ellos
    codigos [index] = Salida.iloc [index, 0]; 
print (codigos); 
"""