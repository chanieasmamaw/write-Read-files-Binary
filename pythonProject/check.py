import random

def crashes_half_of_the_time():
    if random.randrange(2):  # Randomly True half of the times
        raise ValueError("Function crashed!")

def main():
    try:
        crashes_half_of_the_time()
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    finally:
        print("Finished")

if __name__ == "__main__":
    main()
