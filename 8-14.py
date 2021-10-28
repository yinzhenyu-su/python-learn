#构造函数
def make_car(maker,type,**profile):
    car_profile={}
    car_profile['maker']=maker#制造商
    car_profile['type']=type#型号
    for key,value in profile.items():#键值对
        car_profile[key]=value
    return car_profile

car = make_car(
    'subaru',
    'outlook',
    color='blue',
    tow_package=True
)

print(car)
