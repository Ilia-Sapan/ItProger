import torch
from torch.utils.data import DataLoader, random_split

# Допустим, у тебя есть dataset
# dataset = CustomDataset()  # Подставь свой датасет сюда

# Пример для объяснения (вместо CustomDataset ты подставишь свой)
# dataset = torch.utils.data.TensorDataset(torch.randn(100, 10), torch.randint(0, 2, (100,)))

# 1. Разделяем данные на train и test
train_size = int(0.8 * len(dataset))  # 80% для обучения
test_size = len(dataset) - train_size  # оставшиеся 20% для теста

train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

# 2. Создаём DataLoader для каждой части
train_loader = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=32, shuffle=True)

# 3. (Необязательно) — Проверяем, как выглядят данные в DataLoader
for data in train_loader:
    print(data)
    break  # Просто для проверки первой пачки данных
