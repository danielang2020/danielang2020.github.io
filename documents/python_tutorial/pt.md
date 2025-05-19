# The Python Tutoria
## 3. An Informal Introduction to Python
### 3.1. Using Python as a Calculator
#### 3.1.1. Numbers
> Division(/) always returns a float. To do floor division and get an integer result you can use the // operator; to calculate the remainder you ca use %:
```python
17 // 3 # = 5
```

> With python, it is possible to use the ** operator to calculate powers:
```python
5 ** 2 # = 25
```

> In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations.
```python
tax = 12.5 / 100
price = 100.50
price * tax # = 12.5625
price + _ # = 113.0625
round(_,2) # = 113.06
```