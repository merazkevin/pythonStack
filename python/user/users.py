class User:		
    def __init__(self,first_name,last_name,age,email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email= email
        self.is_rewards_member = False
        self.gold_card_points = 0
    # @classmethods
    def display_info(self):
        print(f' name={self.first_name}, last_name={self.last_name}, age={self.age}, email={self.email}, Rewards_member={self.is_rewards_member}, card point={self.gold_card_points}')
    # def enroll(self,amount):


user_kevin=User('kevin', 'Meraz', '32', 'fdas@sfd.com')
user_kevin.display_info()