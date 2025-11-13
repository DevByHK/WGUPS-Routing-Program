from datetime import datetime

def summary(results):
    total_miles_all = 0
    latest_finish = None

    print("\n --- WGUPS DELIVERY INTERFACE --- \n")
    for r in results:
        print(f"\n {r['truck']}:")
        print(f"  Packages: {r['packages']}")
        print(f"  Total miles: {round(r['miles'], 2)}")
        print(f"  Finished at: {r['finish_time'].time()}")

        total_miles_all += r['miles']
        if not latest_finish or r['finish_time'] > latest_finish:
            latest_finish = r['finish_time']

    print(f"\n Total miles traveled (all trucks): {round(total_miles_all, 2)}")
    print(f"All trucks finished by: {latest_finish.time()}\n")

def single_package_status(package_table):
    pid = int(input("Enter Package ID: "))
    pkg = package_table.get(pid)
    if not pkg:
        print("INVALID PACKAGE ID")
        return
    
    time_str = input("Enter time (HH:MM): ")
    query_time = datetime.strptime(time_str, "%H:%M")

    status = pkg.get_status(query_time)
    deadline = pkg.deadline if pkg.deadline else "EOD"
    truck = getattr(pkg, "truck", "N/A")

    print("\nPackage Info:")
    print(f"  ID: {pid}")
    print(f"  Address: {pkg.address}")
    print(f"  Deadline: {deadline}")
    print(f"  Truck: {truck}")
    print(f"  Status at {query_time.time()}: {status}\n")

def total_package_status(package_table):
    time_str = input("Enter time (HH:MM): ")
    query_time = datetime.strptime(time_str, "%H:%M")

    print(f"\nAll package statuses at {query_time.time()}:")
    print(f"{'ID':<5} {'Address':<35} {'Deadline':<12} {'Truck':<8} {'Status'}")
    print("-" * 90)

    for pid in range(1, 41):
        pkg = package_table.get(pid)
        if pkg:
            status = pkg.get_status(query_time)
            deadline = pkg.deadline if pkg.deadline else "EOD"
            truck = getattr(pkg, "truck", "N/A")
            print(f"{pid:<5} {pkg.address:<35} {deadline:<12} {truck:<8} {status}")
    print()

def ui(results, package_table):
    summary(results)

    while True:
        print("Options: ")
        print("\n 1 - View single package status")
        print("\n 2 - View all packages status")
        print("\n 3 - Quit")

        choice = input("Enter choice: ")
        if choice == "1":
            single_package_status(package_table)
        elif choice == "2":
            total_package_status(package_table)
        elif choice == "3":
            print("Exiting ...")
            break
        else:
            print("INVALID, TRY AGAIN")