from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []
        
    @property
    def food(self):
        food_objs = [f for f in self.supplies if f.__class__.__name__ == "FoodSupply"]
        if not self.supplies:
            raise IndexError("There are no food supplies left!")
        return food_objs

    @property
    def water(self):
        water_objs = [f for f in self.supplies if f.__class__.__name__ == "WaterSupply"]
        if not self.supplies:
            raise IndexError("There are no water supplies left!")
        return water_objs

    @property
    def painkillers(self):
        painkiller_objs = [f for f in self.supplies if f.__class__.__name__ == "Painkiller"]
        if not self.medicine:
            raise IndexError("There are no painkillers left!")
        return painkiller_objs

    @property
    def salves(self):
        salve_objs = [f for f in self.supplies if f.__class__.__name__ == "Salve"]
        if not self.medicine:
            raise IndexError("There are no salves left!")
        return salve_objs

    def add_survivor(self, survivor: Survivor):
        if survivor.name in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if not survivor.needs_healing:
            return

        if medicine_type == "Painkiller":
            last_medicine = self.medicine.pop()
            last_medicine.apply(survivor)
        elif medicine_type == "Salve":
            last_medicine = self.medicine.pop()
            last_medicine.apply(survivor)

        return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if not survivor.needs_sustenance:
            return

        if sustenance_type == "FoodSupply":
            last_supp = self.supplies.pop()
            last_supp.apply(survivor)
        elif sustenance_type == "WaterSupply":
            last_supp = self.supplies.pop()
            last_supp.apply(survivor)

        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")
