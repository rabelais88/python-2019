person = {
  "name": "jerry",
  "age": 24
}

target = "name"
print(f"person's name is {person[target]}")

for i in person.items():
  print(f"{i[0]}----{i[1]}")

print(person)