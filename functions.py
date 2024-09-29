#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data
def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  print(item_code)
  for item in data.menu_items:
    item_number, item_name, item_price = item.split(' ')
    if item_number == item_code:
      return item_name.encode("ascii", "ignore").decode(), int(item_price)

def display_items():
  pass

def get_item_number():
  while True:
    print('Drinks', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'D'])
    print('Appetizers', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'A'])
    #write code for displaying the other dishes also
    order_item = input('Enter dish number and quantity: ')
    if order_item.split()[0] in data.all_items:
      return order_item
    else:
      print('Invalid dish number.  Please try again')
def manager():
  while True:
    print("\nHello Musthak") #Manager name
    print("__________\n")
    print('Choose R to remove an item')
    print('Choose A to add an new item')
    print('Choose D to change description of an item')
    print('Choose Q to quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Rr':
      remove_item = input('Enter the dish number of item  you want to remove: ')
      data.menu_items.pop(remove_item)
      print(data.menu_items)
    elif user_menu_choice in 'Aa':
      item_code = input('Enter dish number: ')
      desc = input('Enter dish description: ')
      cost = input('Enter dish price: ')
      stock = input('Enter dish stock number: ')
      data.menu_items[str(item_code)] = list()
      data.menu_items[str(item_code)].append(str(desc))
      data.menu_items[str(item_code)].append(int(cost))
      data.menu_items[str(item_code)].append(int(stock))
      print(data.menu_items)


