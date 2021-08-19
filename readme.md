# Calculate the factorial of all numbers in a date

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple app designed to receive date in the format of `DD/MM/YYYY` and calculate the factorial of sum of all numbers in the date. This app was written as a assignment in SSAD course at Innopolis University.

## Example

Example of usage:

```
python3 main.py
Enter date: 20/05/2020
Factorial of all numbers in date: 11! = 39916800
```

## Installation and usage guide

This app requires python3+ to launch. It comes preinstalled on UNIX systems and MacOS, for Windows installation proceed here: [Download python](https://www.python.org/downloads/).

No libraries other than default is needed.

First, you need to clone this project:

```
git clone https://github.com/zyyyme/factorial-date.git
```

Then, go to the cloned directory and launch application:

```
cd factorial-date
python3 main.py
```

You will get a prompt to enter date: 

```
Enter date: 
```

The date should be in format `DD/MM/YYYY`, otherwise you will get an error:

```
Enter date: 12.31.2004
Date does not match pattern DD/MM/YYYY. Try again.
```

After entering correct date, factorial of sum of all numbers in date will be calculated and printed out:

```
Enter date: 19/08/2021
Factorial of all numbers in date: 23! = 25852016738884976640000
```

## Contributions

Feel free to contribute to this project if you want to. Adding support of other date formats is important for this project, so pull requests with code updates for more date formats are highly appreciated.

## License

As stated in header, it is an [MIT](https://choosealicense.com/licenses/mit/) licensed project, so feel free to use it anywhere, just write me if you want to use it in your project.