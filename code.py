import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Digit check
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    # Strength rating
    ratings = {
        5: "Very Strong ",
        4: "Strong ",
        3: "Moderate ",
        2: "Weak ⚠️",
        1: "Very Weak ",
        0: "Extremely Weak "
    }

    print(f"\nPassword Strength: {ratings[strength]}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(f"- {tip}")

# Interactive prompt
if __name__ == "__main__":
    print("=== Password Strength Checker ===")
    user_password = input("Enter your password: ")
    check_password_strength(user_password)
