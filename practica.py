import files 


cargar = files.upload()

for archivo in cargar.keys():
    print(f"Se cargaron los archivos: {archivo}")