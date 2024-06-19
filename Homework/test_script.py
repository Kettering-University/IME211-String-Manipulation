import sys

# Import student's code
import student_code


def test_extract_information():
    correct_date = "2023-05-06"
    correct_error_code = "Error 404"
    correct_message = "Resource not found."
    return (student_code.date == correct_date and
            student_code.error_code == correct_error_code and
            student_code.message == correct_message)


def test_data_cleanup():
    correct_clean_data = "32,14,59,23,72"
    return student_code.clean_data == correct_clean_data


def test_format_output():
    correct_output = "Temperature readings: [23, 27, 25, 29]"
    # We need to ensure the output exactly matches the expected format.
    return student_code.formatted_temperatures == correct_output


def main():
    results = []
    results.append(test_extract_information())
    results.append(test_data_cleanup())
    results.append(test_format_output())

    if all(results):
        sys.exit(0)  # Pass
    else:
        sys.exit(1)  # Fail


if __name__ == "__main__":
    main()
