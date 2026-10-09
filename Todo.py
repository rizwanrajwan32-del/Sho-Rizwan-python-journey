# SHO Rizwan - Level 12 - TO-DO List App (Interview Wala)
print("📋 SHO Rizwan - Duty Task Manager")

tasks = []

# Pehle purani list load karo agar hai to
try:
    with open("duty.txt", "r") as f:
        tasks = f.read().splitlines()
    print(f"Purani Duty List Load Hui: {len(tasks)} tasks")
except:
    print("Nayi Duty List Start!")

while True:
    print("\n--- MENU ---")
    print("1. Duty Dekho")
    print("2. Nayi Duty Add Karo")
    print("3. Duty Complete (Delete)")
    print("4. Exit")

    choice = input("Choice (1-4): ")

    if choice == "1":
        if len(tasks) == 0:
            print("Koi Duty Nahi Hai - Chai Peelo! ☕")
        else:
            print("\n📋 Aapki Duty List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Nayi Duty Likho: ")
        tasks.append(new_task)
        # File me save karo - Taake band karne pe delete na ho
        with open("duty.txt", "w") as f:
            for t in tasks:
                f.write(t + "\n")
        print(f"✅ Add Ho Gaya: {new_task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("List Khali Hai!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                num = int(input("Kaunsi Duty Complete Hui? Number likho: "))
                removed = tasks.pop(num-1)
                with open("duty.txt", "w") as f:
                    for t in tasks:
                        f.write(t + "\n")
                print(f"🗑️ Complete: {removed}")
            except:
                print("Ghalat Number!")

    elif choice == "4":
        print("Allah Hafiz SHO Sahab! Duty List Save Hai! 👮‍♂️")
        break

    else:
        print("1 se 4 tak likho!")
