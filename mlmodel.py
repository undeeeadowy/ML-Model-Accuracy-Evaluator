predictions  = ["Sales Lead", "Support Request", "Sales Lead", "Support Request"]
true_labels  = ["Sales Lead", "Support Request", "Support Request", "Support Request"]

def calculate_accuracy(predictions, true_labels):
    if len(predictions) == 0 or len(true_labels) == 0:
        print("Ошибка: списки не должны быть пустыми!")
        return None
    
    if len(predictions) != len(true_labels):
        print("Ошибка: длины списков не совпадают!")
        return None
    
    correct = 0
    for pred, true in zip(predictions, true_labels):
        if pred == true:
            correct += 1
    return correct / len(true_labels)
accuracy = calculate_accuracy(predictions, true_labels)
if accuracy is not None:
    print(f"Model Accuracy: {accuracy:.2f}")



print("=== Тест 1: 100% точность ===")
pred1 = ["Sales Lead", "Support Request", "Sales Lead"]
true1 = ["Sales Lead", "Support Request", "Sales Lead"]
acc1 = calculate_accuracy(pred1, true1)
if acc1 is not None:
    print(f"Model Accuracy: {acc1:.2f}\n")

print("=== Тест 2: 0% точность ===")
pred2 = ["Sales Lead", "Sales Lead", "Sales Lead"]
true2 = ["Support Request", "Support Request", "Support Request"]
acc2 = calculate_accuracy(pred2, true2)
if acc2 is not None:
    print(f"Model Accuracy: {acc2:.2f}\n")


print("=== Тест 3: 75% точность ===")
pred3 = ["Sales Lead", "Support Request", "Sales Lead", "Support Request"]
true3 = ["Sales Lead", "Support Request", "Support Request", "Support Request"]
acc3 = calculate_accuracy(pred3, true3)
if acc3 is not None:
    print(f"Model Accuracy: {acc3:.2f}\n")


print("=== Тест 4: Пустые списки ===")
pred4 = []
true4 = []
acc4 = calculate_accuracy(pred4, true4)
if acc4 is not None:
    print(f"Model Accuracy: {acc4:.2f}\n")

print("=== Тест 5: Несовпадающие длины ===")
pred5 = ["Sales Lead", "Support Request"]
true5 = ["Sales Lead"]
acc5 = calculate_accuracy(pred5, true5)
if acc5 is not None:
    print(f"Model Accuracy: {acc5:.2f}\n")

