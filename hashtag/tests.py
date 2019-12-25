from django.test import TestCase
from .models import Tweet, Hashtag

class HashtagTest(TestCase):
    def setUp(self):
        Hashtag.objects.create(message='christmas')

    def test_message_return(self):
        christmas=Hashtag.objects.get(message='christmas')
        self.assertEqual(christmas.__str__(), 'christmas')

# Create your tests here.
