from random import choice

user = input("Введіть stone, scissor або paper: ")
computer = choice(["stone", "scissor", "paper"])

results = {
    ("stone", "scissor"): "Ти переміг!",
    ("scissor", "paper"): "Ти переміг!",
    ("paper", "stone"): "Ти переміг!"
}

print("Комп'ютер вибрав:", computer)
win = {
    user == computer: "Нічия!",
    (user, computer) in results: "Ти переміг!"
}

print(win.get(True, "Комп'ютер переміг!"))