from faker import Faker

Faker.seed(0)
fake = Faker()

for _ in range(10):
    print(fake.unique.currency_symbol())