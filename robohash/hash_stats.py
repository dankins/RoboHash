import sys

class HashStats:
    collisions = 0
    count = 0
    requests = 0
    resizes = 0
    seeks = 0

    def pretty_print(self):
        print "Count: " + str(self.count) + " \n" + \
            "Requests: " + str(self.requests) + " \n" + \
            "Seeks: " + str(self.seeks) + " \n" + \
            "Resizes: " + str(self.resizes) + " \n" + \
            "Collisions: " + str(self.collisions) + " \n"

    def increment_count(self):
        # do nothing
        self.count += 1

    def increment_requests(self):
        self.requests += 1

    def increment_seeks(self):
        self.seeks += 1

    def increment_collisions(self):
        self.collisions += 1

    def increment_resizes(self):
        self.resizes += 1