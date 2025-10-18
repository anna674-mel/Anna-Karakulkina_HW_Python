from smartphone import Smartphone
catalog = [
    Smartphone(brand="Sony", model="Ericsson", ph_number="+79123456789"),
    Smartphone(brand="Apple", model="SE", ph_number="+79987654321"),
    Smartphone(brand="Xiaomi", model="Poco", ph_number="+79012345678"),
    Smartphone(brand="Samsung", model="Galaxy", ph_number="+79087654321"),
    Smartphone(brand="LG", model="AP", ph_number="+79001234567")
]

for smartphone in catalog:
    print(f"{smartphone.brand}, {smartphone.model}, {smartphone.ph_number}")
