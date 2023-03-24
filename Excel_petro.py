import Libreria.ManejoDeDataFrame as mdf


Control_Panol = "/home/gaston/Documentos/Gaston/Proyectos_Programacion/Excel_Petro/Datos/Control pañol P2.xls"; 
Control_Llegada_Pedidos = "/home/gaston/Documentos/Gaston/Proyectos_Programacion/Excel_Petro/Datos/control llegada de pedidos.xlsx";  

#fil = int (input ("Ingrese el numero de filas: ")); 
#col = int (input ("ingrese el numero de columnas: ")); 

DataBase = mdf.ReadData (Control_Panol, "ProductosStock"); 
DataBase = DataBase.rename (columns = {"Dar click en GUARDAR cada vez que se carga un movimiento ": "Codigo", "Unnamed: 2": "Clase", "Unnamed: 3": "Categoria", "Unnamed: 4": "Fabricante","Unnamed: 5": "Nombre","Unnamed: 6": "Descripcion","Unnamed: 7": "Aclaracion","Unnamed: 8": "Valor inicial","Unnamed: 9": "Ingreso","Unnamed: 10": "Salida"}); 
DataBase = DataBase.astype ({"Codigo": "int32", "Valor inicial": "float64", "Ingreso":"float64", "Salida":"float64"}); 


Salida = mdf.ReadData (Control_Panol, "Salidas", [4,513], [1,11]); 
Salida = Salida.drop (["Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7"], axis=1); 
Salida = Salida.rename (columns = {"Dar click en GUARDAR cada vez que se carga un movimiento": "Codigo", "Unnamed: 8": "Fecha", "Unnamed: 9": "Cantidad"}); 
Salida = Salida.astype ({"Codigo": "int32", "Cantidad": "float64"}); 


Entrada = mdf.ReadData (Control_Panol, "Entradas",[4,822], [1,11]); 
Entrada = Entrada.drop (["Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7"], axis=1); 
Entrada = Entrada.rename (columns = {"Dar click en GUARDAR cada vez que se carga un movimiento": "Codigo", "Unnamed: 8": "Fecha", "Unnamed: 9": "Cantidad"}); 
Entrada = Entrada.astype ({"Codigo": "int32", "Cantidad": "float64"}); 


Pedidos = mdf.ReadData (Control_Llegada_Pedidos, fil=[2,2399], col=[0,13]); 
Pedidos = Pedidos.drop (["seguimiento pedidos", "Unnamed: 3", "Unnamed: 5", "Unnamed: 6", "Aerosol Lubricante Deslizante Antiadherente Silox de Rolls x 220 gr  (Celeste)", "Unnamed: 9", "Unnamed: 11"], axis=1); 
Pedidos = Pedidos.rename (columns = {"Unnamed: 0": "Codigo", "Unnamed: 2": "Fecha Pedido", "Unnamed: 4": "Cantidad", "Unnamed: 8": "Estado", "Unnamed: 10": "¿Recibidos?", "Unnamed: 12": "Demora"}); 
Pedidos = Pedidos.astype ({"Codigo": "int32", "Cantidad": "float64"}); 
     

print (mdf.average (Salida)); 


#                   Dataframe Salida pre-ordenamiento
# Index  
#  |
#     | Codigo |       Fecha         | Cantidad  <-- Columns
# 4   |  801   | 2021-10-19 00:00:00 |   2.0
# 5   |  2226  | 2021-10-20 00:00:00 |   3.0
# 6   |  44    | 2021-10-20 00:00:00 |   4.0
# 7   |  1914  | 2021-10-22 00:00:00 |   1.0
# 8   |  799   | 2021-10-23 00:00:00 |   11.0



#                   Dataframe Salida pos-ordenamiento
# Index  
#  |
#  v
#     | Codigo |       Fecha         | Cantidad  <-- Columns
# 143 |   0    | 2022-02-02 00:00:00 |   0.0
# 365 |   0    | 2022-08-16 00:00:00 |   0.0
# 259 |  36    | 2022-05-16 00:00:00 |   2.0
# 267 |  36    | 2022-05-25 00:00:00 |   10.0
# 459 |  36    | 2022-08-23 00:00:00 |   2.0