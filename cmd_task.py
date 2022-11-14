import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--string', action='store_const', const='1')
#parser.add_argument('-1', '--one', help='This will be option One')
#parser.add_argument('two', help='This will be option two')

print(parser.parse_args())
if parser.parse_args().string == '1':
    print("Its my string")


