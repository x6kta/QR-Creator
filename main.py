import qrcode
import hashlib
import humanize
import os

# Genera el código QR
def generate_QR_code(text, file_name):
    img = qrcode.make(f"{text}")
    type(img)
    img.save(f"{file_name}.png")

# Obtiene el tamaño del archivo generado
def get_size_file(file_name):
    file_size = os.stat(f"{file_name}.png").st_size
    file_size_kB = humanize.naturalsize(file_size)
    return file_size_kB

# Nombre del archivo
text = input("Ingrese el URL o texto que desea convertir a QR\n> ")
need_file_name = input("¿Quiere agregar un nombre personalizado a su archivo? (Ingrese Y para sí, cualquier tecla para no)\n> ")

try:
    if need_file_name == "y" or need_file_name == "Y":
        # Nombre del archivo
        file_name = input("Ingrese el nombre del archivo que será convertido en un código QR:\n> ")
        generate_QR_code(text, file_name)
        
        # Se ha generado el QR
        os.system("clear")
        print("QR code has been generated succesfully!") 
        print(f"* File created: {file_name}.png\n* Based on: {text}\n* Size: {get_size_file(file_name)}")
    else:
        os.system("clear")
        print("Cannot hash yet!")

except KeyboardInterrupt:
    os.system("clear")
    print("Interrupted by user")
    exit()


# Hash
# hash = hashlib.md5()
# hash.update(b"https://woolly-honesty-57c.notion.site/E-Garay-d3b54df238a9431694d41f5f2c0a5b79")



# Imagen con el nombre del hash
#img.save(f"{hash.hexdigest()}.png")


# Test
# print(f"{hash.name}: {hash.hexdigest()}")