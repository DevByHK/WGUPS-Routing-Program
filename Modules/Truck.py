#creating the trucks
class Truck:
    def __init__(self, truck_id, departure_time):
        self.truck_id = truck_id
        self.departure_time = departure_time

        self.packages = []
        self.current_location = "Hub"
        self.miles_traveled = 0.0

        self.speed = 18 #mph

    def load_package(self, package):
        #load package to truck if less than 16 total packages already loaded
        if len(self.packages) < 16:
            self.packages.append(package)
            #update status after loading the truck
            package.update_status("EN ROUTE")
        else:
            #show if truck is already at limit of packages
            raise Exception(f"Truck {self.truck_id} is full.")
        
    def get_status(self):
        return(f"Truck {self.truck_id} | Location: {self.current_location} | Miles: {self.miles_traveled: .2f} | Packages on board: {len(self.packages)} | Departure: {self.departure_time}")
    
    def __str__(self):
        return self.get_status()