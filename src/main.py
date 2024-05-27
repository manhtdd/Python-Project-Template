from .module1.example1 import example1
from .module2.example2 import example2
from .utils.logger import logger
import cProfile, pstats, io, os

def main():
    # Your main application code here
    example1()
    example2()
    logger("Hello, this is the main application!")
    print("Hello, this is the main application!")

if __name__ == "__main__":
    # Ensure the profiles directory exists
    os.makedirs('profiles', exist_ok=True)

    # Create a profile object
    pr = cProfile.Profile()

    # Enable profiling
    pr.enable()

    # Run the main function
    main()

    # Disable profiling
    pr.disable()

    # Save the raw profile data to a .prof file
    pr.dump_stats('profiles/profile.prof')

    # Create an output stream for the readable profile data
    s = io.StringIO()
    sortby = 'cumulative'

    # Create a Stats object and print the profiling results
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()

    # Save the readable profiling results to a .txt file
    with open('profiles/profile_readable.txt', 'w') as f:
        f.write(s.getvalue())
