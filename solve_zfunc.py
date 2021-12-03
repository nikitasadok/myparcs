# import gmpy2
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
        words = self.read_input()
        step = len(words)/ len(self.workers)

        mapped = []

        for i in xrange(0, len(self.workers)):
            mapped.append(self.workers[i].mymap(words[int(i * step): int(i + 1) * step]))

        reduced = self.myreduce(mapped)

        self.write_output(reduced)

        print("Job Finished")

    @staticmethod
    @expose
    def mymap(arr_chunk):
        z_funcs = []
        for word in arr_chunk:
            n = len(word)
            z = []
            for i in range(n):
                z.append(0)

            for i in range (1, n):
                while (i + z[i] < n and word[z[i]] == word[i + z[i]]):
                    z[i] += 1
            z_funcs.append("".join(str(x) for x in z[:(n-1)]))

        return z_funcs

    @staticmethod
    @expose
    def myreduce(mapped):
        print("reduce")
        output = []
        max_len = 0
        for z_funcs in mapped:
            output.append(z_funcs.value)
        new_out = []

        for i in range(len(output)):
            for j in range(len(output[i])):
                new_out.append(output[i][j] + "\n")

        return new_out

    def read_input(self):
        file = open(self.input_file_name, 'r')
        num_words = int(file.readline())

        words = []
        for i in range(num_words):
            words.append(file.readline())

        file.close()

        return words

    def write_output(self, output):
        file = open(self.output_file_name, 'w')
       #file.write('[\n'))  
        file.write("".join(output))
        # file.write(']\n')
        file.close()
        print("output done")
