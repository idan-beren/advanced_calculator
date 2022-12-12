from calculator import *


def main():
    while True:
        try:
            Calculator()
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
