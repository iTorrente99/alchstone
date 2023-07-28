import random

class AlchemyStone:
    TIER_LIST = ["Imperfect", "Rough", "Polished", "Sturdy", "Sharp", "Resplendent", "Splendid", "Shining"]
    GRADE_LIST = ["White", "Green", "Blue", "Yellow"]

    tierUpgradeChance = {
        "Imperfect": {"White": 0.1211, "Green": 0.1252, "Blue": 0.1272, "Yellow": 0.132},
        "Rough": {"White": 0.0969, "Green": 0.0991, "Blue": 0.0995, "Yellow": 0.102},
        "Polished": {"White": 0.0727, "Green": 0.073, "Blue": 0.0712, "Yellow": 0.072},
        "Sturdy": {"White": 0.0485, "Green": 0.0469, "Blue": 0.0442, "Yellow": 0.042},
        "Sharp": {"White": 0.0242, "Green": 0.0261, "Blue": 0.0276, "Yellow": 0.03},
        "Resplendent": {"White": 0.0242, "Green": 0.261, "Blue": 0.276, "Yellow": 0.03},
        "Splendid": {"White": 0.0242, "Green": 0.261, "Blue": 0.276, "Yellow": 0.03} 
    }

    gradeUpgradeChance = {
        "Imperfect": {"White": 0.0713, "Green": 0.0388, "Blue": 0.0223},
        "Rough": {"White": 0.057, "Green": 0.0307, "Blue": 0.0175},
        "Polished": {"White": 0.0428, "Green": 0.0226, "Blue": 0.0126},
        "Sturdy": {"White": 0.0285, "Green": 0.0145, "Blue": 0.0078},
        "Sharp": {"White": 0.0143, "Green": 0.0081, "Blue": 0.0049},
        "Resplendent": {"White": 0.0143, "Green": 0.0081, "Blue": 0.0049},
        "Splendid": {"White": 0.0143, "Green": 0.0081, "Blue": 0.0049}
    }
    
    tierAndGradeUpgradeChance = {
        "Imperfect": {"White": 0.025, "Green": 0.024, "Blue": 0.0138},
        "Rough": {"White": 0.02, "Green": 0.019, "Blue": 0.0108},
        "Polished": {"White": 0.015, "Green": 0.014, "Blue": 0.0078},
        "Sturdy": {"White": 0.01, "Green": 0.009, "Blue": 0.0048},
        "Sharp": {"White": 0.005, "Green": 0.005, "Blue": 0.003},
        "Resplendent": {"White": 0.005, "Green": 0.005, "Blue": 0.003},
        "Splendid": {"White": 0.005, "Green": 0.005, "Blue": 0.003}
    }

    keepChance = {
        "Imperfect": {"White": 0.7826, "Green": 0.8121, "Blue": 0.8367, "Yellow": 0.868},
        "Rough": {"White": 0.8261, "Green": 0.8512, "Blue": 0.8722, "Yellow": 0.898},
        "Polished": {"White": 0.8696, "Green": 0.8904, "Blue": 0.9077, "Yellow": 0.928},
        "Sturdy": {"White": 0.5131, "Green": 0.5195, "Blue": 0.5232, "Yellow": 0.528},
        "Sharp": {"White": 0.4165, "Green": 0.4208, "Blue": 0.4245, "Yellow": 0.43},
        "Resplendent": {"White": 0.3265, "Green": 0.3308, "Blue": 0.3345, "Yellow": 0.34},
        "Splendid": {"White": 0.2365, "Green": 0.2408, "Blue": 0.2445, "Yellow": 0.25}
    }

    downgradeChance = {
        "Sturdy": {"White": 0.4, "Green": 0.41, "Blue": 0.42, "Yellow": 0.43},
        "Sharp": {"White": 0.54, "Green": 0.54, "Blue": 0.54, "Yellow": 0.54}
    }

    destroyChance = {
        "Resplendent": {"White": 0.63, "Green": 0.63, "Blue": 0.63, "Yellow": 0.63},
        "Splendid": {"White": 0.72, "Green": 0.72, "Blue": 0.72, "Yellow": 0.72}
    }

    stoneMarketValue = {
        "Imperfect": {"White": 850000, "Green": 2800000, "Blue": 8150000, "Yellow": 33000000},
        "Rough": {"White": 2440000, "Green": 6700000, "Blue": 19600000, "Yellow": 79500000},
        "Polished": {"White": 5850000, "Green": 15900000, "Blue": 47000000, "Yellow": 190000000},
        "Sturdy": {"White": 14100000, "Green": 38600000, "Blue": 113000000, "Yellow": 386000000},
        "Sharp": {"White": 42200000, "Green": 113000000, "Blue": 269000000, "Yellow": 1100000000},
        "Resplendent": {"White": 113000000, "Green": 222000000, "Blue": 650000000, "Yellow": 5300000000},
        "Splendid": {"White": 1200000000, "Green": 500000000, "Blue": 1550000000, "Yellow": 12700000000} 
    }

    stonePolish = {
        "Imperfect": 130,
        "Rough": 260,
        "Polished": 389,
        "Sturdy": 519,
        "Sharp": 648,
        "Resplendent": 778,
        "Splendid": 908
    }

    def __init__(self, tier, grade, startTier, startGrade, polishCost):
        if tier not in AlchemyStone.TIER_LIST:
            raise ValueError("Invalid tier.")
        if grade not in AlchemyStone.GRADE_LIST:
            raise ValueError("Invalid grade.")
        
        self.tier = tier
        self.grade = grade
        self.startTier = startTier
        self.startGrade = startGrade
        self.polishCost = polishCost
        self.totalCost = 0
        self.blackStoneCost = 120000

    def upgradeTier(self):
        #print("upgrade tier",self.totalCost)
        tier_index = AlchemyStone.TIER_LIST.index(self.tier)
        if tier_index < len(AlchemyStone.TIER_LIST) - 1:
            self.tier = AlchemyStone.TIER_LIST[tier_index + 1]
            if self.tier != "Shining":
                self.totalCost += self.polishCost * self.stonePolish[self.tier] + self.blackStoneCost


    def upgradeGrade(self, both):
        #print("upgrade grade",self.totalCost)
        grade_index = AlchemyStone.GRADE_LIST.index(self.grade)
        if grade_index < len(AlchemyStone.GRADE_LIST) - 1:
            self.grade = AlchemyStone.GRADE_LIST[grade_index + 1]
            if both == False:
                self.totalCost += self.polishCost * self.stonePolish[self.tier] + self.blackStoneCost

    def upgradeTierAndGrade(self):
        #print("upgrade both",self.totalCost)
        self.upgradeTier()
        self.upgradeGrade(True)

    def keepStone(self):
        #print("keep",self.totalCost)
        self.totalCost += self.polishCost * (self.stonePolish[self.tier]/2) + self.blackStoneCost
    
    def downgradeTier(self):
        #print("downgrade")
        tier_index = AlchemyStone.TIER_LIST.index(self.tier)
        if tier_index < len(AlchemyStone.TIER_LIST) - 1:
            self.tier = AlchemyStone.TIER_LIST[tier_index - 1]
            self.totalCost += self.polishCost * self.stonePolish[self.tier] + self.blackStoneCost

    def destroyStone(self):
        self.tier = self.startTier
        self.grade = self.startGrade
        self.totalCost += AlchemyStone.stoneMarketValue[self.tier].get(self.grade) + self.polishCost * self.stonePolish[self.tier] + self.blackStoneCost
        #print("poof",self.totalCost)
    
    def enhance(self):
        if self.tier == "Shining":
            print("Cannot enhance anymore.")
        else:
            currentTierUpgradeChance = AlchemyStone.tierUpgradeChance[self.tier].get(self.grade)
            currentKeepChance = AlchemyStone.keepChance[self.tier].get(self.grade)
            if self.grade != "Yellow":
                currentTierAndGradeUpgradeChance = AlchemyStone.tierAndGradeUpgradeChance[self.tier].get(self.grade)
                currentGradeUpgradeChance = AlchemyStone.gradeUpgradeChance[self.tier].get(self.grade)
            else:
                currentTierAndGradeUpgradeChance = 0
                currentGradeUpgradeChance = 0
            if self.tier == "Sturdy" or self.tier == "Sharp":
                currentDowngradeChance = AlchemyStone.downgradeChance[self.tier].get(self.grade)
            else:
                currentDowngradeChance = 0
            if self.tier == "Resplendent" or self.tier == "Splendid":
                currentDestroyChance = AlchemyStone.destroyChance[self.tier].get(self.grade)
            else:
                currentDestroyChance = 0
            
            tapResult = random.random()

            if tapResult < currentTierUpgradeChance:
                self.upgradeTier()
            elif tapResult < currentTierUpgradeChance + currentTierAndGradeUpgradeChance:
                self.upgradeTierAndGrade()
            elif tapResult < currentTierUpgradeChance + currentTierAndGradeUpgradeChance + currentGradeUpgradeChance:
                self.upgradeGrade(False)
            elif tapResult < currentTierUpgradeChance + currentTierAndGradeUpgradeChance + currentGradeUpgradeChance + currentKeepChance:
                self.keepStone()
            elif tapResult < currentTierUpgradeChance + currentTierAndGradeUpgradeChance + currentGradeUpgradeChance + currentKeepChance + currentDowngradeChance:
                self.downgradeTier()
            elif tapResult < currentTierUpgradeChance + currentTierAndGradeUpgradeChance + currentGradeUpgradeChance + currentKeepChance + currentDowngradeChance + currentDestroyChance:
                self.destroyStone()

    def __str__(self):
        formatted_cost = "{:,}".format(self.totalCost)
        return f"Alchemy Stone: Tier {self.tier}, Grade {self.grade}, Cost {formatted_cost}"
            
def append_to_file(file_path,data):
        formatted_data = str(data)  # Get the formatted data using the __str__ method

        with open(file_path, "a") as file:
            file.write(formatted_data + "\n")

stone1 = AlchemyStone("Polished","Green","Polished","Green",21000)
i = 0
stonecount = 0
while stonecount<100:
    while stone1.tier != "Splendid":
        stone1.enhance()
        i += 1
    append_to_file("output.txt",stone1)
    stone1 = AlchemyStone("Polished","Green","Polished","Green",21000)
    stonecount += 1
            