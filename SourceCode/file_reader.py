def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Error: file not found."

def main():
    print("File Reader")
    filename = input("Enter the file name to read: ")
    content = read_file(filename)
    print("\nFile Contents:\n")
    print(content)

if __name__ == "__main__":
    main()
