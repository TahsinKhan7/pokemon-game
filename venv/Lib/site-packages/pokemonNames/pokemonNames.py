#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os

from sys import exc_info
from random import randrange

# Since it fails due to recursive imports
try:
    from numberify.numberify import Numberify
except ImportError:
    from numberify import Numberify

this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, 'names.list')


class PokemonNames():
    '''Generate Pokemon names'''

    def __init__(self, default=True):
        '''Opens the name list and stores the names in a dictionary'''
        self.nameDict = {}
        self.totalCount = 0
        if default:
            self.nameDict = self.get_from_indexedFile(DATA_PATH)

    def get_from_indexedFile(self, filename):
        fd = open(filename, 'r+')
        lines = fd.readlines()
        self.totalCount = len(lines)
        for index, val in enumerate(lines):
            lines[index] = val.split()
        nameDict = {}
        for line in lines:
            nameDict[int(line[0])] = line[1]
        return nameDict

    def get_random_name(self):
        '''Return a random name'''
        key = randrange(1, self.totalCount + 1)
        return self.nameDict[key]

    def get_name(self, key):
        '''Return a name for the given key
        Argument:
        key -- Pokemon number id (int)
        '''
        try:
            return self.nameDict[key]
        except IndexError as e:
            print 'IndexError {0}: {1}'.format(e.errno, e.strerror)

    def append_to_list(self, source, start=None, hasIndex=False):
        '''Appends new list to self.nameDict
        Argument:
        source -- source of new name list (filename or list)
        start  -- starting index of new list
        hasIndex -- the file is already indexed
        '''
        nfy = Numberify()
        try:
            if start is None:
                if type(source) is str:
                    if hasIndex is True:
                        newList = self.get_from_indexedFile(source)
                else:
                    newList = nfy.numberify_data(source,
                                                 len(self.nameDict) + 1)
            else:
                newList = nfy.numberify_data(source, start)
            self.nameDict = dict(self.nameDict.items() + newList.items())
            self.totalCount = len(self.nameDict)
        except:
            print 'Unknown error:', exc_info()[0]
