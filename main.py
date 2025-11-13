#Hunter Knoble

from Modules.Nearest_neighbor import plan_truck, package_table
from User_interface import ui
from datetime import datetime
import time

truck1_packages = [13, 14, 15, 16, 19, 20, 1, 29, 30, 31, 34, 37, 40]
truck2_packages = [3, 6, 18, 25, 28, 32, 36, 38, 27, 35, 39]
truck3_packages = [9, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 33]

Delayed = {6, 25, 28, 32}
for pid in Delayed:
    pkg = package_table.get(pid)
    if pkg:
        pkg.available_time = datetime.strptime("09:05", "%H:%M")

def run_simulation():
    start_timer = time.time()

    truck1_start = datetime.strptime("08:00", "%H:%M")
    truck2_start = datetime.strptime("09:05", "%H:%M")
    truck3_start = datetime.strptime("10:30", "%H:%M")

    results = []
    results.append(plan_truck("Truck 1", truck1_packages, truck1_start))
    results.append(plan_truck("Truck 2", truck2_packages, truck2_start))
    results.append(plan_truck("Truck 3", truck3_packages, truck3_start))


    print(f"\nTotal execution time: {time.time() - start_timer:.2f} seconds\n")

    # Launch the CLI
    ui(results, package_table)

run_simulation()