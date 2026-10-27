# Python — ATM Withdrawal Simulator

A small command-line ATM that verifies a PIN, accepts a withdrawal amount, and checks it against a minimum, the account balance and the note denomination before dispensing cash.

---

## Problem Statement

Build an ATM simulator with these rules:

1. The user enters a PIN. If it doesn't match the stored PIN, stop.
2. If the PIN is correct, ask for a withdrawal amount.
3. The amount must be **greater than zero**.
4. The amount must not exceed the balance.
5. The amount must be a multiple of 100 (the smallest note).
6. On success, deduct the amount and show the remaining balance.

**Example**

```
Enter your PIN : 1234
PIN Verified
Enter the amount withdraw : Rs.2500
Withdrawal Successfull
Remaining Balance : Rs. 7500
```

---

## Solution

```python
correct_pin="1234"
balance = 10000

entered_pin=input("Enter your PIN : ")

if entered_pin == correct_pin :
    print("PIN Verified")

    amount=int(input("Enter the amount withdraw : Rs."))

    if amount<=0:
        print("Amount should be greater than zero")

    else :
        if amount<= balance :
            if amount % 100 == 0 :
                balance -= amount
                print("Withdrawal Successfull")
                print("Remaining Balance : Rs.",balance)
            else :
                print("Amount must be in multiple of 100")
        else :
            print("Insufficient Balance")
            print("Current Balance : Rs.",balance)
else :
    print("Incorrect PIN")
```

---

## The Critical Idea

The program is a **chain of gates**. Each gate checks one rule, and the money moves only if every gate passes:

```
PIN correct?  →  amount > 0?  →  amount <= balance?  →  amount % 100 == 0?  →  withdraw
```

The `amount > 0` gate sits **before** the balance check. Without it, a negative amount such as `-100` passes both the balance and the multiple-of-100 checks, and `balance -= amount` would _add_ money to the account.

---

## How the Decision Flow Works

| Gate | Condition                    | If it fails                              |
| ---- | ---------------------------- | ---------------------------------------- |
| 1    | `entered_pin == correct_pin` | "Incorrect PIN"                          |
| 2    | `amount > 0`                 | "Amount should be greater than zero"     |
| 3    | `amount <= balance`          | "Insufficient Balance" + current balance |
| 4    | `amount % 100 == 0`          | "Amount must be in multiple of 100"      |

PIN is stored and compared as a **string**, which preserves leading zeros (`"0420"`). The amount is converted with `int()` because it is used in arithmetic.

---

## Pseudocode

```
read entered_pin
if entered_pin != correct_pin: print error, stop
read amount
if amount <= 0: print error, stop
if amount > balance: print insufficient, stop
if amount % 100 != 0: print denomination error, stop
balance = balance - amount
print success and remaining balance
```

---

## Dry Run

`balance = 10000`

| Input PIN | Amount | Gate that decides | Output                             |
| --------- | ------ | ----------------- | ---------------------------------- |
| 1234      | 2500   | all pass          | Success, balance 7500              |
| 1234      | -100   | gate 2 fails      | Amount should be greater than zero |
| 1234      | 0      | gate 2 fails      | Amount should be greater than zero |
| 1234      | 15000  | gate 3 fails      | Insufficient Balance               |
| 1234      | 550    | gate 4 fails      | Must be multiple of 100            |
| 9999      | any    | gate 1 fails      | Incorrect PIN                      |

---

## Complexity

- **Time:** O(1). A fixed number of comparisons.
- **Space:** O(1). Three variables.

---

## Edge Cases

| Case                            | Behaviour                           |
| ------------------------------- | ----------------------------------- |
| Amount equals balance (`10000`) | Allowed, balance becomes 0          |
| Amount is `0`                   | Rejected by the `amount <= 0` check |
| Negative amount (`-100`)        | Rejected by the `amount <= 0` check |
| Non-numeric amount (`abc`)      | `ValueError` crash from `int()`     |
| PIN with spaces (`" 1234"`)     | Treated as incorrect                |

---

## Code-Quality Notes

- Wrap `int(input(...))` in `try/except ValueError`.
- The nested `else: if ...` can be flattened with `elif` for less indentation.
- Fix the message typo: "Successfull" → "Successful".
- Move the PIN and balance out of the source if this ever grows beyond a demo.

---

## Natural Extension

- Allow **3 PIN attempts** with a `while` loop, then lock the card.
- Add a **menu** loop: check balance, withdraw, deposit, exit.
- Use a **function per action** and a `class Account`.
- Keep a **transaction history** list.

---

## Repository Structure

```
python-practice/
├── atm.py
└── README.md
```

---

## How to Run

```bash
python atm.py
```

---

## Key Concepts

- `if / else` nesting
- Input validation order (reject invalid values first)
- Comparison operators
- Modulo (`%`) for divisibility
- String vs integer input
- Compound assignment (`-=`)

---

## Why This Problem Matters

Real systems validate in layers: authenticate first, then validate the input, then check business rules. The `amount > 0` fix shows why order matters, because one missing check can let a "withdrawal" deposit money. The same pattern appears in login flows, payment checks and API request validation.

---

## Contributing

Suggestions and improvements are welcome. Fork the repo, make your change and open a pull request.

---

## License

This project is open source and available under the MIT License.
