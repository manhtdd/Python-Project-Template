from .module1.example1 import example1
from .utils.logger import logger

def main():
    example1()
    logger("This is main function")

if __name__ == '__main__':
    main()