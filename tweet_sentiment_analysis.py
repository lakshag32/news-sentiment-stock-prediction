#https://remarkablemark.org/blog/2020/08/26/python-iterate-csv-rows/
#https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
import csv

filename = 'tweets2.csv'
tweets = []

with open(filename, 'r',encoding="utf8") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        tweets.append(row[1])

print(len(tweets))
print(len(list(set(tweets))))