#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@file debug.py
@author Sam Freeside <snovvcrash@protonmail.com>
@date 2018-05

@brief Debug utils.

@license
Copyright (C) 2018 Sam Freeside

This file is part of usbrip.

usbrip is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

usbrip is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with usbrip.  If not, see <http://www.gnu.org/licenses/>.
@endlicense
"""

import functools
import time

import lib.core.config as cfg


def time_it(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print('{}: {:.3f} seconds'.format(func.__name__, end-start))
		return result

	return wrapper


class time_it_if_debug:
	def __init__(self, condition, decorator):
		self._condition = cfg.DEBUG
		self._decorator = decorator

	def __call__(self, func):
		if not self._condition:
			return func

		return self._decorator(func)
