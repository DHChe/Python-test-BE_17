from birds import Parrot
from birds import Sparrow
from birds import Pigeon
from birds import Chicken
from birds import RubberDuck

if __name__=="__main__":
    user_input = input(f"앵무새/참새/비둘기/닭/러버덕 중에 좋아하는 새를 입력하세요.")

    if user_input == "앵무새":
        bird = Parrot()

    elif user_input == "참새":
        bird = Sparrow()

    elif user_input == "비둘기":
        bird = Pigeon()

    elif user_input == "닭":
        bird = Chicken()

    elif user_input == "러버덕":
        bird = RubberDuck()
    else:
        print("잘못된 입력입니다.")
        exit()

    bird.start_fly()


