import random

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.mp = mp
        self.maxmp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = [Bcolors.FAIL + "attack" + Bcolors.ENDC, Bcolors.OKBLUE + "magic" + Bcolors.ENDC]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("actions")
        for item in self.actions:
            print("    ", str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1

        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "    MAGIC:" + Bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def get_hp(self):
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def enemy_get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4
        mp_bar = ""
        mpbar_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks >= 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += "░"

        while mpbar_ticks >= 0:
            mp_bar += "█"
            mpbar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += "░"

        space1 = ""
        space2 = ""
        x = len(str(self.hp))
        while x < 5:
            space1 += " "
            x += 1

        while len(str(self.mp)) < 3:
            space2 += " "

        print("                         ________________________________________               _________________")
        print(self.name + "         " + space1 + str(self.hp) + '/' + str(
            self.maxhp) + "|" + Bcolors.WARNING + hp_bar + Bcolors.ENDC + "|     " + space2 + str(self.mp) + '/' + str(
            self.maxmp) + "|" + Bcolors.FAIL + mp_bar + Bcolors.ENDC + "| ")


    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp/self.maxhp) * 100 / 4
        mp_bar = ""
        mpbar_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks >= 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += "░"

        while mpbar_ticks >= 0:
            mp_bar += "█"
            mpbar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += "░"

        space1 = ""
        space2 = ""
        while len(str(self.hp)) <4:
            space1 += " "

        while len(str(self.mp)) < 3:
            space2 += " "

        print("                           ________________________________________               _________________")
        print(self.name + "           " + space1 + str(self.hp) + '/' + str(self.maxhp) + "|" + Bcolors.OKGREEN + hp_bar + Bcolors.ENDC + "|     " + space2 + str(self.mp) + '/' + str(self.maxmp) + "|" + Bcolors.OKBLUE + mp_bar + Bcolors.ENDC + "| ")

    def choose_target(self, enemies):
        i = 1

        print("\n" + Bcolors.FAIL + Bcolors.BOLD + "    TARGET:" + Bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target:")) - 1
        return choice


    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg