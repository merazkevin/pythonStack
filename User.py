class Fighter:
    def __init__(self):
        self.first_name = "Kevin"
        self.last_name = " MerazBueso"
        self.age = 29
        self.tittle_holder = False
fighter_Kevin = Fighter()
fighter_Dereck = Fighter()
fighter_Dereck.first_name = "Dereck"
fighter_Dereck.last_name = "Meraz"

# print(fighter_Dereck.first_name)
# print(fighter_Dereck.last_name)

class Shoe:
    def __init__(self):
        self.brand ="vans"
        self.type="classic sk8-hi"
        self.price= 69.99
        self.in_stock = True
skater_shoe = Shoe()
dress_shoe = Shoe()

skater_shoe.type = "low-top Trainers"
# print(skater_shoe.type)
dress_shoe.type = "Ballet Flats"
# print(dress_shoe.type)


#<---- Methods--->

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
	    print(f"Hello, my name is {self.name}")

Kevin = User("kevin", "merazkevin@yahoo.com")
cool_person = User("Mark", "Mark@thisEmailfake.com")

Kevin.greeting()
cool_person.greeting()