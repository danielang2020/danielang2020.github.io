> [Forward references](https://peps.python.org/pep-0484/#forward-references)

> [Unpacking Operators in Python](https://towardsdatascience.com/unpacking-operators-in-python-306ae44cd480)
>> \* = tuple ** = dict

> [list/set/dict comprehension](https://towardsdatascience.com/comprehending-the-concept-of-comprehensions-in-python-c9dafce5111)

> [position only argument vs keyword only argument](https://stackoverflow.com/questions/9450656/positional-argument-v-s-keyword-argument)
>> def incr(x):            -> incr(3.8),incr(x=3.8)
>> def incr1(x,/):         -> incr1(3.8) / incr1(x=3.8)
>> def incr2(x,/,y):       -> incr2(1,2),incr2(1,y=2)/ incr2(x=1,y=2)
>> def incr3(x,/,*,y):     -> incr3(1,y=2) / incr3(1,2)

> Threading and asyncio both run on a single processor and therefore only run one at a time.   
> [python-concurrency](https://realpython.com/python-concurrency/)