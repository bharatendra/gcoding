#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specif

import sys

def is_a_solution(p, k, n, m, all):
    cnt = 0
    for i in xrange(k):
        if p[i] == 1:
            cnt = cnt + 1
    if cnt == m:
        all.append(p[:])
        return True
    return False

def backtrack(p, k, n, m, all):
    if is_a_solution(p, k, n, m, all):
        return
    if k >= n:
        return
        
    for i in [1, 0]:
        p[k]= i
        backtrack(p, k + 1, n, m, all)

def get_rotations(pat, n):
    rotations = set()
    prev = pat
    rotations.add(tuple(pat[:]))
    for i in xrange(n - 1):
        r = prev[n-1:] + prev[:n-1]
        rotations.add(tuple(r[:]))
        prev = r[:]
    return rotations

def get_permutations(n, m):
    permutation = [0 for i in xrange(n)]
    candidates = [1, 0]
    allpermutations = []
    backtrack(permutation, 0, n, m, allpermutations)
    return allpermutations

def get_types_and_rotations(n, m):
    permutations = get_permutations(n, m)
    types = []
    while len(permutations) > 0:
        type = permutations[0]
        rotations = get_rotations(type, n)
        types.append((type, rotations))
        #print "pat: ",type, " #: ", len(rotations)
        del permutations[0]
        for i in reversed(xrange(len(permutations))):
            if (tuple(permutations[i]) in rotations):
                del permutations[i]
    return types

if len(sys.argv) < 2:
    print "Please specify number of bits in a word(8/16)"
    sys.exit(1)

n = int(sys.argv[1])
if n != 8 and n != 16:
    print "Please specify 8 or 16"
    sys.exit(1)
count = 0
for m in xrange(n + 1):
    types = get_types_and_rotations(n, m)
    pcount = 0
    for t in types:
        count = count + len(t[1])
        pcount = pcount + len(t[1])
    print "#1-bits: %d types: %d #patterns: %d" %(m, len(types), pcount)
    
print "total: ",count
