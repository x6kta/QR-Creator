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
    file_size_readable = humanize.naturalsize(file_size) 
    return file_size_readable

# Devolver que todo ha sido exitoso
def success(text, file_name):
    size_file = get_size_file(file_name)
    print("QR code has been generated succesfully!") 
    print(f"* File created: {file_name}.png\n* Based on: {text}\n* Size: {size_file}")

def main():
    # Nombre del archivo
    try:
        text = input("Type the URL or plain text that you'll convert into a QR Code:\n> ")
        need_file_name = input("Do you want a custom name to your QR code?\n(Type 'Y' for Yes, another key to not add a custom name.)\n> ")
        if need_file_name == "Y" or need_file_name == "y":
            # Nombre del archivo
            file_name = input("Ingrese el nombre del archivo que será convertido en un código QR:\n> ")
            generate_QR_code(text, file_name)

            # Se ha generado el QR
            os.system("clear")
            success(text, file_name)
        else:
            os.system("clear")
            hash = hashlib.md5(text.encode()).hexdigest()
            print(hash)
            generate_QR_code(text, hash)

            os.system("clear")
            success(text, hash)       
    except KeyboardInterrupt:
        os.system("clear")
        print("Program finished succesfully by an KeyboardInterruption. (Ctrl + C hass been pressed)")
        exit()

if __name__ == "__main__":
    main()