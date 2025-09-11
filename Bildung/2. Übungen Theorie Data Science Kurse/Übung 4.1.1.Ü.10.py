from faker import Faker

Faker.seed(0)
fake = Faker()

print("Jahr:", fake.year())
print("Monatszahl:", fake.month())
print("Monatsname:", fake.month_name())
print("Wochentag:", fake.day_of_week())
print("Zeitzone:", fake.timezone())