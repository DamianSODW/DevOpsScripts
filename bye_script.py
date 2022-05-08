#!/usr/bin/env python3
"""
Simple utility for command line
"""
import sys

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo your input')
    parser.add_argument('message',
                        help='Message to echo')

    parser.add_argument('--twice', '-t',
                        help='Do it twice',   # Unnecessary flag
                        action='store_true')  # Default value

    args = parser.parse_args()

    print(args.message)
    if args.twice:
        print(args.message)
