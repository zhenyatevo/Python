class Song:
    tags = []

    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
        self.tags =[]

    def add_tags(self, *args):
        self.tags.extend(args)


song1 = Song('Shakey Graves', 'Roll the Bones')
song1.add_tags('Americana', 'Country')

song2 = Song('Neuromonah', 'Holodno v lesu')
song2.add_tags('Russian', 'Drum \'n\' base')

print(song2.tags)
# ['Americana', 'Country', 'Russian', 'Drum \'n\' base']
