class Converter():
    def __init__(self):
        
        self.length_factors = {
            "m" : 1,
            "km" : 0.001,
            "cm" : 100,
            "mm" : 1000
        }

        self.weight_factors = {
            'g' : 1,
            'kg' : 0.001,
            'mg' : 1000,
            'pounds' : 0.00220462,
            'ounces' : 0.035274
        }

    def convert_length(self, value : int, unit_from : str, unit_to: str) -> int: 

        if unit_from not in self.length_factors or unit_to not in self.length_factors:
            return "UnsupportedUnit"
        
        else:
            meters = value / self.length_factors[unit_from]
            
            return meters * self.lenght_factors[unit_to]
        
    def convert_weight(self, value : int, unit_from : str, unit_to : str) -> int:

        if unit_from not in self.weight_factors or unit_to not in self.weight_factors:
            return "UnsupportedUnit"
        
        else:
            
            grams = value / self.weight_factors[unit_from]
            
            return grams * self.weight_factors[unit_to]
    