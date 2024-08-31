import redis

class MusicCache:
    def __init__(self, redis_host="localhost", redis_port=6379):
        self.redis = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    def add_track(self, track_id, track_info):
        # Add track information to a hash
        self.redis.hset(f"track:{track_id}", mapping=track_info)

    def get_track(self, track_id):
        # Retrieve track information from a hash
        return self.redis.hgetall(f"track:{track_id}")

    def create_playlist(self, playlist_id):
        # No need to pass an empty list to sadd
        # Just ensure the set is created, if it doesn't already exist
        self.redis.sadd(f"playlist:{playlist_id}:tracks", "dummy_member")

    def add_track_to_playlist(self, playlist_id, track_id):
        # Add a track ID to the playlist set
        self.redis.sadd(f"playlist:{playlist_id}:tracks", track_id)

    def get_playlist(self, playlist_id):
        # Retrieve all track IDs from the playlist set
        return self.redis.smembers(f"playlist:{playlist_id}:tracks")

if __name__ == "__main__":
    cache = MusicCache()

    cache.add_track("1", {"title": "Song A", "artist": "artistA"})
    cache.add_track("2", {"title": "Song B", "artist": "artist B"})

    cache.create_playlist("playlist1")
    cache.add_track_to_playlist("playlist1", "1")
    cache.add_track_to_playlist("playlist1", "2")

    print(f"Track1 info: {cache.get_track('1')}")
    print(f"Track2 info: {cache.get_track('2')}")
    print(f"Playlist 1 tracks: {cache.get_playlist('playlist1')}")

