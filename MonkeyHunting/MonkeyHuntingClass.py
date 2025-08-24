import math

class MonkeyHunting:
    def __init__(self,g_acc: float) -> None:
        self.__g_acc=g_acc
        print("g_acc = ",self.__g_acc)

    def set_initial_bullet_position(self,x0:float,z0:float)->None:
        self.__x0 = x0
        self.__z0 = z0

    def set_initial_bullet_velocity(self,vx0:float,vz0:float)->None:
        self.__vx0 = vx0
        self.__vz0 = vz0

    def set_initial_bullet_velocity_angle(self,v0:float,theta0:float)->None:
        self.__vx0 = v0*math.cos(theta0)
        self.__vz0 = v0*math.sin(theta0)

    def get_bullet_position(self,time:float)->[float,float]:
        xw = self.__vx0*time+self.__x0
        zw = 0.5*self.__g_acc*time*time \
                +self.__vz0*time \
                +self.__z0
        return [xw,zw]

    def set_initial_monkey_position(self,xm0:float,zm0:float)->None:
        self.__xm0 = xm0
        self.__zm0 = zm0

    def get_monkey_position(self,time:float)->float:
        return [xm0,0.5*self.__g_acc*time*time + zm0]

    def set_ground(self,z_ground:float)->None:
        self.__z_grounbd = z_ground

    def solve_theta(self,v0:float)->[bool,float]:
        tan_th=(self.__zm0 - self.__z0)/(self.__xm0 - self.__x0)
        th = math.atan(tan_th)
        vx0 = v0*math.cos(th)
        vz0 = v0*math.sin(th)
        #check bullet reaches the ground
        tw = (self.__xm0 - self.__x0)/vx0
        zw = 0.5*self.__g_acc*tw*tw + vz0*tw + self.__z0
        if zw < self.__z_grounbd:
            return [False,0.0]
        return [True,th]

    @property
    def g_acc(self)->float:
        return self.__g_acc

    @g_acc.setter
    def g_acc(self,g_acc:float)->None:
        self.__g_acc=g_acc



