from address import Address
from mailing import Mailing


address_to = Address("101000", "Москва", "Ленина", "15", "42")
address_from = Address("630000", "Новосибирск", "Советская", "10", "5")


my_mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=500.50,
    track="RU123456789"
)


print(f"Отправление {my_mailing.track} из "
f"{my_mailing.from_address.index}, {my_mailing.from_address.city}, "
f"{my_mailing.from_address.street}, {my_mailing.from_address.house} - {my_mailing.from_address.apartment} "
f"в {my_mailing.to_address.index}, {my_mailing.to_address.city}, "
f"{my_mailing.to_address.street}, {my_mailing.to_address.house} - {my_mailing.to_address.apartment}. "
f"Стоимость {my_mailing.cost} рублей."
)
