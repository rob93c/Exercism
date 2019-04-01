public class BankAccount {

	private int account = 0;
	private boolean isOpen;

	public synchronized void open() {
		isOpen = true;
	}	

	public synchronized void close() {
		isOpen = false;
	}

	public synchronized void deposit(int dep) throws BankAccountActionInvalidException {
		if(!isOpen) {
			throw new BankAccountActionInvalidException("Account closed");
		} else if (dep < 0) {
			throw new BankAccountActionInvalidException("Cannot deposit or withdraw negative amount");
		} else account += dep;
	}

	public synchronized void withdraw(int wit) throws BankAccountActionInvalidException {
		if (!isOpen) {
			throw new BankAccountActionInvalidException("Account closed");
		} else if (account == 0) {
			throw new BankAccountActionInvalidException("Cannot withdraw money from an empty account");
		} else if (account < wit && wit >= 0) {
			throw new BankAccountActionInvalidException("Cannot withdraw more money than is currently in the account");
		} else if (wit < 0) {
			throw new BankAccountActionInvalidException("Cannot deposit or withdraw negative amount");
		} else {
			account -= wit;
		}
	}

	public synchronized int getBalance() throws BankAccountActionInvalidException {
		if (!isOpen) {
			throw new BankAccountActionInvalidException("Account closed");
		} else {
			return account;
		}
	}
}
