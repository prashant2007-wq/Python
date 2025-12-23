"""
BankAccount Class - Object-Oriented Programming Example

This module demonstrates OOP concepts including:
- Class definition and object instantiation
- Constructor (__init__)
- Encapsulation (private attributes)
- Methods for accessing and modifying object state
- Docstrings for documentation
"""


class BankAccount:
    """
    A simple BankAccount class to demonstrate OOP concepts.
    
    This class demonstrates:
    - Class and Object definition
    - Constructor (__init__)
    - Encapsulation using private attributes (name mangling with __)
    - Methods for checking balance, depositing, and withdrawing money
    
    Attributes:
        _BankAccount__account_number (int): Private account number (name mangled)
        balance (float): Current account balance
    """

    def __init__(self, account_number: int, balance: float = 0.0) -> None:
        """
        Initialize a BankAccount object.
        
        Args:
            account_number (int): Unique account number
            balance (float): Initial balance (default: 0.0)
        
        Raises:
            ValueError: If account_number is not positive or balance is negative
        """
        if not isinstance(account_number, int) or account_number <= 0:
            raise ValueError("Account number must be a positive integer")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self.__account_number = account_number
        self.balance = balance

    def check_balance(self) -> None:
        """
        Display the account number and current balance.
        
        This method prints the account number and available balance
        to demonstrate encapsulation and method usage.
        """
        print(f"Your account number is: {self.__account_number}")
        print(f"Your available balance is: {self.balance:.2f}")

    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit (must be positive)
        
        Returns:
            bool: True if deposit was successful, False otherwise
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive")
            return False
        
        self.balance += amount
        print(f"Successfully deposited: {amount:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw (must be positive)
        
        Returns:
            bool: True if withdrawal was successful, False otherwise
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
            return False
        
        if amount > self.balance:
            print(f"Error: Insufficient funds. Available balance: {self.balance:.2f}")
            return False
        
        self.balance -= amount
        print(f"Successfully withdrew: {amount:.2f}")
        return True

    def get_account_number(self) -> int:
        """
        Get the account number (demonstrates encapsulation).
        
        Returns:
            int: The account number
        """
        return self.__account_number

    def __repr__(self) -> str:
        """
        Return a string representation of the BankAccount object.
        
        Returns:
            str: String representation showing account number and balance
        """
        return f"BankAccount(account_number={self.__account_number}, balance={self.balance:.2f})"


if __name__ == "__main__":
    # Example usage demonstrating OOP concepts
    print("=== BankAccount OOP Example ===")
    
    # Create a new bank account
    account = BankAccount(281207, 27000)
    
    # Check the account balance
    account.check_balance()
    print()
    
    # Deposit money
    account.deposit(5000)
    print()
    
    # Withdraw money
    account.withdraw(2000)
    print()
    
    # Check balance again
    account.check_balance()
    print()
    
    # Display account information
    print(account)
