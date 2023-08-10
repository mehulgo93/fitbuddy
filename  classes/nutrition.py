class Nutrition:
    def __init__(self, user, date, calories, protein, carbs, fat):
        self.user = user
        self.date = date
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value):
        self._user = value
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        self._date = value
    
    @property
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, value):
        CALORIES_IS_AN_INT = type(value) == int
        if CALORIES_IS_AN_INT:
            self._calories = value
    

    @property
    def protein(self):
        return self._protein
    
    @protein.setter
    def protein(self, value):
        PROTEIN_IS_AN_INT = type(value) == str
        if PROTEIN_IS_AN_INT:
            self._protein = value
    
    @property
    def carbs(self):
        return self._carbs
    
    @carbs.setter
    def carbs(self, value):
        CARBS_IS_AN_INT = type(value) == int
        if CARBS_IS_AN_INT:
            self._carbs = value
    
    @property
    def fat(self):
        return self.__fat
    
    @fat.setter
    def fat(self, value):
        FAT_IS_AN_INT = type(value) == int
        if FAT_IS_AN_INT:
            self._fat = value
    
    
        
