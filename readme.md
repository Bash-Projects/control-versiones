# Copia de seguridad automática
Este script está configurado para escuchar una carpeta y hacer una copia de seguridad automática de cualquier archivo cuando se realiza una modificación en el sistema de archivos. Permitir que el Control de versiones simple se mantenga en archivos en un sistema de archivos local / sistema de archivos de red.

Los archivos se renombraron correctamente con el siguiente formato:
```
[timestamp]_[original_filename].[extension] 
```
Ejemplo:
 10-12-2019 22.50.00_mattncott.docx 

## Dependencias requeridas
Instale lo siguiente a través de pip antes de usar la aplicación

```
pip3 install Watchgod
```

