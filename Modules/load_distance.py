import csv

#load addresses
def load_addresses(filename="Csv/WGUPS Address.csv"):
    addresses = {}
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            #store address with ID as key
            addresses[int(row["ID"])] = {"Name": row["Name"], "Address": row["Address"]}
    return addresses

def load_distances(filename="Csv/WGUPS Distance.csv"):
    distances = []
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            distances.append([float(x) if x else 0.0 for x in row[1:]])
    return distances

#get distance between two address ids
def get_distance(matrix, from_id, to_id):
    if matrix[from_id][to_id] != 0:
        return matrix[from_id][to_id]
    else:
        return matrix[to_id][from_id]