from rich import print 
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from car_management import CarManager

console = Console()

# create main terminal car manager function to call 
def terminal_car_manager():
    # set menu counter
    menu_choice = 0
    # create while loop to allow program to cont until exit is called in order to maintain input
    while menu_choice != '7':
        # call main menu funct
        main_menu()
        # create var to store user menu input
        menu_choice = console.input(":waving_hand: Hello, please enter your selection : [bold red][i]1, 2, 3, 4, 5, 6, 7[/i]? :point_right: ")
        # switch statement for menu options
        match menu_choice:
            case '1' : add_car()
            case '2' : all_cars()
            case '3' : total_cars()
            case '4' : car_details()
            case '5' : enter_service()
            case '6' : mileage_update()

# terminal helper to not exit unless key press
def exit():
    return input("Press enter to return to main menu")

# helper funct for repetition when calling on car id instances
def get_car_id():
    car_id = int(input("Enter the car ID:"))
    car = CarManager.get_car(car_id)
    return car

# create main menu for terminal
def main_menu():
    menu = ["1. Add Car", "2. View all cars", "3. View total number of cars", "4. See a car's details", "5. Service a car", "6. Update Mileage", "7. Quit"]
    
    console.rule(":diamond_shape_with_a_dot_inside: [b]Welcome to Car Manager[/b] :diamond_shape_with_a_dot_inside:", style="blue")
    table = Table(show_header=False, show_lines=False, style="purple4")
    table.add_column(min_width=40, justify="center")
    table.add_column(min_width=40, justify="center")
    table.add_row(Panel(menu[0], expand=True, style="cyan1"),Panel(menu[1], expand=True, style="cyan1"))
    table.add_row(Panel(menu[2], expand=True, style="cyan1"), Panel(menu[3], expand=True, style="cyan1"))
    table.add_row(Panel(menu[4], expand=True, style="cyan1"), Panel(menu[5], expand=True, style="cyan1"))
    table.add_row(Panel(menu[6], expand=True, style="cyan1"))
    console.print(table)
    console.rule("[b]End Main Menu[/b]", style="blue")
    

# get user car info
def add_car():
    car_make = input("Enter your car's make:")
    car_model = input("Enter your car's model:")
    car_year = input("Enter your car's year:")
    car_mileage = input("Enter your car's current mileage:")
    car_services = input("Enter any services your car's had separated by commas:")
    car_services_list = car_services.split(',')
    # create instance using the var entered
    owner_name_input = input("Enter your last name:")
    owner_name = CarManager(car_make, car_model, car_year, car_mileage, car_services_list)
    exit()
    
# see all cars
def all_cars():
    console.print(CarManager.all_cars)
    exit()
    
# see total cars
def total_cars():
    console.print(CarManager.total_cars)
    exit()
    
# see car details funct
def car_details():
    # use helper func to get car id
    car = get_car_id()
    # if car exists print the car using CarManagement str setup
    if car is not None:
        print(car)
    else:
        print("There is no car by that ID.")
    exit()
    
# add a service
def enter_service():
    car = get_car_id()
    if car is not None:
        # print car so user sees car data first prior to entering info 
        print(car)
        service = input("What service would you like to add?")
        car.add_service(service)
    else:
        print("There is no car by that ID.")
    exit()
    
# update mileage
def mileage_update():
    car = get_car_id()
    if car is not None:
        # print car mileage to show user current setting to make sure they want to update
        print(f'Current car mileage is {car._mileage}')
        # set entered user input to var and ensure it's an int
        mileage = int(input("What mileage would you like to set it to?"))
        # call on setter from CarManager
        car.set_mileage(mileage)
        # print new mileage
        print(f"New mileage set to: {car._mileage}")
    else:
        print("There is no car by that ID.")
    exit()

terminal_car_manager()       
