import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randrange(begin, end + 1, 1)

def main():

    random = gen_random(15, 1, 5)
    for i in random:
        print(i, end = " ")

if __name__ == "__main__":
    main()