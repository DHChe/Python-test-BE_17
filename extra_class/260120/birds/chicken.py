from birds.birds import Birds

class Chicken(Birds):
    def __init__(self) -> None:
        super().__init__("닭")
        self.tweet = '꼬끼오'
        self.flight_method = '퍼덕이며'

    def species(self) -> str:
        return self.species

    def get_tweet(self) -> str:
        return self.tweet

    def get_method(self) -> str:
        return self.flight_method