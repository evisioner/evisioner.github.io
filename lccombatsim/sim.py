import random

class skills:
    def __init__(self, name, base_power, coin_power, coin_count):
        self.name = name
        self.base_power = base_power
        self.coin_power = coin_power
        self.coin_count = coin_count
        self.original_coin_count = coin_count

    def roll(self):
        power = self.base_power
        for i in range(self.coin_count):
            if random.randint(0, 1) == 1:
                power += self.coin_power
        return power

class SkillPage:
    def __init__(self, skills_list):
        self.skills_list = skills_list[:]  # current page
        self.original_skills = skills_list[:]  # for refresh

    def pick_skill(self):
        if not self.skills_list:
            self.refresh()
        skill = random.choice(self.skills_list)
        self.skills_list.remove(skill)
        return skill

    def refresh(self):
        self.skills_list = self.original_skills[:]
        print("Skill page refreshed!")

class ids:
    def __init__(self, name, skill_page, hp=100):
        self.name = name
        self.skill_page = skill_page
        self.hp = hp

class ini_combat:
    @staticmethod
    def clash(sinner1, sinner2):
        while sinner1.hp > 0 and sinner2.hp > 0:
            # Pick random skill from each page
            skill1 = sinner1.skill_page.pick_skill()
            skill2 = sinner2.skill_page.pick_skill()
            skill1.coin_count = skill1.original_coin_count
            skill2.coin_count = skill2.original_coin_count
            clash_count = 0

            print(f"\nNew clash! {sinner1.name} HP: {sinner1.hp}, {sinner2.name} HP: {sinner2.hp}")
            print(f"{sinner1.name} uses {skill1.name}")
            print(f"{sinner2.name} uses {skill2.name}")

            # Clash loop
            while skill1.coin_count > 0 and skill2.coin_count > 0:
                power1 = skill1.roll()
                print(sinner1.name + " rolls " + str(power1))
                power2 = skill2.roll()
                print(sinner2.name + " rolls " + str(power2))
                clash_count += 1
                if power1 > power2:
                    print(sinner1.name + " wins the round!")
                    skill2.coin_count -= 1
                    print(skill2.name + " loses a coin. Coins left: " + str(skill2.coin_count))
                elif power2 > power1:
                    print(sinner2.name + " wins the round!")
                    skill1.coin_count -= 1
                    print(skill1.name + " loses a coin. Coins left: " + str(skill1.coin_count))
                else:
                    print("Tie! No coins lost.")

            # Clash ends, determine victor and deal damage
            if skill1.coin_count > 0:
                victor = sinner1
                victor_skill = skill1
                loser = sinner2
            else:
                victor = sinner2
                victor_skill = skill2
                loser = sinner1

            print(victor.name + " wins the clash!")
            damage = 0
            current_power = victor_skill.base_power
            print(f"Damage phase: {victor.name} flips {victor_skill.coin_count} coins!")
            for i in range(victor_skill.coin_count):
                flip = random.randint(0, 1)
                if flip == 1:
                    current_power += victor_skill.coin_power
                    print(f"Coin {i+1}: heads! Power increases to {current_power}.")
                else:
                    print(f"Coin {i+1}: tails. Power remains {current_power}.")
                damage += current_power
            print(f"Total damage dealt: {damage} (includes all coin flips)")
            damage += clash_count
            print(f"Clash count: {clash_count} (extra damage: {clash_count})")
            print(loser.name + " takes " + str(damage) + " damage!")
            loser.hp -= damage
            if loser.hp <= 0:
                print(loser.name + " has been mutilated.")
                break
            else:
                print(loser.name + " has " + str(loser.hp) + " HP left.")

# Input section for skill pages
def input_skill(skill_label):
    name = input(f"Enter name for {skill_label}: ")
    base_power = int(input(f"Enter base power for {skill_label}: "))
    coin_power = int(input(f"Enter coin power for {skill_label}: "))
    coin_count = int(input(f"Enter coin count for {skill_label}: "))
    return skills(name, base_power, coin_power, coin_count)

def input_skill_page(sinner_label):
    print(f"\nEnter info for {sinner_label}:")
    name = input("Name: ")
    print("Skill 1 (will be added 3 times):")
    skill1 = input_skill("Skill 1")
    print("Skill 2 (will be added 2 times):")
    skill2 = input_skill("Skill 2")
    print("Skill 3 (will be added 1 time):")
    skill3 = input_skill("Skill 3")
    hp = int(input("HP: "))
    skills_list = [skill1]*3 + [skill2]*2 + [skill3]
    skill_page = SkillPage(skills_list)
    return ids(name, skill_page, hp)

sinner1_obj = input_skill_page("first sinner")
sinner2_obj = input_skill_page("second sinner")

ini_combat.clash(sinner1_obj, sinner2_obj)
