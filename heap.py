# =========================================================
# heap.py
# =========================================================

import numpy as np

MAX_HEAP = 100


# =========================================================
# PICKUP REQUEST CLASS
# =========================================================

class PickupRequest:

    def __init__(
            self,
            passenger,
            driver,
            priority):

        self.passenger = passenger
        self.driver = driver
        self.priority = priority


# =========================================================
# MAX HEAP CLASS
# =========================================================

class MaxHeap:

    def __init__(self):

        self.heap = np.empty(
            MAX_HEAP,
            dtype=object
        )

        for i in range(MAX_HEAP):

            self.heap[i] = None

        self.size = 0

    # =====================================================
    # INSERT
    # =====================================================

    def insert(self, request):

        self.heap[self.size] = request

        index = self.size

        # HEAPIFY UP

        while index > 0:

            parent = (index - 1) // 2

            if self.heap[index].priority > \
               self.heap[parent].priority:

                temp = self.heap[index]

                self.heap[index] = \
                    self.heap[parent]

                self.heap[parent] = temp

                index = parent

            else:

                break

        self.size += 1

    # =====================================================
    # EXTRACT MAX
    # =====================================================

    def extract_max(self):

        if self.size == 0:

            print("Heap Empty")
            return None

        root = self.heap[0]

        self.size -= 1

        self.heap[0] = self.heap[self.size]

        self.heap[self.size] = None

        index = 0

        # HEAPIFY DOWN

        while True:

            left = (2 * index) + 1

            right = (2 * index) + 2

            largest = index

            if left < self.size:

                if self.heap[left].priority > \
                   self.heap[largest].priority:

                    largest = left

            if right < self.size:

                if self.heap[right].priority > \
                   self.heap[largest].priority:

                    largest = right

            if largest != index:

                temp = self.heap[index]

                self.heap[index] = \
                    self.heap[largest]

                self.heap[largest] = temp

                index = largest

            else:

                break

        return root

    # =====================================================
    # PEEK
    # =====================================================

    def peek(self):

        if self.size == 0:

            return None

        return self.heap[0]

    # =====================================================
    # PRINT HEAP
    # =====================================================

    def print_heap(self):

        print("\nHeap State:")

        if self.size == 0:

            print("Heap Empty")
            return

        for i in range(self.size):

            request = self.heap[i]

            print(
                "[Passenger:",
                request.passenger.passenger_id,
                "| Priority:",
                round(
                    request.priority,
                    2
                ),
                "]"
            )