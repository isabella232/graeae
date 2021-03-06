#!/usr/bin/env python

import unittest
import app_config

from datetime import datetime
from scrapers.facebook import FacebookScraper

class TestScrapeFacebook(unittest.TestCase):
    def setUp(self):
        self.scraper = FacebookScraper()
        self.posts = self.scraper.scrape_facebook(
            profile_filename='tests/snapshots/fb-profile-04-20-2015.json',
            posts_filename='tests/snapshots/fb-posts-04-20-2015.json'
        )

    def test_facebook_id(self):
        self.assertEqual(self.posts[0].facebook_id, '10643211755_10153419389686756')

    def test_headline(self):
        self.assertEqual(self.posts[0].headline, 'How D.C. Is Turning A \'Pedestrian Dead-Zone\' Into An Eco-Showcase')

    def test_post_type(self):
        self.assertEqual(self.posts[0].post_type, 'link')

    def test_art_url(self):
        self.assertEqual(self.posts[0].art_url, 'http://amplify.nprstations.org/files/201504/viewmalltobanneker.jpg_itok_KBLvGBLY')

    def test_art_root_url(self):
        self.assertEqual(self.posts[2].art_root_url, 'http://media.npr.org/assets/img/2015/04/17/englishname.jpg')

    def test_link_url(self):
        self.assertEqual(self.posts[0].link_url, 'http://wamu.org/programs/metro_connection/15/04/17/southwest_ecodistrict')

    def test_seamus_id(self):
        self.assertEqual(self.posts[2].seamus_id, '400399802')

    def test_created_time(self):
        self.assertEqual(self.posts[0].created_time, datetime(2015, 4, 20, 17, 9, 40))

    def test_updated_time(self):
        self.assertEqual(self.posts[0].updated_time, datetime(2015, 4, 20, 17, 9, 40))

class TestScrapeInsights(unittest.TestCase):
    def setUp(self):
        self.scraper = FacebookScraper()
        self.posts = self.scraper.scrape_facebook(
            profile_filename='tests/snapshots/fb-profile-04-20-2015.json',
            posts_filename='tests/snapshots/fb-posts-04-20-2015.json'
        )
        self.insights = self.scraper.scrape_post_insights(
            self.posts[0],
            filename='tests/snapshots/fb-insights-04-20-2015.json'
        )

    def test_shares(self):
        self.assertEqual(self.insights.shares, 0)

    def test_likes(self):
        self.assertEqual(self.insights.likes, 3)

    def test_comments(self):
        self.assertEqual(self.insights.comments, 0)

    def test_link_clicks(self):
        self.assertEqual(self.insights.link_clicks, 24)

    def test_photo_view_clicks(self):
        self.assertEqual(self.insights.photo_view_clicks, 0)

    def test_people_reached(self):
        self.assertEqual(self.insights.people_reached, 1160)
