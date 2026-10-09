# SHO Rizwan - BOSS Bot V4.0 - Crash Proof AI
print("🤖 BOSS BOT V4.0 ONLINE - SHO Rizwan Project")

boss_memory = {
    "hello": "Walaikum Salam SHO Sahab! Hukum?",
    "name": "Me BOSS Bot V4.0 hu, aapka personal AI!",
    "clifton": "Clifton Thana Zindabad! SHO Rizwan Duty pe hai!",
    "chai": "Chai 50 Rs ki, Nashta 300 ka!",
    "salary": "Aapki bachat system me safe hai!"
}

print("BOSS: Salam! Koi bhi sawal pucho (exit likho band karne ke liye)")

while True:
    try:
        user = input("\nAap: ").lower()

        if user == "exit":
            print("BOSS: Allah Hafiz SHO Sahab! 👮‍♂️")
            break

        elif user.startswith("sikh "):
            parts = user.split(" ", 1)
            if len(parts) > 1 and "=" in parts[1]:
                key, val = parts[1].split("=", 1)
                boss_memory[key.strip()] = val.strip()
                print(f"BOSS: Sikh liya! {key.strip()} = {val.strip()}")
            else:
                print("BOSS: Aise sikhao: sikh chai = 50 rupay")

        elif user in boss_memory:
            print(f"BOSS: {boss_memory[user]}")

        else:
            print(f"BOSS: Ye '{user}' mujhe nahi aata. Sikhana hai to 'sikh {user} = jawab' likho!")

    except:
        print("BOSS: Koi masla ho gaya, phir se bolo!")
        continue
