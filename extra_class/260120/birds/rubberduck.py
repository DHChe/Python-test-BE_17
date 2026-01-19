from birds.birds import Birds

class RubberDuck(Birds):
    def __init__(self) -> None:
        super().__init__("러버덕")
        self.tweet = '삑삑삑'
        self.flight_method = '날지 못함'

    def species(self) -> str:
        return self.species

    def get_tweet(self) -> str:
        return self.tweet

    def get_method(self) -> str:
        return self.flight_method