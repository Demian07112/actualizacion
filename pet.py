class Pet:
    def __init__(self, pet_id, name, species, age):
        self.id = pet_id
        self.name = name
        self.species = species
        self.age = age

    def __repr__(self):
        return f"Pet(id={self.id}, name='{self.name}', species='{self.species}', age={self.age})"

    def validate(self):
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(self.species, str) or not self.species:
            raise ValueError("Species must be a non-empty string.")
        if not isinstance(self.age, int) or self.age < 0:
            raise ValueError("Age must be a non-negative integer.")
