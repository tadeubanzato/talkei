#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bots/followfollowers.py

from GoogleNews import GoogleNews

googlenews = GoogleNews()
googlenews.search('Trump')
result = googlenews.result()
print(len(result))

for n in range(len(result)):
    print(n)
    for index in result[n]:
        print(index, '\n', result[n][index])

    exit()
