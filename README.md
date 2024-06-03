# Resolution-proof-solver

## Introduction

Resolution-proof-solver is a Python-based tool designed to solve resolution proofs in logic.

## Features

- Parse logical expressions in standard notation
- Apply resolution rules to derive conclusions
- Generate detailed steps of the resolution process

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/mayzelf/Resolution-proof-solver.git
    ```


## Usage

### Interactive Mode

To use the solver in interactive mode, simply run the main script without any arguments:

```bash
python solver.py
```

You'll be prompted to enter a logical expression. The solver will then display the resolution process and the final conclusion.


## Logical Expression Format

The solver uses the following format for logical expressions:

- Negation: `!`
- OR: `or`
- AND: `and`
- Parentheses for grouping: `()`

Example:

```
(!a or b or !c or !d) and (!a or b or !c or d) and (!a or !b or !c) and (a or !b or !c or !d) and (a or b or !c or !d) and (!a or !b) and (a) and (!a or b or c or !d) and (b)
```

## Examples

### Example 1

Given the following expressions:

```
(!a or b or !c or !d) and (!a or b or !c or d) and (!a or !b or !c) and (a or !b or !c or !d) and (a or b or !c or !d) and (!a or !b) and (a) and (!a or b or c or !d) and (b)
```

The solver will output the resolution steps and the final conclusion.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## Contact

For any questions or suggestions, please contact me via Discord: mayzelf or via the Github issues.
