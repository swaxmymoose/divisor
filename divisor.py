#!/usr/bin/python3
import argparse
import sys
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-names', '--n', nargs='+', help='contributor names')
    parser.add_argument('-contributions', '--c', nargs='+', required=True, help='peoples contribution')
    #parser.add_argument('-units', '--u', help='units')
    #parser.add_argument('-presision', '--p', help='precision')
    parser.add_argument('-prize', '--r', help="prize", required=True)
    #parser.add_argument('--v', '--verbose', action='store_true', help='increase output verbosity')
    args = parser.parse_args()
    calculate(args)

def calculate(args):
    float_array = np.array(args.c,dtype=float)
    total = np.sum(float_array)
    if args.n:
        if len(args.n) != len(args.c):
            print("Error: the number of people names needs to equal the number of different contributions")
            return
        else:
            num_people = len(args.n)
            names_array = np.array(args.n)
            for contribution, name in zip(float_array, names_array):
                print(name + " gets " + str(round((contribution/total) * float(args.r), 2)))

    else:
        for contribution in float_array:
            print(round((contribution/total) * float(args.r), 2))

main()
    
