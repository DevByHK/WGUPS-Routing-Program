from Modules.load_distance import load_addresses, load_distances, get_distance
from Modules.load_packages import load_packages, package_to_address_id, addr_lookup
from Modules.Hash_table import Hash_table
from datetime import datetime, timedelta

# Load data
addresses = load_addresses("Csv/WGUPS Address.csv")
distances = load_distances("Csv/WGUPS Distance.csv")

# Build package hash table
package_table = Hash_table()
load_packages("Csv/WGUPS Package File Cleaned.csv", package_table)

#put packages onto trucks
truck1_packages = [1, 5, 10, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck2_packages = [3, 6, 18, 25, 28, 32, 36, 38, 7, 8, 9, 11, 12, 17, 21, 22]
truck3_packages = [2, 4, 23, 24, 26, 27, 33, 35, 39]

HUB_ADDRESS = "4001 South 700 East"
HUB_ID = addr_lookup.get(HUB_ADDRESS, 0)

#map package id to address id
def build_truck_plan(package_ids):
    addr_to_pkgs = {}
    skipped = []
    for pid in package_ids:
        pkg = package_table.get(pid)
        if not pkg:
            skipped.append((pid, "not in package table"))
            continue

        addr_id = package_to_address_id(pkg)
        if addr_id is None:
            skipped.append((pid, f"address not found: {pkg.address}"))
            continue

        addr_to_pkgs.setdefault(addr_id, []).append(pid)

    unique_addr_ids = list(addr_to_pkgs.keys())
    return addr_to_pkgs, unique_addr_ids, skipped

#this runs nearest neighbor over the addresses, finding our route
def nearest_neighbor_over_addresses(start_id, targets):
    if not targets:
        return [start_id, start_id], 0.0

    unvisited = set(targets)
    route = [start_id]
    total = 0.0
    current = start_id

    while unvisited:
        nearest = min(unvisited, key=lambda aid: get_distance(distances, current, aid))
        total += get_distance(distances, current, nearest)
        route.append(nearest)
        current = nearest
        unvisited.remove(nearest)

    total += get_distance(distances, current, start_id)
    route.append(start_id)
    return route, total

def address_str(addr_id):
    info = addresses.get(addr_id)
    return info["Address"] if info else f"<Unknown addr {addr_id}>"

TRUCK_SPEED_MPH = 18

def time_to_travel(miles):
    hours = miles / TRUCK_SPEED_MPH
    return timedelta(hours=hours)

#this is the saved outcome of the nearest nna per truck
def plan_truck(truck_name, package_ids, start_time):
    addr_to_pkgs, unique_addr_ids, skipped = build_truck_plan(package_ids)
    addr_route, miles = nearest_neighbor_over_addresses(HUB_ID, unique_addr_ids)

    current_time = start_time
    current_location = HUB_ID
    package_route = []

    total_miles = 0.0
    deadline_violations = []

    for next_addr in addr_route[1:]:
        distance = get_distance(distances, current_location, next_addr)
        total_miles += distance
        travel_time = time_to_travel(distance)
        current_time += travel_time

        for pid in addr_to_pkgs.get(next_addr, []):
            pkg = package_table.get(pid)
            if pkg:
                if pkg.departure_time is None:
                    pkg.departure_time = start_time
                pkg.delivery_time = current_time
                package_route.append(pid)

                pkg.truck = truck_name



        current_location = next_addr

    # return to hub
    distance = get_distance(distances, current_location, HUB_ID)
    total_miles += distance
    current_time += time_to_travel(distance)
    addr_route.append(HUB_ID)

    return {
        "truck": truck_name,
        "route": addr_route,
        "packages": package_route,
        "miles": total_miles,
        "finish_time": current_time,
        "start_time": start_time,
    }