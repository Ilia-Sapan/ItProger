#-------------------------------------------
# Dateiname: Teilprüfung_8.py
# Autor: Ilia Sapan
# Data Science (K4.0026_2.0_VZ)
# Matrikelnummer: 399644000031193700
# Letzte Änderung: 09.04.2025
#-------------------------------------------

import pandas as pd
import random
from faker import Faker

# für Deutschesprache eine Initializierung
fake = Faker('de_DE')


def generate_synthetic_users(n=10):

    users = []
    # Erzeuge eine Liste von n einzigartigen IDs zwischen 0 und 100
    unique_ids = random.sample(range(101), n)

    for i in range(n):
        user_id = unique_ids[i]
        name = fake.name()
        # Erzeugt eine Adresse; ersetze Zeilenumbrüche durch Kommas
        address = fake.address().replace("\n", ", ")
        # Geo-Location als Tupel (latitude, longitude)
        geo = (fake.latitude(), fake.longitude())
        users.append({
            "user_id": user_id,
            "name": name,
            "address": address,
            "geo": geo
        })

    return pd.DataFrame(users)


# Erstelle den DataFrame mit 10 Einträgen
df_users = generate_synthetic_users(10)
print(df_users.to_string())
