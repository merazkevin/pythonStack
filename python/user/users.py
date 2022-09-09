from pickle import TRUE


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
    def enroll(self,):
        if self.gold_card_points ==0:
            self.gold_card_points+= 200
        if self.is_rewards_member == True:
            print ('*WARNING*')
            print(f'User {self.first_name}, {self.last_name} already is a member.')
        if  self.gold_card_points > 0:
            self.is_rewards_member = True
    def spend_point(self,amount):
        if self.is_rewards_member==False:
            print('*WARNING* no Goldcard points.You are not a member')
        elif self.gold_card_points < 0:
            print(f'*WARNING*-Unsufficient GoldCard points! Current Balance*{self.gold_card_points}')
        else:
            self.gold_card_points = self.gold_card_points - amount


user_kevin=User('kevin1', 'Meraz1', '32', 'fdas@sfd.com1')
user_kevin.enroll()
user_kevin.spend_point(50)
user_kevin.display_info()
user_kevin.enroll()


user_kevin2=User('kevin2', 'Meraz2', '32', 'fdas@sfd.com2')
user_kevin2.enroll()
user_kevin2.spend_point(80)
user_kevin2.display_info()

user_kevin3=User('kevin3', 'Meraz3', '32', 'fdas@sfd.com3')
user_kevin3.display_info()
user_kevin3.spend_point(50)

