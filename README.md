Object Oriented Programming with Python

https://www.youtube.com/watch?v=Ej_02ICOIgs&ab_channel=freeCodeCamp.org

### Notes

* Classes should have the first letter as a capital
* anything that starts with `__` is called a "magic method"
* you can assign value to parm by given a default value `def __init__(self, name, price, qty=0):`
* to force a data type use `:` after varible name example `def __init__(self, name: str, price: float, qty=0):`
    * fact that we have assigned a default value of an int in `qty` tells python the date type it must use
* assert keyword check what is happening to your expectations
* asserts allow you to add better error handling easily
* Class attributes are shared belongs to the class itself
* instance attribute are only for the instance of that class
* `__dict__` all the attribute for Class level and instance level. This is useful for debugging
* `__repr__` is a magic method - representing your objects
    * it is best practise to name the items the same format as when you call the class return `f"Item('{self.name}, {self.price}, {self.qty}')"` = `Item('Phone', 100, 5)`
    * a special method used to represent a class's objects as a string.
* ![image](https://user-images.githubusercontent.com/32961611/193047084-6c902c74-5850-4e30-be5d-d94d067e205f.png)
* `@classmethod` using this converts function into a class method
* `cls` loads the class itself
* static mehtod should do some work for you that has some logical connection to a class
    * a static method is bound to a class rather than the objects for that class
* Parent and child classes
* ![image](https://user-images.githubusercontent.com/32961611/193412181-c67a773a-7722-4ced-9f44-a3c6fc332739.png)
* super functions allows us to use functionality from parent class
* `self.__class__.__name__` allows you to see the name of the class in a parent child situation
* Encapsulation - describes the concept of bundling data and methods within a single unit
* Decorators are like another function that you pre execute before another function
* Puttig 2 `__` infornt of a variable or attribute makes it a "private" atrribute
* `@property` decorator makes things read only
* 
* 



