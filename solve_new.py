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
        num_words = self.read_input()
        step = num_words/ len(self.workers)

        mapped = []

        for i in xrange(0, len(self.workers)):
            mapped.append(self.workers[i].mymap(step))

        reduced = self.myreduce(mapped)

        self.write_output(reduced)

        print("Job Finished")

    @staticmethod
    @expose
    def mymap(step):
        strs = []
        n = 50
        for i in range(step):
            s = ''
            for j in range(random.randint(6, n)):
                letter = random.randint(65, 123)
                s += str(chr(letter))
            strs.append(s)
        
        max_len = 0
        longest_words = []
        for word in strs:
            if len(word) > max_len:
                max_len = len(word)

        for word in strs:
            if len(word) == max_len:
                longest_words.append(word)

        return longest_words

    @staticmethod
    @expose
    def myreduce(mapped):
        print("reduce")
        output = []
        max_len = 0
        for words in mapped:
            print("reduce loop one")
            if len(words.value[0]) > max_len:
                max_len = len(words.value[0])

        for words in mapped:
            print("reduce loop two")
            if len(words.value[0]) == max_len:
                output.append(words.value[0])
                return output
            
        print("reduce done")
        return output

    def read_input(self):
        file = open(self.input_file_name, 'r')
        num_words = int(file.readline())
        file.close()

        return num_words

    def write_output(self, output):
        file = open(self.output_file_name, 'w')
       # file.write('[\n')
        file.write("".join(output))
        # file.write(']\n')
        file.close()
        print("output done")
