import Libreria.ManejoDeDataFrame as mdf

Control_Panol = "/home/gaston/Documentos/Gaston/Proyectos_Programacion/Excel_Petro/Datos/Control pañol P2.xls"; 
Control_Llegada_Pedidos = "/home/gaston/Documentos/Gaston/Proyectos_Programacion/Excel_Petro/Datos/control llegada de pedidos.xlsx";  

def main ():
    DataBase = mdf.ReadData (Control_Panol, "ProductosStock"); 
    DataBase = mdf.Rename (DataBase,["Dar click en GUARDAR cada vez que se carga un movimiento ", "Unnamed: 2", "Unnamed: 3", "Unnamed: 4","Unnamed: 5","Unnamed: 6","Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10"], ["Codigo", "Clase", "Categoria", "Fabricante", "Nombre", "Descripcion", "Aclaracion", "Valor inicial", "Ingreso", "Salida"], ["Codigo", "Valor inicial", "Ingreso", "Salida"], ["int32", "float64", "float64", "float64"]); 

    Salida = mdf.ReadData (Control_Panol, "Salidas", [4,513], [1,11]); 
    Salida = mdf.Rename (Salida, ["Dar click en GUARDAR cada vez que se carga un movimiento", "Unnamed: 8", "Unnamed: 9"], ["Codigo", "Fecha", "Cantidad"], ["Codigo", "Cantidad"], ["int32", "float64"], True, ["Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7"]); 

    Entrada = mdf.ReadData (Control_Panol, "Entradas",[4,822], [1,11]); 
    Entrada = mdf.Rename (Entrada, ["Dar click en GUARDAR cada vez que se carga un movimiento", "Unnamed: 8", "Unnamed: 9"], ["Codigo", "Fecha", "Cantidad"], ["Codigo", "Cantidad"], ["int32", "float64"], True, ["Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7"]);  

    Pedidos = mdf.ReadData (Control_Llegada_Pedidos, fil=[2,2399], col=[0,13]); 
    Pedidos = mdf.Rename (Pedidos, ["Unnamed: 0", "Unnamed: 2", "Unnamed: 4", "Unnamed: 8", "Unnamed: 10", "Unnamed: 12"], ["Codigo", "Fecha Pedido", "Cantidad", "Estado", "¿Recibidos?", "Demora"], ["Codigo", "Cantidad"], ["int32", "float64"], True, ["seguimiento pedidos", "Unnamed: 3", "Unnamed: 5", "Unnamed: 6", "Aerosol Lubricante Deslizante Antiadherente Silox de Rolls x 220 gr  (Celeste)", "Unnamed: 9", "Unnamed: 11"]);  

    #print (mdf.Average (Salida)); 

if __name__=='__main__':
    main(); 