# =========================================================
# main.py
# MENU DRIVEN ZIPRIDE SYSTEM
# =========================================================

import numpy as np

from graph import Graph

from hash_table import (
    PassengerHashTable,
    DriverHashTable,
    Passenger,
    Driver
)

from heap import (
    MaxHeap,
    PickupRequest
)

from sorting import benchmark


# =========================================================
# GRAPH MODULE
# =========================================================

def run_graph_module():

    graph = Graph()

    graph.add_road(
        "CBD",
        "Airport",
        15
    )

    graph.add_road(
        "Airport",
        "IndustrialPark",
        20
    )

    graph.add_road(
        "CBD",
        "University",
        10
    )

    graph.add_road(
        "University",
        "ShoppingMall",
        8
    )

    graph.add_road(
        "ShoppingMall",
        "Hospital",
        6
    )

    graph.add_road(
        "Hospital",
        "IndustrialPark",
        12
    )

    graph.print_graph()

    graph.bfs("CBD")

    graph.dfs_cycle()

    graph.dijkstra(
        "CBD",
        "IndustrialPark"
    )


# =========================================================
# HASH TABLE MODULE
# =========================================================

def run_hash_module():

    passenger_table = PassengerHashTable()

    driver_table = DriverHashTable()

    print(
        "\n===== MODULE 2: "
        "HASH TABLE LOOKUP ====="
    )

    # =====================================================
    # INSERT PASSENGERS
    # =====================================================

    for i in range(20):

        passenger = Passenger(
            101 + i,
            "Passenger" + str(i),
            "CBD",
            (i % 5) + 1
        )

        passenger_table.insert(
            passenger
        )

    print(
        "\n20 passenger records inserted."
    )

    print(
        "Passenger Load Factor:",
        round(
            passenger_table.load_factor(),
            2
        )
    )

    # =====================================================
    # INSERT DRIVERS
    # =====================================================

    for i in range(20):

        driver = Driver(
            201 + i,
            "Driver" + str(i),
            "Airport",
            "Available"
        )

        driver_table.insert(driver)

    print(
        "\n20 driver records inserted."
    )

    print(
        "Driver Load Factor:",
        round(
            driver_table.load_factor(),
            2
        )
    )

    # =====================================================
    # SEARCH TESTS
    # =====================================================

    print("\nSearch Tests:")

    result = passenger_table.search(
        101
    )

    if result is not None:

        print(
            "Passenger 101 FOUND"
        )

    result = driver_table.search(
        201
    )

    if result is not None:

        print(
            "Driver 201 FOUND"
        )

    # =====================================================
    # DELETE TEST
    # =====================================================

    passenger_table.delete(101)

    # =====================================================
    # VALIDATION TESTS
    # =====================================================

    passenger_table.insert(

        Passenger(
            999,
            "",
            "CBD",
            1
        )
    )

    passenger_table.insert(

        Passenger(
            998,
            "Test",
            "CBD",
            9
        )
    )

    driver_table.insert(

        Driver(
            999,
            "Driver",
            "CBD",
            "INVALID"
        )
    )

    print(
        "\n===== HASH TABLE "
        "MODULE COMPLETE ====="
    )


# =========================================================
# HEAP MODULE
# =========================================================

def run_heap_module():

    heap = MaxHeap()

    print(
        "\n===== MODULE 3: "
        "HEAP PICKUP SCHEDULING ====="
    )

    # =====================================================
    # INSERT REQUESTS
    # =====================================================

    for i in range(10):

        passenger = Passenger(
            101 + i,
            "Passenger" + str(i),
            "CBD",
            1
        )

        driver = Driver(
            201 + i,
            "Driver" + str(i),
            "Airport",
            "Available"
        )

        priority = 50 + i

        request = PickupRequest(
            passenger,
            driver,
            priority
        )

        heap.insert(request)

        print(
            "\nInserted Passenger:",
            passenger.passenger_id
        )

    # =====================================================
    # HEAP STATE
    # =====================================================

    heap.print_heap()

    # =====================================================
    # PEEK
    # =====================================================

    top = heap.peek()

    if top is not None:

        print(
            "\nHighest Priority:",
            top.passenger.passenger_id
        )

    # =====================================================
    # EXTRACTION
    # =====================================================

    print("\nExtracting Requests:")

    for i in range(5):

        request = heap.extract_max()

        if request is not None:

            print(
                "Extracted Passenger:",
                request.passenger.passenger_id
            )

    print(
        "\n===== HEAP MODULE "
        "COMPLETE ====="
    )


# =========================================================
# SORTING MODULE
# =========================================================

def run_sorting_module():

    benchmark()


# =========================================================
# FULL SYSTEM DEMO
# =========================================================

def run_full_demo():

    print(
        "\n===== FULL SYSTEM DEMO ====="
    )

    run_graph_module()

    run_hash_module()

    run_heap_module()

    run_sorting_module()

    print(
        "\n===== FULL SYSTEM "
        "DEMO COMPLETE ====="
    )


# =========================================================
# MENU
# =========================================================

def menu():

    while True:

        print(
            "\n===== ZIPRIDE MENU ====="
        )

        print(
            "1. Graph Route Planning"
        )

        print(
            "\n2. Hash Table Lookup"
        )

        print(
            "\n3. Heap Pickup Scheduling"
        )

        print(
            "\n4. Sorting Pickup Records"
        )

        print(
            "\n5. Run Full System Demo"
        )

        print(
            "\n6. Exit"
        )

        choice = input(
            "\nEnter Option : "
        )

        # =================================================
        # OPTION 1
        # =================================================

        if choice == "1":

            run_graph_module()

        # =================================================
        # OPTION 2
        # =================================================

        elif choice == "2":

            run_hash_module()

        # =================================================
        # OPTION 3
        # =================================================

        elif choice == "3":

            run_heap_module()

        # =================================================
        # OPTION 4
        # =================================================

        elif choice == "4":

            run_sorting_module()

        # =================================================
        # OPTION 5
        # =================================================

        elif choice == "5":

            run_full_demo()

        # =================================================
        # OPTION 6
        # =================================================

        elif choice == "6":

            print(
                "\nExiting ZipRide System..."
            )

            break

        # =================================================
        # INVALID
        # =================================================

        else:

            print(
                "\nInvalid Option"
            )


# =========================================================
# RUN PROGRAM
# =========================================================

menu()