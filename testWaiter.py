#!/usr/bin/env python

import unittest
from waiter import Waiter


class TestWaiter(unittest.TestCase):

    def testPrime(self):
        self.assertTrue(Waiter.isPrime(5))

    def testNotPrime(self):
        self.assertFalse(Waiter.isPrime(4))

    def testWaiterOK(self):
        iterations = "27 9"
        numbers = "27 17 60 38 67 90 4 43 74 17 25 16 26 51 78 23 58 63 84 41 3 73 12 50 66 60 33 57 27 35 73 59 34 69 \
        31 88 19 12 70 46 18 32 75 89 63 28 77 47 20 44 47 17 32 2 88 5 30 66 83 77 2 51 80 34 37 68 77 90 80 64 41 35 \
        86 70 86 17 39 55 22 42 76 39 7 51 56"
        waiter = Waiter(iterations, numbers)
        piles = waiter.stackPiles()

        expectedResult = "60 38 90 4 74 16 26 78 58 84 12 50 66 60 34 88 12 70 46 18 32 28 20 44 32 2 88 30 66 2 80 34 \
        68 90 80 64 86 70 86 22 42 76 56 51 39 39 51 63 75 69 27 57 33 3 63 51 27 25 35 5 35 55 7 77 77 77 17 17 17 17 \
        19 23 67 43 41 73 73 59 31 89 47 47 83 37 41"
        platesResult = list(map(int, expectedResult.split()))   # Convert the expected result in a list of integers
        counterPlate = 0    # Counter for iterate the expected values list
        for pile in piles:
            for plate in pile:
                self.assertEqual(plate, platesResult[counterPlate])
                counterPlate += 1

    def testWaiterFirstArgumentNotOK(self):
        iterations = "10 e"
        numbers = "27 17 60 38 67 86 70 86 17 39"
        waiter = Waiter(iterations, numbers)
        piles = waiter.stackPiles()
        self.assertEqual(-1, piles)

    def testWaiterSecondArgumentNotOK(self):
        iterations = "10 9"
        numbers = "27 error 55 22 42 76 39 7 51 56"
        waiter = Waiter(iterations, numbers)
        piles = waiter.stackPiles()
        self.assertEqual(-1, piles)

    def testWaiterNInvalidUpper(self):
        iterations = "50001 9"
        numbers = "27 3 55 22 42 76 39 7 51 56"
        waiter = Waiter(iterations, numbers)
        piles = waiter.stackPiles()
        self.assertEqual(-1, piles)

    def testWaiterNInvalidLower(self):
        iterations = "0 9"
        numbers = "27 3 55 22 42 76 39 7 51 56"
        waiter = Waiter(iterations, numbers)
        piles = waiter.stackPiles()
        self.assertEqual(-1, piles)

    def testWaiterQInvalidUpper(self):
        iterations = "10 1201"
        numbers = "27 3 55 22 42 76 39 7 51 56"
        waiter = Waiter(iterations, numbers)
        piles = waiter.stackPiles()
        self.assertEqual(-1, piles)

    def testWaiterQInvalidLower(self):
        iterations = "10 0"
        numbers = "27 3 55 22 42 76 39 7 51 56"
        waiter = Waiter(iterations, numbers)
        piles = waiter.stackPiles()
        self.assertEqual(-1, piles)

    def testWaiterNumberInvalidUpper(self):
        iterations = "10 2"
        numbers = "10001 3 55 22 42 76 39 7 51 56"
        waiter = Waiter(iterations, numbers)
        piles = waiter.stackPiles()
        self.assertEqual(-1, piles)

    def testWaiterNumberInvalidLower(self):
        iterations = "10 2"
        numbers = "1 3 55 22 42 76 39 7 51 56"
        waiter = Waiter(iterations, numbers)
        piles = waiter.stackPiles()
        self.assertEqual(-1, piles)

if __name__ == '__main__':
    unittest.main()
