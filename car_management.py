# create a class named CarManager w/ the following attributes: 
# - all_cars (class attribute) a list/dict that will store all the car instances created
# - total_cars (class attribute) an integer that will keep track of the total num of cars

class CarManager: 
    all_cars = []
    total_cars = 0
    
    def __init__(self, make, model, year, mileage, services=[]):
        self._id = CarManager.total_cars + 1
        CarManager.total_cars += 1
        CarManager.all_cars.append(self)
        
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
    
    @staticmethod
    def get_car(car_id):
        for car in CarManager.all_cars:
            if car._id == car_id:
                return car
            
        return None
        
    # view instance detail// See a car's details    
    def __str__(self):
        return f'ID: {self._id}, MAKE: {self._make}, MODEL: {self._model}, YEAR: {self._year}, MILEAGE: {self._mileage}, SERVICES: {self._services}.'
    
    # view all cars details
    def __repr__(self):
        return f'(ID: {self._id} make={self._make}, model={self._model}, year={self._year}, mileage={self._mileage}, services={self._services})'

    # print current services and add service which will return new list as well 
    def print_services (self):
        str_services = ', '.join(self._services)
        print(f'Services completed include {str_services}.')
        
    def add_service(self, new_service):
        self._services.append(new_service)
        print(f'New services added.')
        return self.print_services()
    
    # get and set new mileage
    @property
    def get_mileage(self):
        return self._mileage
    

    def set_mileage(self, new_mileage):
        if isinstance(new_mileage, int) and new_mileage >= self._mileage:
            self._mileage = new_mileage
        else: 
            print("You cannot rollback car's mileage")



# Car Instances
CarManager('Jeep', 'Wrangler', 2016, 76400, ['oil change', '2020 new tires'])
CarManager('Chevrolet', 'Silverado 2500', 2020, 64500, ['oil change', 'tire rotation'])
CarManager('Honda', 'Civic', 2010, 150456, ['oil change', 'tire rotation', '2019 new tires'])


#print(jeep._id)
#print(jeep._services)
#print(chevy_truck._services)
#print_services()
#car1.add_service('tire rotation')

