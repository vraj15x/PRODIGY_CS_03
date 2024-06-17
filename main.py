def check_password_complexity(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(not char.isalnum() for char in password)


    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "STRONG PASSWORD!"
    else:
        feedback = "WEAK PASSWORD!!!\nConsider the following improvements:\n"
        if not length_criteria:
            feedback += "  --> Ensure that the password is at least 8 characters long\n"
        if not uppercase_criteria:
            feedback += "  --> Include at least one Uppercase letter\n"
        if not lowercase_criteria:
            feedback += "  --> Include at least one Lowercase letter\n"
        if not digit_criteria:
            feedback += "  --> Include at least one Digit\n"
        if not special_char_criteria:
            feedback += "  --> Include at least one Special character (!@#$%^&*(),.?\":{}|<>)\n"

        return feedback

def main():
    print("Password Complexity Checker")


    password = input("Enter your Password: ")


    result = check_password_complexity(password)
    print(result)

if __name__ == "__main__":
    main()