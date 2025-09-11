#-------------------------------------------
# Dateiname: Teilprüfung_7.py
# Autor: Ilia Sapan
# Data Science (K4.0026_2.0_VZ)
# Matrikelnummer: 399644000031193700
# Letzte Änderung: 09.04.2025
#-------------------------------------------

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset


# Definition einer einfachen Feedforward-Netzwerk-Klasse,
# bei der die Aktivierungsfunktion als Parameter übergeben wird.
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes, activation):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.activation = activation  # hier wird z. B. nn.Sigmoid(), nn.LeakyReLU(), etc. eingesetzt.
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        x = self.fc1(x)
        x = self.activation(x)
        x = self.fc2(x)
        return x


# Trainingsfunktion, die das Modell über eine vorgegebene Anzahl von Epochen trainiert.
def train_model(model, train_loader, criterion, optimizer, num_epochs=20):
    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0
        correct = 0
        total = 0
        for inputs, targets in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * inputs.size(0)

            # Berechne die Klassifikation (bei CrossEntropyLoss: argmax entlang der Klassen-Dimension)
            _, predicted = torch.max(outputs, 1)
            total += targets.size(0)
            correct += (predicted == targets).sum().item()
        epoch_loss = running_loss / total
        epoch_acc = correct / total
        print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {epoch_loss:.4f}, Accuracy: {epoch_acc:.4f}")
    return epoch_loss, epoch_acc


#Vorbereitung eines synthetischen Datensets
# Wir erzeugen einen binären Klassifikationsdatensatz:
input_size = 10
hidden_size = 16
num_classes = 2
N = 1000
batch_size = 32

torch.manual_seed(0)  # für Reproduzierbarkeit
X = torch.randn(N, input_size)
# Klassenzuordnung: Summe der Features > 0  => Klasse 1, sonst 0
y = (torch.sum(X, axis=1) > 0).long()

dataset = TensorDataset(X, y)
train_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Definition der zu testenden Aktivierungsfunktionen

# Wir legen alle Varianten in einem Dictionary ab.
activations = {}

# 1. Sigmoid-Aktivierung:
activations['Sigmoid'] = nn.Sigmoid()

# 2. LeakyReLU für verschiedene negative_slope-Parameter:
for negative_slope in [0.01, 0.05, 0.1, 0.5]:
    activations[f'LeakyReLU({negative_slope})'] = nn.LeakyReLU(negative_slope=negative_slope)

# 3. PReLU:
activations['PReLU'] = nn.PReLU()

# 4. ELU für verschiedene Alpha-Parameter:
for alpha in [0.1, 0.2, 0.3]:
    activations[f'ELU({alpha})'] = nn.ELU(alpha=alpha)

# Dictionary, in dem wir die Ergebnisse (Loss, Accuracy) für die einzelnen Aktivierungen speichern.
results = {}

# Training und Evaluation für jede Aktivierungsfunktion
num_epochs = 20  # Anzahl der Trainingsdurchläufe; kann je nach Experiment variiert werden.

for act_name, act_func in activations.items():
    print(f"\nTraining mit Aktivierungsfunktion: {act_name}")
    # Instanziiere das Modell neu, um für jede Variante einen frischen Zustand zu haben:
    model = SimpleNN(input_size=input_size, hidden_size=hidden_size, num_classes=num_classes, activation=act_func)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    final_loss, final_acc = train_model(model, train_loader, criterion, optimizer, num_epochs=num_epochs)
    results[act_name] = {'loss': final_loss, 'accuracy': final_acc}

# Ausgabe der Endperformances:
print("\nFinale Performance:")
for act, metrics in results.items():
    print(f"{act}: Loss = {metrics['loss']:.4f}, Accuracy = {metrics['accuracy']:.4f}")
