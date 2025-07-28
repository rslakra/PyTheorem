#
# Author: Rohtash Lakra
#
import random


class VinGenerator:
    # Valid VIN characters (excluding I, O, Q)
    VIN_CHARS = "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"

    @classmethod
    def randomVINGenerator(cls) -> str:
        """Generates a 17-character alphanumeric string that resembles a VIN."""
        vin = ""
        for _ in range(17):
            vin += random.choice(cls.VIN_CHARS)

        return vin


def main():
    vinGenerator = VinGenerator()
    while True:  # <<
        try:
            how_many = int(input("How many VINs do you want to generate? "))  # <<
            if how_many <= 0:
                print("Please enter a positive number.")  # <<
            else:
                break
        except ValueError:  # <<
            print("Invalid input! Please enter a valid integer.")  # <<

    for i in range(how_many):
        print(vinGenerator.randomVINGenerator())


if __name__ == "__main__":
    main()
