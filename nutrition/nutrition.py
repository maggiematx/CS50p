fruits=[{"Item":"Apple","Calories":"130"},
        {"Item":"Avocado","Calories":"50"},
        {"Item":"Banana","Calories":"110"},
        {"Item":"Cantaloupe","Calories":"50"},
        {"Item":"Grapefruit","Calories":"60"},
        {"Item":"Grapes","Calories":"90"},
        {"Item":"Honeydew","Calories":"50"},
        {"Item":"Kiwifruit","Calories":"90"},
        {"Item":"Lemon","Calories":"15"},
        {"Item":"Lime","Calories":"20"},
        {"Item":"Nectarine","Calories":"60"},
        {"Item":"Orange","Calories":"80"},
        {"Item":"Peach","Calories":"60"},
        {"Item":"Pear","Calories":"100"},
        {"Item":"Pineapple","Calories":"50"},
        {"Item":"Plums","Calories":"70"},
        {"Item":"strawberries","Calories":"50"},
        {"Item":"Sweet Cherries","Calories":"100"},
        {"Item":"Tangerine","Calories":"50"},
        {"Item":"Watermelon","Calories":"80"},
]

user_input=input("Item: ")
for fruit in fruits:
    if user_input==fruit["Item"]:
        print("Calories:",fruit["Calories"])
        break
