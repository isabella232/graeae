from collections import OrderedDict
from itertools import groupby

import os

class Story:
    def __init__(self, api_story, run_time):
        self.api_story = api_story
        self.run_time = run_time

    def serialize(self):
        return OrderedDict([
            ('run_time', self.run_time),
            ('id', self.id),
            ('title', self.title),
            ('publication_date', self.publication_date),
            ('story_date', self.story_date),
            ('last_modified_date', self.last_modified_date),
        ])

    @property
    def id(self):
        return self.api_story.attr('id')

    @property
    def title(self):
        return self.api_story.children('title').text()

    @property
    def publication_date(self):
        return self.api_story.children('pubDate').text()

    @property
    def story_date(self):
        return self.api_story.children('storyDate').text()

    @property
    def last_modified_date(self):
        return self.api_story.children('lastModifiedDate').text()