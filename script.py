from news.parse.db.read import read_all_records
import re

if __name__ == '__main__':
    r = read_all_records('epochtimes2017__1_1000.db')
    for i in r:
        print(3)
        print(i.pretify())
        input()