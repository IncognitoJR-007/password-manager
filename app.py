from password_manager import PasswordManager
from password_strength import check_password_strength
from two_factor_auth import send_2fa_code, verify_2fa_code

def main():
    manager = PasswordManager()

    print("Welcome to the Password Manager!")
    
    # Two-factor authentication
    email = input("Enter your email for 2FA: ")
    code = send_2fa_code(email)
    user_code = input("Enter the 2FA code sent to your email: ")
    
    if not verify_2fa_code(code, user_code):
        print("Invalid 2FA code.")
        return
    
    while True:
        print("\nOptions:")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Generate a strong password")
        print("4. Check password strength")
        print("5. Quit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            site = input("Enter the site name: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            manager.add_password(site, username, password)
            print("Password added successfully!")

        elif choice == "2":
            site = input("Enter the site name: ")
            data = manager.retrieve_password(site)
            if data:
                print(f"Username: {data['username']}, Password: {data['password']}")
            else:
                print("No password found for this site.")

        elif choice == "3":
            length = int(input("Enter the desired length for the password: "))
            generated_password = manager.generate_password(length)
            print(f"Generated Password: {generated_password}")

        elif choice == "4":
            password = input("Enter the password to check: ")
            strength = check_password_strength(password)
            print(f"Password Strength: {strength}")

        elif choice == "5":
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
