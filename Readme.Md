# Python-Package

## Installation
```bash
pip install techyshiv-evenodd
```

## what it does
    This Basically Provide you to get easier whenever you are facing such problems where you have to find the even and odd numbers.
    This Modules Helps,you to find whether the given number is even and odd or you can also pass a list to this function and get the desired list for even & odd numbers.

## Supported Data-Typs
    Integer
    String
    List

## How to use it
```python
import techyshiv_evenodd as evenodd
params = evenodd.EvenOdd(data=2)
params.checkEven() # Output - True
params.checkOdd()  # Output - False

params = evenodd.EvenOdd(data="2")
params.checkEven() # Output - True
params.checkOdd()  # Output - False

params = evenodd.EvenOdd(data=[10,20,30,1,19,40])
params.checkEven() # Output - [10,20,30,40]
params.checkOdd()  # Output - [1,19]
```

## License
    © 2022 Shivang Saxena
    This repository is licensed under the MIT license. See LICENSE for details.