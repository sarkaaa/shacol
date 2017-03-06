from __future__ import division
from __future__ import print_function
# !/usr/bin/env python
# requirments - guppy, redis

from future import standard_library

standard_library.install_aliases()
from builtins import input
from builtins import str
from builtins import range
from builtins import object
from past.utils import old_div
import os
import sys
import time
import timeit
# import queue
import hashlib
import argparse
import threading
import linecache
# from sets import Set
# from guppy import hpy
from io import StringIO
import redis
import binascii


class Shacol(object):
    def __init__(self, sha256, bits, inputFile, hashGroup=False, text=False, first=False):
        self.sha256 = sha256
        self.bits = int(bits)
        self.inputFile = inputFile
        self.hashGroup = hashGroup
        self.text = text
        self.first = first

        self.hashPartLength = old_div(int(self.bits), 4)
        self.shaList = []
        self.hashPart = str()

        with open(self.inputFile, 'r', encoding='utf-8') as dataFromFile:
            if self.hashGroup:
                if self.sha256:
                    if self.text:
                        for textInFile in dataFromFile:
                            self.shaList.append(hashlib.sha256(textInFile).hexdigest()[0:self.hashPartLength])
                    else:
                        for hashInFile in dataFromFile:
                            self.shaList.append(hashInFile[0:self.hashPartLength])
            else:
                if sha256:
                    if self.text:
                        self.hashPart = hashlib.sha256(dataFromFile.read()).hexdigest()[0:self.hashPartLength]
                    else:
                        self.hashPart = dataFromFile.readline()[0:self.hashPartLength]
        dataFromFile.close()

    """ Ready for threading - not be real with set (just with a slower database using
        low RAM consumption)
    if (len(sha256) % hashPartLength == 0): #seperation of hash to n-bits blocks
        hashPart = [sha256[i:i+hashPartLength] for i in range(0, len(sha256), hashPartLength)]
    else:
        print 'Badly aliquot bit value! Use only the power of two... '
    """

    def getInfo(self):
        printHashes = str()
        for i in self.shaList:
            printHashes += i + '\t'
        # print absolute path to input file
        print('\nYou are trying to find a collision with %s hash for %db with SHA-2.\n' %
              ('first' if self.first else 'arbitary', self.bits) +
              'Using %s as input file with %s.' %
              (self.inputFile,
               'one hash inside' if not self.hashGroup else 'with one hash per line inside.') +
              '\nInput %s %s' % ('hash is  '
                                 if not self.hashGroup else 'hashes are ',
                                 self.hashPart if not self.hashGroup else printHashes))

    def changeBitLength(self, newBitLength):
        self.bits = newBitLength
        self.hashPartLength = old_div(self.bits, 4)

    def hashToBits(self, hashPart):
        bits = bin(int(binascii.hexlify(hashPart.encode('utf-8', 'surrogatepass')), 16))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

    def hashFromBits(self, bitHash):
        n = int(bitHash, 2)
        return self.intToBytes(n).decode('utf-8', 'surrogatepass')

    def intToBytes(self, i):
        hex_string = '%x' % i
        n = len(hex_string)
        return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

    def findCollisionFast(self, hashPart=None):
        """
        Best performance function - high RAM load
        """
        try:
            if not hashPart:
                hashPart = self.hashPart
                hashPartLength = self.hashPartLength
            else:
                hashPartLength = len(hashPart)

            newHashPart = hashPart
            count = 0
            print('\nInput hashPart:', hashPart)
            hashPartSet = set()
            hashPartSet2 = set()
            hashPartSet3 = set()
            hashPartSet4 = set()
            hashPartSet5 = set()
            hashPartSet6 = set()
            hashPartSet7 = set()
            hashPartSet8 = set()
            hashPartSet9 = set()
            hashPartSet10 = set()
            hashPartSet11 = set()
            hashPartSet12 = set()
            hashPartSet13 = set()
            hashPartSet14 = set()
            hashPartSet15 = set()
            hashPartSet16 = set()
            hashPartSet17 = set()
            hashPartSet18 = set()
            hashPartSet19 = set()
            hashPartSet20 = set()
            hashPartSet21 = set()
            hashPartSet22 = set()
            hashPartSet23 = set()
            hashPartSet24 = set()
            hashPartSet25 = set()
            hashPartSet26 = set()
            hashPartSet27 = set()
            hashPartSet28 = set()
            hashPartSet29 = set()
            hashPartSet30 = set()
            hashPartSet31 = set()
            hashPartSet32 = set()
            hashPartSet33 = set()
            hashPartSet34 = set()
            hashPartSet35 = set()
            hashPartSet36 = set()
            hashPartSet37 = set()
            hashPartSet38 = set()
            hashPartSet39 = set()
            hashPartSet40 = set()

            startTime = time.time()
            while newHashPart not in (hashPartSet or hashPartSet2 or hashPartSet3 or hashPartSet4
                                      or hashPartSet5 or hashPartSet6 or hashPartSet7
                                      or hashPartSet8 or hashPartSet9 or hashPartSet10
                                      or hashPartSet11 or hashPartSet12 or hashPartSet13
                                      or hashPartSet14 or hashPartSet15 or hashPartSet16
                                      or hashPartSet17 or hashPartSet18 or hashPartSet19
                                      or hashPartSet20 or hashPartSet21 or hashPartSet22
                                      or hashPartSet23 or hashPartSet24 or hashPartSet25
                                      or hashPartSet26 or hashPartSet27 or hashPartSet28
                                      or hashPartSet29 or hashPartSet30 or hashPartSet31
                                      or hashPartSet32 or hashPartSet33 or hashPartSet34
                                      or hashPartSet35 or hashPartSet36 or hashPartSet37
                                      or hashPartSet38 or hashPartSet39 or hashPartSet40):
                if count <= 85000000:
                    hashPartSet.add(newHashPart)
                elif count <= 170000000:
                    hashPartSet2.add(newHashPart)
                elif count <= 255000000:
                    hashPartSet3.add(newHashPart)
                elif count <= 340000000:
                    hashPartSet4.add(newHashPart)
                elif count <= 425000000:
                    hashPartSet5.add(newHashPart)
                elif count <= 505000000:
                    hashPartSet6.add(newHashPart)
                elif count <= 590000000:
                    hashPartSet7.add(newHashPart)
                elif count <= 675000000:
                    hashPartSet8.add(newHashPart)
                elif count <= 760000000:
                    hashPartSet9.add(newHashPart)
                elif count <= 845000000:
                    hashPartSet10.add(newHashPart)
                elif count <= 930000000:
                    hashPartSet11.add(newHashPart)
                elif count <= 1010000000:
                    hashPartSet12.add(newHashPart)
                elif count <= 1090000000:
                    hashPartSet13.add(newHashPart)
                elif count <= 1170000000:
                    hashPartSet14.add(newHashPart)
                elif count <= 1250000000:
                    hashPartSet15.add(newHashPart)
                elif count <= 1330000000:
                    hashPartSet16.add(newHashPart)
                elif count <= 1410000000:
                    hashPartSet17.add(newHashPart)
                elif count <= 1490000000:
                    hashPartSet18.add(newHashPart)
                elif count <= 1570000000:
                    hashPartSet19.add(newHashPart)
                elif count <= 1650000000:
                    hashPartSet20.add(newHashPart)
                elif count <= 1730000000:
                    hashPartSet21.add(newHashPart)
                elif count <= 1810000000:
                    hashPartSet22.add(newHashPart)
                elif count <= 1890000000:
                    hashPartSet23.add(newHashPart)
                elif count <= 1970000000:
                    hashPartSet24.add(newHashPart)
                elif count <= 2050000000:
                    hashPartSet25.add(newHashPart)
                elif count <= 2050000000:
                    hashPartSet26.add(newHashPart)
                elif count <= 2050000000:
                    hashPartSet27.add(newHashPart)
                elif count <= 2130000000:
                    hashPartSet28.add(newHashPart)
                elif count <= 2210000000:
                    hashPartSet29.add(newHashPart)
                elif count <= 2290000000:
                    hashPartSet30.add(newHashPart)
                elif count <= 2370000000:
                    hashPartSet31.add(newHashPart)
                elif count <= 2450000000:
                    hashPartSet32.add(newHashPart)
                elif count <= 2530000000:
                    hashPartSet33.add(newHashPart)
                elif count <= 2610000000:
                    hashPartSet34.add(newHashPart)
                elif count <= 2690000000:
                    hashPartSet35.add(newHashPart)
                elif count <= 2770000000:
                    hashPartSet36.add(newHashPart)
                elif count <= 2850000000:
                    hashPartSet37.add(newHashPart)
                elif count <= 2930000000:
                    hashPartSet38.add(newHashPart)
                elif count <= 3010000000:
                    hashPartSet39.add(newHashPart)
                else:
                    hashPartSet40.add(newHashPart)

                count += 1
                if count % 10000000 == 0:
                    print(count)
                newHash = hashlib.sha256(newHashPart.encode('utf-8')).hexdigest()
                newHashPart = newHash[0:hashPartLength]

            totalTime = round(time.time() - startTime, 12)
            print('\n##### Fast method - Collision found process succeeded! #####')
            print("Collision found after %s seconds" % (totalTime))
            print(('Count of the cycles:', count))
            print(('Collision hash:', newHashPart))

            hashPartSet.clear()
            hashPartSet2.clear()
            hashPartSet3.clear()
            hashPartSet4.clear()
            hashPartSet5.clear()
            hashPartSet6.clear()
            hashPartSet7.clear()
            hashPartSet8.clear()
            hashPartSet9.clear()
            hashPartSet10.clear()
            hashPartSet11.clear()
            hashPartSet12.clear()
            hashPartSet13.clear()
            hashPartSet14.clear()
            hashPartSet15.clear()
            hashPartSet16.clear()
            hashPartSet17.clear()
            hashPartSet18.clear()
            hashPartSet19.clear()
            hashPartSet20.clear()
            hashPartSet21.clear()
            hashPartSet22.clear()
            hashPartSet23.clear()
            hashPartSet24.clear()
            hashPartSet25.clear()
            hashPartSet26.clear()
            hashPartSet27.clear()
            hashPartSet28.clear()
            hashPartSet29.clear()
            hashPartSet30.clear()
            hashPartSet31.clear()
            hashPartSet32.clear()
            hashPartSet33.clear()
            hashPartSet34.clear()
            hashPartSet35.clear()
            hashPartSet36.clear()
            hashPartSet37.clear()
            hashPartSet38.clear()
            hashPartSet39.clear()
            hashPartSet40.clear()

            return {"inputHash": hashPart, "time": totalTime, "cycles": count, "collisionHash": newHashPart}
        except Exception as e:
            print(str(e))

    def findCollisionInt(self, hashPart=None):
        """
        Best performance function + storing in LOG set
        """
        try:
            if not hashPart:
                hashPart = self.hashPart
            print('\nInput hashPart:', hashPart)

            hashPartLength = len(hashPart)
            intHashSet = {int()}
            newHashPart = int(binascii.hexlify(bytes(hashPart,'utf-8')),16)

            startTime = time.time()
            while newHashPart not in intHashSet:
                intHashSet.add(newHashPart)
                if len(intHashSet)+1 % 10000000 == 0 : print(len(intHashSet)+1)
                strHashPart = binascii.unhexlify(bytes(newHashPart).decode('utf-8'))
                newHash = hashlib.sha256(strHashPart).hexdigest()
                newHash = bytes(newHash[0:hashPartLength],'utf-8')
                newHashPart = int(binascii.hexlify(newHash),16)

            totalTime = round(time.time() - startTime, 12)
            print('\n##### LONG method - Collision found process succeeded! #####')
            print("Collision found after %s seconds" % (totalTime))
            print('Count of the cycles:', len(intHashSet)+1)
            print('Collision hash:', newHash)

            #h = hpy()
            #print h.heap()

            """
            indexOfCollision = int()
            cycleCount = 0
            for i in setArray:
                indexOfCollision = list(i).index(newHashPart)
                if indexOfCollision:
                    indexOfCollision += cycle_count * setCount
                    break
                cycleCount += 1
            print(('Index of collision hash:', indexOfCollision))
            return {"inputHash": hashPart, "time": totalTime, "cycles": len(longHashSet)+1,
                    "collisionHash": newHash, "indexOfCollisionHash": indexOfCollision}
            """
            return {"inputHash": hashPart, "time": totalTime, "cycles": len(intHashSet)+1, "collisionHash": newHash}

        except Exception as e:
            print(str(e))

    def findCollisionFirst(self, hashPart=None):
        """
        Function to be thread by individually calling - looking for a collision with first hashPart
        """
        try:
            count = 0
            newHashPart = ''
            hashPartLength = len(hashPart)

            startTime = time.time()
            while hashPart != newHashPart:
                newHashPart = hashlib.sha256(newHashPart.encode('utf-8')).hexdigest()[0:hashPartLength]
                count += 1
                if count % 100000000 == 0: print(count)
            totalTime = round(time.time() - startTime, 12)
            print('\n##### findCollisionFirst method - Collision found process succeeded! #####')
            print("Collision found after %s seconds" % (totalTime))
            print(('Count of the cycles:', count))
            print(('Collision hash:', newHashPart))

            return {"inputHash": hashPart, "time": totalTime, "cycles": count, "collisionHash": newHashPart}

        except Exception as e:
            print(str(e))

    def findCollisionWithDBSet(self, hashPart=None):
        """
        Function is looking for a collision with hashPart
        """
        try:
            pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
            r = redis.Redis(connection_pool=pool)
            r.flushdb()

            if not hashPart:
                hashPart = self.hashPart
                hashPartLength = self.hashPartLength
            else:
                hashPartLength = len(hashPart)

            count = 0

            startTime = time.time()
            while not r.sismember('hset', hashPart):
                r.sadd('hset', hashPart)
                count += 1
                if count % 10000000 == 0:
                    print(count)
                hashPart = hashlib.sha256(hashPart.encode('utf-8')).hexdigest()[0:hashPartLength]

            totalTime = round(time.time() - startTime, 12)
            print('\n##### DBSet method - Collision found process succeeded! #####')
            print("Collision found after %s seconds" % (totalTime))
            print(('Count of the cycles:', r.scard('hset')))
            print(('Collision hash:', hashPart))
            # print 'Index of collision hash:'
            return {"inputHash": hashPart, "time": totalTime, "cycles": count, "collisionHash": hashPart}

        except Exception as e:
            print(str(e))


def main():
    # Input parameters

    parser = argparse.ArgumentParser(usage='$prog [options] -sha2 -b 32 -i hash.txt',
                                     description='SHA collision finder', add_help=True,
                                     epilog='SHA collision finder. Written by Jan Stangler, Ondrej\
                                      Gajdusek, Sarka Chwastova, VUT FEKT, ICT1 project, 2017')
    parser.add_argument('-sha2', '--sha256', action='store_true', dest='sha256',
                        help='-sha2 (hash algorithm)', required=True)
    parser.add_argument('-b', '--bits', action='store', dest='bits',
                        help='-b 32 (Number of hash bits to find collision)', required=True)
    parser.add_argument('-i', '--input', action='store', dest='inputFile',
                        help='-i input.txt The input file with hashes', required=True)
    parser.add_argument('-hg', '--hashgroup', action='store_true', dest='hashGroup',
                        help='-h The input file has hashes per line', required=False)
    parser.add_argument('-t', '--text', action='store_true', dest='text',
                        help='-t The input file of random text', required=False)
    parser.add_argument('-f', '--first', action='store_true', dest='first',
                        help='-f Collision with the first one hash', required=False)
    args = parser.parse_args()

    # Instance of the class Shacol
    shacol = Shacol(args.sha256, args.bits, args.inputFile, args.hashGroup, args.text, args.first)
    shacol.getInfo()

    print("Do you want to proceed?")
    input('\nPress Enter to continue...')

    start = timeit.default_timer()  # Default run time monitoring

    """
    #Queuing and threading
    q = Queue.LifoQueue()
    #put items to queue
    for key in jobTrack:
    	if jobTrack[key] != "Invalid":
    		q.put(str(key))
    	else:
    		print (str(key) + " is not added to queue as its invalid")

    #for i in range(100):
    t1 = threading.Thread(target=findCollisionStatus) #,args=(q,))
	t1.daemon = True
    t1.start() #Start the thread

    #q.join()
    #print ("\nFinally")
    """

    shacol.findCollisionFast()
    shacol.findCollisionInt()

    if (args.first):
        for hashes in shacol.shaList:
            shacol.findCollisionFirst(hashes)

    # shacol.findCollisionFirst(shacol.shaList[0])
    # shacol.findCollisionSetArray()
    # shacol.findCollisionWithDBset()

    stop = timeit.default_timer()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted... Terminating')
        sys.exit()


def status():  # Count of cycles, array/database
    countOfCycles = 0
    runTime = ''
    # h = hpy()

    print('\n' * 100)
    # shacol.findCollisionCheckSequence.count
    print(('Runtime:', stop - start))
    # print (h.heap())


def findCollisionStatus(q):  # method working with threads, q means queqe
    while not q.empty():
        myCollision = threading.local()
        myCollision.scanning = True
        myCollision.dom = q.get
        myCollision.pstart = pstart
        myCollision.prepeat = prepeat
        # str(myCollision.dom) --- now Processing
        # str(threading.activeCount())

        while (myCollision.scanning):
            try:
                status()
            except Exception as e:
                print(str(e))
                pass
        myData.scanning = False
