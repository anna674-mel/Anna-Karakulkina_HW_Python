from address import Address
from mailing import Mailing

to_address = Address("123456", "Пермь", "Ленина", 102, 5)
from_address = Address("654321", "Киров", "Пионерская", 12, 7)

mailing = Mailing(to_address, from_address, "1000", "TRK654321")
print(
    f"Отправление {mailing.track} из {mailing.from_address.index},"
    f"{mailing.from_address.city}, {mailing.from_address.street},"
    f"{mailing.from_address.house} - "
    f"{mailing.to_address.flat} в {mailing.to_address.index},"
    f"{mailing.to_address.city}, {mailing.to_address.street},"
    f"{mailing.to_address.house} - {mailing.to_address.flat}."
    f"Стоимость {mailing.cost} рублей."
    )
