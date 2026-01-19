from birds.birds import Birds

class Pigeon(Birds):
    def __init__(self) -> None:
        super().__init__("비둘기")
        self.tweet = '구구'
        self.flight_method = '부드럽게'

    def species(self) -> str:
        return self.species

    def get_tweet(self) -> str:
        return self.tweet

    def get_method(self) -> str:
        return self.flight_method