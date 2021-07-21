"""
genres							plays				return
["classic", "pop", "classic", "classic", "pop"]		[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
"""

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

hash_genre = {}
for genre, play in zip(genres, plays):
    if genre in hash_genre:
        hash_genre[genre] += play
    else:
        hash_genre[genre] = play

# hash_genre: {'pop': 3100, 'classic': 1450}