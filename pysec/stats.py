# Python Security Project (PySec) and its related class files.
#
# PySec is a set of tools for secure application development under Linux
#
# Copyright 2014 PySec development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: ascii -*-
"""Module with statistics utilities."""


__all__ = 'avg',


def avg(*values):
    """Generator to calculate arithmetic mean"""
    n = -1.
    tot = .0
    for n, el in enumerate(values):
        tot += el
    n += 1.
    avg = 0 if n == 0. else tot/n
    while 1:
        el = (yield avg)
        if el is None:
            continue
        el = float(el)
        avg = (avg + el / n) / ((n + 1) / n)
        n += 1

