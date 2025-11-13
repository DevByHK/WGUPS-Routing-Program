import csv
from Modules.Package import Package
from Modules.load_distance import load_addresses

# Load addresses 
addresses = load_addresses("Csv/WGUPS Address.csv")
addr_lookup = {info["Address"].strip(): addr_id for addr_id, info in addresses.items()}
id_lookup = {addr_id: info["Address"].strip() for addr_id, info in addresses.items()}

def load_packages(filename, package_table):
    #load packages into hash table
    count = 0
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            p = Package(
                id=int(row[0]),
                address=row[1],
                city=row[2],
                state=row[3],
                zip=row[4],
                deadline=row[5],
                weight=row[6],
                notes=row[7] if len(row) > 7 else "",
                status="AT HUB"
            )
            package_table.insert(p.id, p)
            count += 1

def package_to_address_id(pkg):
    #Convert package to its corresponding address
    addr_text = pkg.address.strip()
    return addr_lookup.get(addr_text)