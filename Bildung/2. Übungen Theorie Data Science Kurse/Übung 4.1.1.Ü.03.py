from faker import Faker

fake = Faker()

latitude = fake.latitude()
longitude = fake.longitude()

print(latitude, longitude)