class PetController:
    def __init__(self):
        self.pets = []

    def get_all_pets(self):
        return self.pets

    def get_pet_by_id(self, pet_id):
        for pet in self.pets:
            if pet['id'] == pet_id:
                return pet
        return None

    def create_pet(self, pet_data):
        self.pets.append(pet_data)
        return pet_data

    def update_pet(self, pet_id, pet_data):
        for index, pet in enumerate(self.pets):
            if pet['id'] == pet_id:
                self.pets[index] = pet_data
                return pet_data
        return None

    def delete_pet(self, pet_id):
        for index, pet in enumerate(self.pets):
            if pet['id'] == pet_id:
                del self.pets[index]
                return True
        return False
                return True
        return False
