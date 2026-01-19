from birds.birds import Birds
from birds.flight_distance import cal_dis

class Parrot(Birds):
    def __init__(self) -> None:
        super().__init__("앵무새")
        self.tweet = '까악'
        self.flight_method = '힘차게'

    def species(self) -> str:
        return self.species

    def get_tweet(self) -> str:
        return self.tweet

    def get_method(self) -> str:
        return self.flight_method

    def get_distance(self) -> int:
        return cal_dis(self, flight_method)