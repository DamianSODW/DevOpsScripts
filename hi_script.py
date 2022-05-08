#!/usr/bin/env python3
"""
Simple utility for command line
"""
import sys


def say_it(greeting, target):
    # message = f"{greeting} {target}"
    # print(message)
    print(f'{greeting} {target}')


if __name__ == '__main__':
    greeting = 'Hello'
    target = 'Joe'

    if '--help' in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
        print(help_message)
        sys.exit()  # Exit from program

    if '--name' in sys.argv:
        # Выясняем позицию значения, следующего за флагом name
        name_index = sys.argv.index('--name') + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if '--greeting' in sys.argv:
        # Выясняем позицию значения, следующего за флагом greeting
        greeting_index = sys.argv.index('--greeting') + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    say_it(greeting, name)
