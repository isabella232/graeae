#!/usr/bin/env python

import dataset
import unittest
import app_config

from fabric.api import local
from nose.tools import assert_equal
from scrapers.homepage import HomepageScraper
from time import time


class TestScraper(unittest.TestCase):
    """
    Test the scraper
    """
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""
        klass.temp_db_name = 'graeae_%s' % int(time())
        local('createdb %s' % klass.temp_db_name)

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""
        local('dropdb %s' % klass.temp_db_name)

    def setUp(self):
        self.db = dataset.connect('postgres:///%s' % self.temp_db_name)
        self.scraper = HomepageScraper(self.db)

    def test_db_write(self):
        self.scraper.scrape()
        rows = list(self.scraper.table.all())
        self.assertGreater(len(rows), 0)



