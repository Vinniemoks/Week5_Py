def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            lines = ["First line\n", "Second line\n", "12345\n"]
            file.writelines(lines)
        print("File created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
    finally:
        pass

def read_and_display_file():
    try:
        # Read the contents of "my_file.txt"
        with open("my_file.txt", "r") as file:
            # Display the contents on the console
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        pass

def append_to_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            lines = ["Fourth line\n", "Fifth line\n", "67890\n"]
            file.writelines(lines)
        print("Content appended to the file.")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        pass

# Main function to execute the tasks
def main():
    create_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()
