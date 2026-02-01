import random

def galactic_scavenger():
    # 1. Game Setup
    ship_hull = 100
    credits = 0
    cargo = []
    locations = {
        "1": {"name": "Alpha Belt", "danger": 10, "loot": ["Iron", "Copper"]},
        "2": {"name": "Nebula Core", "danger": 30, "loot": ["Silver", "Gold"]},
        "3": {"name": "The Void", "danger": 60, "loot": ["Void Crystal", "Antimatter"]}
    }

    print("--- 🚀 Galactic Scavenger 🚀 ---")
    print("Mine resources to earn 1,000 credits before your hull hits 0%!")

    # 2. Game Loop
    while ship_hull > 0 and credits < 1000:
        print(f"\nHull: {ship_hull}% | Credits: {credits} | Cargo: {cargo}")
        print("Locations:")
        for key, loc in locations.items():
            print(f"[{key}] {loc['name']} (Danger: {loc['danger']}%)")
        
        choice = input("\nWhere to mine? (or [S]ell cargo): ").strip().upper()

        if choice == 'S':
            # Selling Logic
            if not cargo:
                print("❌ Cargo bay is empty!")
                continue
            
            earnings = 0
            for item in cargo:
                if "Iron" in item: earnings += 20
                elif "Gold" in item: earnings += 100
                elif "Void" in item: earnings += 300
                else: earnings += 50 # Default for others
            
            credits += earnings
            print(f"💰 Sold cargo for {earnings} credits!")
            cargo = []
            continue

        if choice in locations:
            loc = locations[choice]
            print(f"🛰️ Scanning {loc['name']}...")
            
            # 3. Risk/Reward Logic
            # Check for damage based on danger level
            if random.randint(1, 100) <= loc['danger']:
                damage = random.randint(15, 30)
                ship_hull -= damage
                print(f"💥 Collision! Your hull took {damage}% damage!")
            else:
                found = random.choice(loc['loot'])
                cargo.append(found)
                print(f"💎 Success! You extracted {found}.")
        else:
            print("❌ Invalid navigation coordinates.")

    # 4. End State
    if credits >= 1000:
        print(f"\n🏆 VICTORY! You retired a wealthy scavenger with {credits} credits!")
    else:
        print("\n💀 DISASTER! Your ship broke apart in deep space. Game Over.")

galactic_scavenger()
