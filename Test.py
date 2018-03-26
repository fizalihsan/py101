# import json
#
# data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
# print 'DATA:', repr(data)
#
# data_string = json.dumps(data, indent=4, sort_keys=True)
# print 'JSON:', data_string


def greet(*args):
    print "{0}".format(args)


greet("Hello", "Nags", "Senthil", "Kumar", "Fizal", "Mohamed")


class Employee:
    """
    This encapsulates all the details of an employee
    """

    def __init__(self, first_name, last_name, emp_id):
        self.first = first_name
        self.last = last_name
        self.id = emp_id

    def print_name(self):
        print "{0} {1}".format(self.first, self.last)

    @classmethod
    def whereami(cls):
        print "I'm in class {0}".format(cls.__doc__)


    @staticmethod
    def run_me(fn, *r):
        def blah():
            return "Done"
        print fn(*r)
        return blah

emp = Employee('Nags', 'Sedhuraman', 123)
emp = Employee(last_name='Sedhuraman', emp_id=123, first_name='Nags')
emp.print_name()  # Employee.print(emp)
Employee.print_name(emp)
print emp.first
Employee.whereami()

print Employee.run_me(lambda r: 3.14 * r * r, 4)()
Employee.run_me(lambda b, h: b * h, 4, 5)()
