from django.test import TestCase
from music.models import Artist, Album
from music.serializers import ArtistSerializer, SongSerializer


class TestArtistSerializers(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Example Artist")

    def test_data(self):
        data = ArtistSerializer(self.artist).data
        assert data['id'] is not None
        assert data['name'] == 'Example Artist'
        assert data['picture'] == ''


class TestSongSerializers(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name='Example Artitst')
        self.album = Album.objects.create(artist=self.artist, title='Example Album')

    def test_is_valid(self):
        data = {
            "title": "Example Title",
            "album": self.album.id,
            "cover": "",
            "source": "https://example.com/music.mp3",
            "listened": 0,
        }
        serializer = SongSerializer(data=data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)

    def test_is_not_valid(self):
        data = {
            "title": "Example Title",
            "album": self.album.id,
            "cover": "",
            "source": "https://example.com/music",
            "listened": 0,
        }
        serializer = SongSerializer(data=data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertEqual(str(serializer.errors['source'][0]), 'Only mp3 is supported')
