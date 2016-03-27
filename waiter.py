#!/usr/bin/env python


class Waiter(object):
    def __init__(self, iterations, numbers):
        self.__N = ""
        self.__Q = ""
        self.__pile = []
        self.__iterations = iterations
        self.__numbers = numbers

    @staticmethod
    def isPrime(number):
        """
        Check if the given number is prime.
        :param number: Number to check.
        :return: True if the number is prime and False otherwise.
        """
        prime = False

        # Check valid numbers
        if number > 1:
            # Check for factors
            for iterator in range(2, number):
                if (number % iterator) == 0:
                    break                       # Number is not prime
            else:
                prime = True
        return prime

    def __formatIterations(self, iterations):
        """
        Format the variables N and Q
        :param iterations: String that will be split in two integer values
        :return: 0 if the process is correct, and -1 otherwise.
        """
        try:
            self.__N, self.__Q = map(int, iterations.split())    # Split string in two elements and converted to integer
        except ValueError:
            print("Not valid arguments")                         # Capture the exception
            return -1

        # Check input ranges
        if (self.__N > 50000) or (self.__N < 1) or (self.__Q > 1200) or (self.__Q < 1):
            return -1
        else:
            return 0

    def __formatPile(self, pile):
        """
        Format the value of the plates
        :param pile: String of numbers
        :return: 0 if the process is correct, and -1 otherwise.
        """
        try:
            pileList = pile.split()                             # Split string in N elements
            # self.__pile = list(map(int, pile.split()))
            for element in pileList:
                number = int(element)                           # Try to convert element to integer

                # Check input ranges
                if (number >= 2) and (number <= 10000):
                    self.__pile.append(number)
                else:
                    return -1
        except ValueError:
            print("Not valid pile")                              # Capture the exception
            return -1
        return 0

    def stackPiles(self):
        """
        Stack the plates on different piles
        :param Q: Number of iterations
        :param pile: Input pile
        :return: A list with the piles
        """
        P = 2                                                       # Initial prime number
        piles = []                                                  # List where the different piles will be stacked
        firstArgument = self.__formatIterations(self.__iterations)  # Try convert the first argument to a valid input
        secondArgument = self.__formatPile(self.__numbers)          # Try convert the second argument to a valid input

        # Check if the arguments are valid
        if (firstArgument != -1) and (secondArgument != -1):
            self.__pile.reverse()                                   # The leftmost plate is on the top of the pile

            # Iterations
            for iteration in range(0, self.__Q):
                divisible = []                                      # List of divisible numbers
                noDivisible = []                                    # List of non-divisible numbers

                # Check if P is prime. If P is not prime, it will search the following prime
                while not Waiter.isPrime(P):
                    P += 1

                # Check if the number of the plate on a pile is divisible by the P number.
                # The plate will be appended to the correct pile.
                for plate in self.__pile:
                    if (plate % P) == 0:
                        divisible.append(plate)
                    else:
                        noDivisible.append(plate)
                P += 1                                   # Increment the prime number for the next iteration

                # Check if there are divisible plates in this iteration.
                if len(divisible) > 0:
                    divisible.reverse()                  # The leftmost plate is on the top of the pile
                    piles.append(divisible)              # Append divisible plates to the piles list

                # Check if there are non-divisible plates in this iteration.
                if len(noDivisible) > 0:
                    if iteration == self.__Q:            # Check if it is the last iteration to clear the pile
                        self.__pile.clear()
                    else:
                        noDivisible.reverse()            # The leftmost plate is on the top of the pile
                        self.__pile = list(noDivisible)  # The next pile to check is the non-divisible list
                else:
                    self.__pile.clear()                  # If there are no non-divisible plates, the pile will be cleared

            # The rest of the plates are appended to the pile list.
            if len(self.__pile) > 0:
                piles.append(self.__pile)

            return piles

        # Arguments are invalid
        else:
            return -1


if __name__ == '__main__':
    # Get arguments from input
    iterations = input()
    numbers = input()

    waiter = Waiter(iterations, numbers)    # Instantiate the object
    piles = waiter.stackPiles()             # Call the method

    if (piles != -1):
        # Print all plates in every pile in the asked order.
        for pile in piles:
            for plate in pile:
                print(plate)
