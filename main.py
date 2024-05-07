from utillity import classuser

def main():
    print("Welcome")
    print("1. Register")
    print("2. Login")
    print('3. Exit')
    while True:
        try:
            choice = input("Enter your choice: ")
            if choice =='1':
                pass
            elif choice =='2':
                pass
            elif choice =='3':
                pass
        except ValueError as e:
            print(f"Invalid Input. {e}")

if __name__ == '__main__':
    main()