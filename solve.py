from Pyro4 import expose
import random

class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers
        print("Inited")

    def solve(self):
        print("Job Started")
        print("Workers %d" % len(self.workers))
        start, end = self.read_input()
        step = (end - start) / len(self.workers)

        mapped = []
        for i in xrange(0, len(self.workers)):
            mapped.append(self.workers[i].find_carmichael_numbers(str(start + i * int(step)), str(start + (i + 1) * int(step))))
        reduced = self.myreduce(mapped)

        self.write_output(reduced)

        print("Job Finished")

    @staticmethod
    @expose
    def gcd(a,b):
        while (b):
            a, b = b, a % b
        return a

    @staticmethod
    @expose
    def is_prime(n):
        if n <= 2:
            return n == 2

        if n % 2 == 0:
            return False

        for divisor in range(3, int(n ** 0.5) + 1, 2):
            if n % divisor == 0:
                return False

        return True

    @staticmethod
    @expose
    def is_Carmichael(n):
        if n <= 2 or n % 2 == 0 or Solver.is_prime(n):
            return False

        for a in range(3, n, 2):
            if Solver.gcd(a, n) == 1:
                if pow(a, n - 1, n) != 1:
                    return False

        return True
   
    @staticmethod
    @expose
    def find_carmichael_numbers(start, end):
        start = int(start)
        end = int(end)
        res = []
        for n in range(start, end):
            if Solver.is_Carmichael(n):
                res.append(str(n))

        return res  

    @staticmethod
    @expose
    def myreduce(mapped):
        print("reduce")
        output = []
        for out in mapped:
            output = output + out.value

        return output

    def read_input(self):
        file = open(self.input_file_name, 'r')
        interval = file.readline()
        interval_parts = interval.split(" ")
        file.close()

        return int(interval_parts[0]), int(interval_parts[1])

    def write_output(self, output):
        file = open(self.output_file_name, 'w')
       #file.write('[\n'))  
        file.write("\n".join(output))
        # file.write(']\n')
        file.close()
        print("output done")