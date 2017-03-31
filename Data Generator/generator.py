import csv
import random
import string

num_columns = 4
num_rows = 1000

def random_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2))

with open('sim_data.csv', 'w+') as f:
    w = csv.writer(f)
#     w.writerow([random_string() for x in xrange(num_columns+1)])
    for x in xrange(num_rows):
        w.writerow([x+1]+[random.randint(0,4) for r in xrange(num_columns)])
