from birds.birds import Birds

class Sparrow(Birds):
    def __init__(self) -> None:
        super().__init__("참새")
        self.tweet = '쨱짹'
        self.flight_method = '빠르게'

    def species(self) -> str:
        return self.species

    def get_tweet(self) -> str:
        return self.tweet

    def get_method(self) -> str:
        return self.flight_method