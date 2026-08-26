def convert_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    print("Grade Converter")
    score = float(input("Enter the numeric score (0-100): "))
    letter = convert_grade(score)
    print("Letter Grade:", letter)

if __name__ == "__main__":
    main()
