class Scanner(object):
    """class to scan the expression"""
    def __init__(self):
        self.expression = self.scan()

    def scan(self) -> str:
        """
        scan the expression from the user
        :return: the expression as a string
        """
        try:
            print("-------------------------------------------------------------------------------------------------")
            self.expression = input("Enter the expression: ")
        except EOFError:
            print("The program has been terminated.")
            exit()
        except KeyboardInterrupt:
            print("\nThe program has been stopped!")
            exit()
        if self.expression == "exit":
            print("Thank you for using the calculator!")
            exit()
        return self.expression
