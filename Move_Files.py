import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/ADMIN/Downloads"
to_dir = "C:/WhiteHatJr/"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Mueve Todos los Archivos de Imágenes de la Carpeta de Descargas a Otra Carpeta
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx']:

        path1 = from_dir + '/' + file_name                       # Ejemplo path1 : Downloads/ImagenNombre1.jpg        
        path2 = to_dir + '/' + "Document_Files"                     # Ejemplo path2 : D:/My Files/Imagen_Archivos      
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name   # Ejemplo path3 : D:/My Files/Imagen_Archivos/ImagenNombre1.jpg
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Checa si la ruta de Carpeta/Directorio existe antes de mover
        # Else haz una NUEVA Carpeta/Directorio y después mueve
        
        if os.path.exists(path2):
          print("Moviendo " + file_name + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moviendo " + file_name + ".....")
          shutil.move(path1, path3)

        
