# Password Strength Checker

A beginner-friendly command-line tool written in Python that evaluates the strength of a password and tells you exactly which rules it fails.

> **Note:** This is an educational project built while learning Python. It is not a replacement for a real password manager or a professional security audit.

## Features

- Checks four basic rules and reports the result of each one
- Gives a final rating: **Weak**, **Medium**, or **Strong**
- Lets you test as many passwords as you want in a single session
- Runs fully offline: nothing is stored, logged, or sent anywhere
- No external dependencies, only the Python standard library

## How it works

Each password is checked against four rules. Every rule that is satisfied earns one point.

| Rule | Requirement |
|------|-------------|
| Length | At least 8 characters |
| Digit | At least one number (`0-9`) |
| Uppercase | At least one uppercase letter (`A-Z`) |
| Lowercase | At least one lowercase letter (`a-z`) |

The total score decides the final rating:

| Points | Rating |
|--------|--------|
| 4 | Strong Password |
| 2 or 3 | Medium Password |
| 0 or 1 | Weak Password |

## Requirements

- Python 3.6 or newer

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/echO-sudo-1/password-strength-checker.git
cd password-strength-checker
python main.py
```

On some systems you may need to use `python3` instead of `python`.

### Example session

```text
Password Strength Checker

Enter your password to check its strength: Hello1234
Password meets the minimum length requirement.
Password contains at least one number.
Password contains at least one uppercase letter.
Password contains at least one lowercase letter.
Strong Password

Press Enter to check another password or type 'quit' to exit:

Enter your password to check its strength: hello
Password must be at least 8 characters long.
Password must contain at least one number.
Password must contain at least one uppercase letter.
Password contains at least one lowercase letter.
Weak Password

Press Enter to check another password or type 'quit' to exit:
quit
Exiting Password Strength Checker.
```

## Project structure

```text
password-strength-checker/
├── main.py       # The program
├── README.md     # Project documentation
├── LICENSE       # MIT License
└── .gitignore    # Files excluded from version control
```

## Python concepts practiced

This project was built to practice the following fundamentals:

- Variables and the `input()` / `print()` functions
- Conditional statements: `if`, `elif`, `else`
- `for` loops and `while` loops
- Boolean flags and counters
- String methods: `isdigit()`, `isupper()`, `islower()`
- f-strings and the `len()` function

## Limitations

- Special characters (such as `!`, `@`, `#`) are not checked yet
- The tool does not compare passwords against lists of commonly used passwords
- Length is the only measure of size: a long but predictable password such as `Password123` will still be rated Strong

## Roadmap

- [ ] Check for special characters
- [ ] Detect common passwords such as `Password123`
- [ ] Refactor the code into reusable functions
- [ ] Add automated tests
- [ ] Add a score out of 100 instead of four fixed levels

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
