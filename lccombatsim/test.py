print("hi")

import random

class stats:
    def __init__(self, id_name, id_level, health, attack_level, defense_level, min_speed, max_speed, max_hp, current_hp, current_sp=0):
        self.name = id_name
        self.level = id_level
        self.health = health
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.max_hp = max_hp
        self.current_hp = int(current_hp)
        self.current_sp = int(current_sp)
        if self.current_sp >= 45:
            self.current_sp = 45
        elif self.current_sp <= -45:
            self.current_sp = -45

class skill_stats_n_combat:
    def __init__(self, skill_name, base_power, coin_power, coin_count):
        self.name = skill_name
        self.base_power = base_power
        self.coin_power = coin_power
        self.coin_count = coin_count

    def roll(self, stats_obj):
        power = self.base_power
        for i in range(self.coin_count):
            if random.randint(0, 100) <= 50+stats_obj.current_sp:
                power += self.coin_power
        return power
    
    def clash(self, stats_obj1, stats_obj2):
        clash_count = 0
        print(f"new clash: {stats_obj1.name} HP: {stats_obj1.current_hp}, {stats_obj2.name} HP: {stats_obj2.current_hp}")
        while self.coin_count > 0:
            clash_count += 1
            power1 = self.roll(stats_obj1)
            power2 = self.roll(stats_obj2)
            print(f"{stats_obj1.name} rolls {power1}")
            print(f"{stats_obj2.name} rolls {power2}")
            if power1 > power2:
                self.coin_count -= 1
                print(f"{stats_obj1.name} wins this round's clash, coins left: {self.coin_count}")
            elif power2 > power1:
                print(f"{stats_obj2.name} wins this round's clash")
                
            else:
                print("tie, rerolling")
        if skill_stats_n_combat.coin_count <= 0:




skill1 = skill_stats_n_combat("Skill1", 10, 5, 3)
skill2 = skill_stats_n_combat("Skill2", 12, 4, 2)
unit1 = stats("Unit1", 1, 100, 10, 8, 5, 10, 100, 100)
unit2 = stats("Unit2", 1, 100, 9, 7, 4, 9, 100, 100)

while unit1.current_hp > 0 and unit2.current_hp > 0:
    skill1.clash(unit1, unit2)
    skill2.clash(unit2, unit1)