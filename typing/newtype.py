from typing import NewType


UserId = NewType("UserId", int)
CarId = NewType("CarId", int)


def get_car_id() -> CarId:
    return CarId(0)

def get_user_id() -> UserId:
    return UserId(0)

def get_car_owner(car: CarId) -> UserId:
    return UserId(0)

car_id = get_car_id()
user_id = get_user_id()
owner = get_car_owner(user_id)
