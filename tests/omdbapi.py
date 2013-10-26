# -*- coding: UTF-8 -*-
import os
import tempfile
import shutil
import unittest

import logging
logging.basicConfig(level=logging.DEBUG, filename='tests.log')

import medialinkfs.parsers.omdbapi as omdbapi

base = os.path.dirname(__file__)

class TestOMDBAPI(unittest.TestCase):
	def setUp(self):
		logging.debug("Initializing unittest %s"%(self.id(),))

	def test_dynomutt(self):
		res = omdbapi.get_metadata({"path":"/Dynomutt Dog Wonder"})
		self.assertNotEqual(None, res)
		res['actors'] = sorted(res['actors'])
		res['genres'] = sorted(res['genres'])
		self.assertEqual(4, len(res['actors']))
		self.assertEqual(1, len(res['directors']))
		self.assertEqual(2, len(res['genres']))
		self.assertEqual('Frank Welker', res['actors'][0])
		self.assertEqual('Gary Owens', res['actors'][1])
		self.assertEqual('Charles A. Nichols', res['directors'][0])
		self.assertEqual('Animation', res['genres'][0])

	def test_startrek(self):
		res = omdbapi.get_metadata({"path":"/Star Trek (1966)"})
		self.assertNotEqual(None, res)
		self.assertEqual(1966, res['year'])
