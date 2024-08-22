import phonenumbers
from phoneNumber import numeber

from phonenumbers import geocoder
ch_number = phonenumbers.parse(numeber,"CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(numeber,"RO")
print(carrier.name_for_number(service_number,"en"))