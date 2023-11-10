def main():
    fruit = input("Item: ").upper()
    if str(get_cal(fruit)) != "":
        print("Calories: ",str(get_cal(fruit)))
    else:
        print("")

def get_cal(s):
 
    fruits = {
         "APPLE": 130
        ,"AVOCADO": 50
        ,"BANANA": 110
        ,"CANTALOUPE": 50
        ,"GRAPEFRUIT": 60
        ,"GRAPES": 90
        ,"HONEYDEW Melon": 50
        ,"KIWIFRUIT": 90
        ,"LEMON": 15
        ,"LIME": 20
        ,"NECTARINE": 60
        ,"ORANGE": 80
        ,"PEACH": 60
        ,"PEAR": 100
        ,"PINEAPPLE": 50
        ,"PLUMS": 70
        ,"STRAWBERRIES": 50
        ,"SWEET CHERRIES": 100
        ,"TANGERINE": 50
        ,"WATERMELON": 80
    }

    if s in fruits:
        return fruits[s]
    else:
        return ""

main()