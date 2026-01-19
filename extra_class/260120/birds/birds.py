# 자식 클래스에서 반드시 구현해야 하는 메서드를 강제하기 위헤 abstractmethod 사용
from abc import ABC, abstractmethod

class Birds(ABC):
    def __init__(self, species: str) -> None:
        self.species = species

    @abstractmethod
    def tweet(self) -> None:
        pass

    @abstractmethod
    def flight_method(self) -> None:
        pass

    @abstractmethod
    def flight_distance(self) -> None:
        pass

    def start_fly(self) -> None:
        print(f"{self.species} 출발!!!")
        print(f"{self.get_tweet()}")
        print(f"날개를 {self.get_flight_method()} 날았습니다.")
        print(f"결과는 {self.get_distance()} m 입니다.")