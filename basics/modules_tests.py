import time
import datetime
from datetime import datetime as dt
import os
import sys

from dateutil.tz import tz


def time_tests():
    print("Number of seconds that have passed since the epoch:", time.time())
    print("String represent of time:", time.ctime())
    print("Struct time:", time.gmtime())
    print("Local time:", time.localtime())
    print("Timestamp:", time.asctime(time.localtime()))


def datetime_tests():
    print("Datetime:", dt.now())
    print("Time:", dt.now(tz=tz.tzlocal()))
    print("Time delta:", datetime.timedelta(days=50, seconds=27,
                                            microseconds=10, milliseconds=29000,
                                            minutes=5, hours=8, weeks=2))


def os_tests():
    print("Os name:", os.name)
    print("Os info:", os.uname())
    print(f"List dir ({os.getcwd()}):\n", "\n".join(map(lambda x: "- " + x, os.listdir())))


def sys_test():
    print("Python interpreter path:", sys.executable)
    print("Coding:", sys.getdefaultencoding())
    print("File system coding:", sys.getfilesystemencoding())
    print("Recursion limit: ", sys.getrecursionlimit())
    sys.setrecursionlimit(2000)  # change recursion limit
    print("Recursion limit: ", sys.getrecursionlimit())
    print("Int info:", sys.int_info)


def main():
    time_tests()
    print()
    datetime_tests()
    print()
    os_tests()
    print()
    sys_test()


if __name__ == "__main__":
    main()
