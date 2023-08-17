#!/usr/bin/python3
"""Log parsing"""
from sys import stdin

if __name__ == "__main__":

    statusCodes = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}
    totalSize = 0

    def parseLine(line):
        """Parses a line of known format"""
        global totalSize

        try:
            toks = line.rstrip().split(' ')
            totalSize += int(toks[-1])

            if int(toks[-2]) in statusCodes:
                statusCodes[int(toks[-2])] += 1

        except BaseException:
            pass

    def printStats():
        """Prints all current stats"""
        print("File size: {}".format(totalSize))
        for k in sorted(statusCodes.keys()):
            if statusCodes[k]:
                print("{}: {}".format(k, statusCodes[k]))

    lineNb = 1

    try:
        for line in stdin:
            parseLine(line)
            if lineNb % 10 == 0:
                printStats()
            lineNb += 1
    except KeyboardInterrupt:
        printStats()
        raise
    printStats()
