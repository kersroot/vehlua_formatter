# Araç isimlerinin bulunduğu dosya
input_file = "kers.lua"

# vehicles.lua dosyasını açıyoruz (yazmak için)
with open("vehicles.lua", "w") as lua_file:
    # Kers.lua dosyasını okuyoruz
    with open(input_file, "r") as file:
        for line in file:
            vehicle_name = line.strip()  # Araç ismini alıyoruz
            # Formatı oluşturup vehicles.lua dosyasına yazıyoruz
            lua_file.write(f"{{\n")
            lua_file.write(f"    model = '{vehicle_name}',\n")
            lua_file.write(f"    name = '{vehicle_name}',\n")
            lua_file.write(f"    brand = 'aracmarkasi',\n")
            lua_file.write(f"    price = 999999999999999,\n")
            lua_file.write(f"    category = 'donatearaclar',\n")
            lua_file.write(f"    type = 'automobile',\n")
            lua_file.write(f"    shop = 'pdm',\n")
            lua_file.write(f"}},\n")

print("Araç kodları başarıyla vehicles.lua dosyasına yazıldı.") 
print("The vehicle codes have been successfully written to vehicles.lua.")