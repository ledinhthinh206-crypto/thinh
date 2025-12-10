class Bank:
    Account_type = "Savings"
    location = "Guntur"
    CORRECT_PIN = 123

    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance

    def __repr__(self):
        # Chỉ dùng để hiển thị thông tin cơ bản của tài khoản (như thẻ)
        return f"ATM Account for {self.name} (A/C: *******{str(self.Account_Number)[-4:]})"

    def run_atm(self):
        """Khởi động quy trình ATM"""
        print("Welcome to the SBI ATM Machine")
        print("------------------------------")
        
        if self._authenticate():
            self._main_menu()
        else:
            print("❌ Account locked due to multiple incorrect PIN attempts.")

    def _authenticate(self, attempts=3):
        """Xác thực PIN với số lần thử giới hạn"""
        for i in range(attempts):
            try:
                account_pin = int(input("Please enter your pin number: "))
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")
                continue

            if account_pin == self.CORRECT_PIN:
                print("✅ Authentication successful.")
                return True
            else:
                print(f"❌ Pin Incorrect. Please try again. ({attempts - 1 - i} attempts remaining)")
        return False

    def _main_menu(self):
        """Hiển thị menu và xử lý giao dịch"""
        print(f"\nYour Card Number is:XXXX XXXX XXXX {str(self.Account_Number)[-4:]}")
        is_running = True
        
        while is_running:
            print("\n--- TRANSACTION MENU ---")
            print("1) Balance")
            print("2) Withdraw")
            print("3) Deposit")
            print("4) Quit")
            
            try:
                option = int(input("Please enter your choice: "))
            except ValueError:
                print("⚠️ Invalid choice. Please enter a number (1-4).")
                continue

            if option == 1:
                self.Balance()
            elif option == 2:
                self.Withdraw()
            elif option == 3:
                self.Deposit()
            elif option == 4:
                self.Exit()
                is_running = False
            else:
                print("⚠️ Invalid option. Please choose 1, 2, 3, or 4.")

    def Balance(self):
        """Kiểm tra số dư"""
        print(f"\n--- BALANCE ---")
        print(f"Your current balance is: *{self.balance}*")

    def Withdraw(self):
        """Thực hiện rút tiền"""
        try:
            w = int(input("Please Enter Desired amount: "))
        except ValueError:
            print("⚠️ Invalid input. Please enter a numerical amount.")
            return

        if w > 0 and self.balance >= w:
            self.balance -= w
            print("✅ Your transaction is successful!")
            print(f"Your New Balance: *{self.balance}*")
        else:
            print("❌ Your transaction is cancelled.")
            print("Reason: Amount is not sufficient in your account or invalid amount.")

    def Deposit(self):
        """Thực hiện nạp tiền"""
        try:
            d = int(input("Please Enter Desired amount: "))
        except ValueError:
            print("⚠️ Invalid input. Please enter a numerical amount.")
            return
        
        if d > 0:
            self.balance += d
            print("✅ Your transaction is successful!")
            print(f"New Balance: *{self.balance}*")
        else:
            print("❌ Deposit amount must be positive.")
            
    def Exit(self):
        """Thoát khỏi chương trình"""
        print("\n👋 Thank you for using the SBI ATM. Goodbye!")

# --- EXAMPLE USAGE ---
t1 = Bank("Mahesh", 1453210145, 5000)

# Khởi chạy chương trình ATM (thay vì dùng print(t1))
t1.run_atm()
