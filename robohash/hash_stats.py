
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

    def print_distribution(self, storage, buckets):
        storage_size = len(storage)
        bucket_size = storage_size / buckets
        elements = [0 for _ in range(buckets+1)]

        current_bucket = 0
        for i in range(0, storage_size-1):
            if i > (current_bucket + 1) * bucket_size:
                current_bucket += 1

            if storage[i] is not None:
                elements[current_bucket] += 1

        for i in range(0, buckets):
            print(
                "[" + str(bucket_size*i) + " - " + str(bucket_size*(i+1)) + "] : " +
                str(elements[i]) + " elements | " +
                "%1.1f" % ((elements[i]*1.0/bucket_size)*100.0) + "% filled")
                #str({:.2f}.format((elements[i]/bucket_size)*100) + "% filled")




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