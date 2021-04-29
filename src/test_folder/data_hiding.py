# class JustCounter:
#
#    __secretCount = 0
#    non_hidden = 5
#
#    def count(self):
#
#       self.__secretCount += 1
#
#       print(self.__secretCount)
#
# counter = JustCounter()
#
# counter.count()
#
# counter.count()
#
# print(counter.non_hidden)
# print(counter.__secretCount)


class Encrypt:
    __encryption_factor = 5
    
    def send_message(self, number):
        print("Encrypted message is : ", number * self.__encryption_factor)
        return number * self.__encryption_factor
    
    def read_message(self, number):
        print("Actual message is : ", int(number / self.__encryption_factor))


my_enc_obj = Encrypt()

message_recieved = my_enc_obj.send_message(7)
print("Message Recieved : ", message_recieved)

my_enc_obj.read_message(message_recieved)


