"""
Below, you'll find a class definition for animals. Create two new animals `cat`
and `dog`. Set `cat` to have a name of "Purrfect", kind of "cat",
and color of "brown". Set `dog` to have a name of "Fido",
kind of "dog", and color of "black".
"""
class Animal:
    name = ""
    kind = ""
    color = ""
    
    def description(self):
        return "%s is a %s %s." % (self.name, self.color, self.kind)

# Create instances of Animal here and modify the instance attributes
# as described above.

# YOUR CODE HERE
cat = Animal()
dog = Animal()

cat.kind = "cat"
dog.kind = "dog"

cat.name = "Purrfect"
dog.name = "Fido"

cat.color = "brown"
dog.color = "black"


# Should print Purrfect is a brown cat.
print(cat.description())
# Should print Fido is a black dog.
print(dog.description())
