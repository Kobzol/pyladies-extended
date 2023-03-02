struct CarId(u32);
struct UserId(u32);

fn get_car_owner(car: CarId) {
}

fn get_user() -> UserId {
    UserId(0)
}

fn newtype() {
    let user = get_user();
    get_car_owner(user);
}
