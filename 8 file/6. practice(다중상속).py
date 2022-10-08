#일반 유닛
class Unit:   # 부모 클래스
    def __init__(self, name, hp,):
        self.name = name
        self.hp = hp

#다중 상속은 부모 클래스가 여러개 ㅇㅇ

#공격 유닛
class AttackUnit(Unit):  #자식클래스
    def __init__(self, name, hp, damage):        
        Unit.__init__(self, name, hp)  
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp >= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#드랍쉽

#날수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed  # 멤버변수 초기화
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
    
#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):   # 다중 상속 받을 시 콤마 사용
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


#발키리 만들기 !!!!
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")  # flyable 클래스에 이름 부분이 따로 없어서 따로 이름을 기입함

#정리

#FlyableAttackUnit >> Flyable
#                  >> AttackUniy >> Unit