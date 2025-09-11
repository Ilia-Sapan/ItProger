from faker import Faker

fake = Faker()

# Пример: женский профиль
profile = fake.profile(sex='F')
print(profile)

# Пример: мужской профиль
profile = fake.profile(sex='M')
print(profile)
