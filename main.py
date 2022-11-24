from scanner import *
from handler import *


def main():
    while True:
        try:
            s = Scanner()
            Handler(s.exercise)
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nThe program has been stopped!")
            break
        except EOFError:
            print("The program has been stopped!")
            break


if __name__ == '__main__':
    main()
