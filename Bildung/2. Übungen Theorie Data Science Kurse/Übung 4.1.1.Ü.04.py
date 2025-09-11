# from faker import Faker
#
# fake = Faker("de_De")
# person = fake.simple_profile()
#
# print(person)

from faker import Faker

fake = Faker()

# Генерация имени и фамилии
first_name = fake.first_name()
last_name = fake.last_name()

# Генерация профессии
job = fake.job()

# Генерация геолокации
latitude = fake.latitude()
longitude = fake.longitude()

print(f"Имя: {first_name}, Фамилия: {last_name}, Профессия: {job}")
print(f"Координаты: {latitude}, {longitude}")