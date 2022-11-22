import qrcode
import hashlib

# Hash
hash = hashlib.md5()
hash.update(b"https://woolly-honesty-57c.notion.site/E-Garay-d3b54df238a9431694d41f5f2c0a5b79")

img = qrcode.make('https://woolly-honesty-57c.notion.site/E-Garay-d3b54df238a9431694d41f5f2c0a5b79')
type(img)
img.save(f"{hash.hexdigest()}.png")
print("Printed succesfully!")


print(f"{hash.name}: {hash.hexdigest()}")