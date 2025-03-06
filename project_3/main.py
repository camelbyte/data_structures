# main.py

from pet import Pet

def read_pet_data(file_path):
    pets = []
    with open(file_path, 'r') as file:
        for line in file:
            pet_data = line.strip().split(' ')
            pet = Pet(pet_data[0], pet_data[1], pet_data[2], pet_data[3])
            pets.append(pet)
    return pets

def display_pets(pets):
    for pet in pets:
        print(pet)

def find_owners_by_family_type(pets, family_type):
    owners = []
    for pet in pets:
        if pet.get_family_type().lower() == family_type.lower():
            owners.append((pet.get_owner(), pet.get_name()))
    return owners

if __name__ == "__main__":
    file_path = '/home/whaler/data_structures/project_3/pet_data.txt'
    pets = read_pet_data(file_path)

    print("All Pets:")
    display_pets(pets)

    snake_owners = find_owners_by_family_type(pets, 'snake')
    insect_owners = find_owners_by_family_type(pets, 'insect')

    snake_owners = {owner: pet_name for owner, pet_name in find_owners_by_family_type(pets, 'snake')}
    insect_owners = {owner: pet_name for owner, pet_name in find_owners_by_family_type(pets, 'insect')}

    print("Owners \t\t Pet Name")
    print(snake_owners)
    print(insect_owners)

