import datetime
import time
class Time:
    def get_time(self):
        start_time = int(time.time())
        time.sleep(10)
        end_time = int(time.time())
        total_time = end_time-start_time
        print(total_time)
        # time.sleep(10)
        # end_time = datetime.datetime.now()

# time.sleep(5)
# end_time = datetime.datetime
# total_time = end_time-start_time
# print(total_time)

if __name__ == '__main__':
    T = Time()
    T.get_time()