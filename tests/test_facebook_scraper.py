#!/usr/bin/env python

import unittest
import app_config

from scrapers.facebook import FacebookScraper

class TestScrapeFacebook(unittest.TestCase):
    def setUp(self):
        self.scraper = FacebookScraper()
        self.posts = self.scraper.scrape_facebook(
            profile_filename='tests/snapshots/fb-profile-04-20-2015.json',
            posts_filename='tests/snapshots/fb-posts-04-20-2015.json'
        )

    def test_headline(self):
        self.assertEqual(self.posts[0].headline, 'How D.C. Is Turning A \'Pedestrian Dead-Zone\' Into An Eco-Showcase')

class TestScrapeInsights(unittest.TestCase):
    def setUp(self):
        self.scraper = FacebookScraper()
        self.posts = self.scraper.scrape_facebook()
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
