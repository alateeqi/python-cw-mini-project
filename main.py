# write your code here
def padel_court_cost(court_type):
    
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20

    
def   rackets_cost(racket_brand):
    if racket_brand == "bullpadd":
        return 100
    elif racket_brand == "nox":
        return 140
    elif racket_brand == "siux":
        return 200


def padel_balls_cost(ball_boxes):
    if  ball_boxes == " one box":
        return 2
    elif ball_boxes == "tow boxes":
        return 3.5
    elif ball_boxes == "theree boxes":
        return 5
    else:
        print("return the price")
        


def padel_game_cost():
    court_type=(input("the court type"))
    racket_brand=(input("racket brand")) 
    ball_boxes=int(input("number of ball boxs")) 
    total=padel_balls_cost(ball_boxes) + padel_court_cost(court_type) +rackets_cost(racket_brand)
    return total

   
print(padel_game_cost())
  


