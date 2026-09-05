def calculate_average(numbers):
    """Return the average of a non-empty sequence of numbers.

    If numbers is None or empty, return 0.
    """
    if not numbers:
        return 0

    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1

    return total / count

def process_data(data):
    """Process a sequence of numbers by calculating and printing its average.

    If an error occurs during processing, print a simple error message.
    """
    try:
        result = calculate_average(data)
        print(f"Average: {result}")
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50, 100]
    process_data(sample_data)