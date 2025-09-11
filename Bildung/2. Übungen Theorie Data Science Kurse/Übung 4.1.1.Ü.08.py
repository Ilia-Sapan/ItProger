from faker import Faker

fake = Faker()
names = [fake.unique.name() for i in range(10)]

for i in range(1,len(names)):
    print(names[i])