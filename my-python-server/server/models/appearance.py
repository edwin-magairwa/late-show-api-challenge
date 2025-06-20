class Appearance:
    def __init__(self, guest_id, episode_id):
        self.guest_id = guest_id
        self.episode_id = episode_id

    def __repr__(self):
        return f"<Appearance guest_id={self.guest_id} episode_id={self.episode_id}>"