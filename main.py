import random
import logo_and_data


def compare(x,y):
    if x["follower_count"]>= y["follower_count"]:
        return A
    else:
        return B

def Answer(correct_ans,option):
    if correct_ans==option:
        global score
        score+=1
        print(f"\nCongrats, You're right! Current score: {score}")
        return True
    else:
        print(f"\nSorry, that's wrong. Final score: {score}")
        return False


A=random.choice(logo_and_data.data)
logo_and_data.data.remove(A)
program_run=True
score = 0

while program_run:
    print(f"\nCompare A: {A['name']}, a {A["description"]}, from {A["country"]}.")
    print(logo_and_data.vs)
    B=random.choice(logo_and_data.data)
    logo_and_data.data.remove(B)
    print(f"Compare B: {B["name"]}, a {B["description"]}, from {B["country"]}.")
    choice = input("\nWho has more followers? type 'A' or 'B':  ")
    if choice=='A':
        choice=A
    else:
        choice=B
    ans = compare(A,B)
    n = Answer(ans,choice)
    if n==False:
        program_run=False
    
    A=B