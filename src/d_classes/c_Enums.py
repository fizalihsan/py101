from enum import Enum
# from enum import unique

# @unique
class EmailStatus(Enum):
    EMAIL_INVALID = 'email_invalid'
    DOMAIN_INVALID = 'domain_invalid'
    EMAIL_EXISTS = 'email_exist'
    DOMAIN_EXISTS = 'domain_exist'
    EMAIL_VALID_DOESNT_EXIST = 'valid_not_exist'
    TYPE_REGISTERED = 'registered_emails'
    TYPE_UNREGISTERED = 'unregistered_emails'

    def __str__(self):
        return '{0} = {1}'.format(self.name, self.value)

    def reverse(self):
        return reversed(self.value)

    @staticmethod
    def values():
        for s in EmailStatus:
            print s


print(EmailStatus.TYPE_UNREGISTERED)  # EmailStatus.TYPE_UNREGISTERED
print(EmailStatus.TYPE_UNREGISTERED.name)  # TYPE_UNREGISTERED
print(EmailStatus.TYPE_UNREGISTERED.value)  # unregistered_emails
print(repr(EmailStatus.TYPE_UNREGISTERED))  # <EmailStatus.TYPE_UNREGISTERED: 'unregistered emails'>
print EmailStatus.TYPE_UNREGISTERED == 'unregistered_emails'  # False

for s in EmailStatus:
    print s

print "--------------------"
print EmailStatus.values()
print "~~~~~~~~~~~~~~~~~~~~"
print EmailStatus.TYPE_UNREGISTERED
Animal = Enum('Animal', 'ant bee cat dog')
print Animal
print Animal.ant.value