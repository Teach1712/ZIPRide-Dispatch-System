# =========================================================
# hash_table.py
# =========================================================

import numpy as np

TABLE_SIZE = 53


# =========================================================
# PASSENGER CLASS
# =========================================================

class Passenger:

    def __init__(
            self,
            passenger_id,
            name,
            pickup_location,
            membership_tier):

        self.passenger_id = passenger_id
        self.name = name
        self.pickup_location = pickup_location
        self.membership_tier = membership_tier


# =========================================================
# DRIVER CLASS
# =========================================================

class Driver:

    def __init__(
            self,
            driver_id,
            name,
            current_location,
            availability_status):

        self.driver_id = driver_id
        self.name = name
        self.current_location = current_location
        self.availability_status = \
            availability_status


# =========================================================
# NODE CLASS
# =========================================================

class Node:

    def __init__(self, key, data):

        self.key = key
        self.data = data
        self.next = None


# =========================================================
# PASSENGER HASH TABLE
# =========================================================

class PassengerHashTable:

    def __init__(self):

        self.size = TABLE_SIZE

        self.table = np.empty(
            TABLE_SIZE,
            dtype=object
        )

        for i in range(TABLE_SIZE):

            self.table[i] = None

        self.count = 0

    # =====================================================
    # HASH FUNCTION
    # =====================================================

    def hash_function(self, key):

        return key % self.size

    # =====================================================
    # INSERT
    # =====================================================

    def insert(self, passenger):

        # VALIDATION

        if passenger.membership_tier < 1 or \
           passenger.membership_tier > 5:

            print(
                "Invalid membership tier: "
                "REJECTED"
            )

            return

        if passenger.name == "":

            print(
                "Empty passenger name: "
                "REJECTED"
            )

            return

        index = self.hash_function(
            passenger.passenger_id
        )

        current = self.table[index]

        # DUPLICATE CHECK

        while current is not None:

            if current.key == \
                    passenger.passenger_id:

                print(
                    "Duplicate passenger ID: "
                    "REJECTED"
                )

                return

            current = current.next

        # INSERT NODE

        node = Node(
            passenger.passenger_id,
            passenger
        )

        node.next = self.table[index]

        self.table[index] = node

        self.count += 1

    # =====================================================
    # SEARCH
    # =====================================================

    def search(self, passenger_id):

        index = self.hash_function(
            passenger_id
        )

        current = self.table[index]

        while current is not None:

            if current.key == passenger_id:

                return current.data

            current = current.next

        return None

    # =====================================================
    # DELETE
    # =====================================================

    def delete(self, passenger_id):

        index = self.hash_function(
            passenger_id
        )

        current = self.table[index]

        previous = None

        while current is not None:

            if current.key == passenger_id:

                if previous is None:

                    self.table[index] = \
                        current.next

                else:

                    previous.next = current.next

                self.count -= 1

                print(
                    "Delete Passenger",
                    passenger_id,
                    ": SUCCESS"
                )

                return

            previous = current
            current = current.next

        print(
            "Delete Passenger",
            passenger_id,
            ": KEY NOT FOUND"
        )

    # =====================================================
    # LOAD FACTOR
    # =====================================================

    def load_factor(self):

        return self.count / self.size


# =========================================================
# DRIVER HASH TABLE
# =========================================================

class DriverHashTable:

    def __init__(self):

        self.size = TABLE_SIZE

        self.table = np.empty(
            TABLE_SIZE,
            dtype=object
        )

        for i in range(TABLE_SIZE):

            self.table[i] = None

        self.count = 0

    # =====================================================
    # HASH FUNCTION
    # =====================================================

    def hash_function(self, key):

        return key % self.size

    # =====================================================
    # INSERT
    # =====================================================

    def insert(self, driver):

        valid_status = np.array([
            "Available",
            "Busy",
            "Offline"
        ])

        valid = False

        for i in range(len(valid_status)):

            if driver.availability_status \
                    == valid_status[i]:

                valid = True

        if not valid:

            print(
                "Invalid driver status: "
                "REJECTED"
            )

            return

        index = self.hash_function(
            driver.driver_id
        )

        current = self.table[index]

        while current is not None:

            if current.key == driver.driver_id:

                print(
                    "Duplicate driver ID: "
                    "REJECTED"
                )

                return

            current = current.next

        node = Node(
            driver.driver_id,
            driver
        )

        node.next = self.table[index]

        self.table[index] = node

        self.count += 1

    # =====================================================
    # SEARCH
    # =====================================================

    def search(self, driver_id):

        index = self.hash_function(
            driver_id
        )

        current = self.table[index]

        while current is not None:

            if current.key == driver_id:

                return current.data

            current = current.next

        return None

    # =====================================================
    # LOAD FACTOR
    # =====================================================

    def load_factor(self):

        return self.count / self.size