#use this list of menu items
menu_items = {
'D1': ['SODA', 3],
'D2': ['LEMONADE', 3],
'D3': ['TEA' ,2],
'D4': ['WATER', 0],
'A1': ['POTATO_CAKES', 7, 33],
'A2': ['SPINACH_DIP', 5, 43],
'A3': ['OYSTERS', 13, 28],
'A4': ['CHEESE_FRIES', 4, 30],
'A5': ['ONION_RINGS', 7, 27],
'S1': ['COBB', 14, 35],
'S2': ['CAESAR', 13, 36],
'S3': ['GREEK', 12, 48],
'E1': ['BURGER', 16, 40],
'E2': ['PASTA', 15, 32],
'E3': ['GNOCCHI',14, 31],
'E4': ['GRILLED_STEAK_SANDWICH',17, 26],
'T1': ['CARAMEL_CHEESECAKE',13, 48],
'T2': ['APPLE_COBBLER',12, 49],
'T3': ['BROWNIE_SUNDAE',9, 49],
'T4': ['FLAN', 8, 39]
}
drink_items = ['D1', 'D2',  'D3', 'D4']
appetizer_items = ['A1', 'A2',  'A3', 'A4', 'A5']
salad_items = ['S1', 'S2', 'S3']
entree_items = ['E1', 'E2',  'E3', 'E4']
dessert_items =['T1', 'T2',  'T3', 'T4']
all_items = drink_items + appetizer_items + salad_items + entree_items + dessert_items

#defining items of categories
drink_items = ['D1', 'D2', 'D3', 'D4']
appetizer_items = ['A1', 'A2', 'A3', 'A4', 'A5']
salad_items = ['S1', 'S2', 'S3']
entree_items = ['E1', 'E2', 'E3', 'E4']
dessert_items = ['T1', 'T2', 'T3', 'T4']

# Creating a list of dictionaries
menu_dicts = []
for code, details in menu_items.items():
    item_dict = {
        "code": code,
        "name": details[0],
        "price": details[1],
        "stock_number": details[2] if len(details) > 2 else None
    }

   # Assign category based on item code
    if code in drink_items:
        item_dict["category"] = "Drink"
    elif code in appetizer_items:
        item_dict["category"] = "Appetizer"
    elif code in salad_items:
        item_dict["category"] = "Salad"
    elif code in entree_items:
        item_dict["category"] = "Entree"
    elif code in dessert_items:
        item_dict["category"] = "Dessert"
    
    menu_dicts.append(item_dict)