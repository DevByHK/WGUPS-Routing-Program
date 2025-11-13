#this holds package details
class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes="", status="AT HUB", address_id=None):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.address_id = address_id  # ID that links to address
        self.departure_time = None
        self.delivery_time = None

    #update package status
    def update_status(self, new_status):
        self.status = new_status

    #get status of package
    def get_status(self, current_time):
        #delayed packages
        if hasattr(self, "available_time") and self.available_time:
            if current_time < self.available_time:
                return "Status: Delayed"
            
        if self.delivery_time and current_time >= self.delivery_time:
            return f"Status: delivered\tDelivered Time: {self.delivery_time}"
        elif self.departure_time and self.departure_time <= current_time < (self.delivery_time or float('inf')):
            return "Status: En Route"
        else:
            return "Status: Hub"

    def __str__(self):
        return (f"Package {self.id}: {self.address}, {self.city}, {self.state} {self.zip} | "
                f"Deadline: {self.deadline} | Weight: {self.weight} | Status: {self.status}")
 