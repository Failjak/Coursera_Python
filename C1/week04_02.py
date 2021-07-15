class Value:
    def __get__(self, obj, obj_type):
        return self.new_amount

    def __set__(self, obj, value):
        self.new_amount = (1 - obj.commission) * value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

#
# new_account = Account(0.15)
# new_account.amount = 30
#
# print(new_account.amount)