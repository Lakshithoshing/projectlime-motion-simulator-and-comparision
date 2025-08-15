import math
import matplotlib
import matplotlib.pyplot
u1 = float(input("enter magnitude of velocity in m/sec for first projectile"))
u2 = float(input("enter magnitude of velocity in m/sec for second projectile"))
angle1 = float(input("enter angle for projectile in degrees for first projectile"))

angle2 = float(input("enter angle for projectile in degrees for second projectile"))
g =10
dt =0.0001
radians1=math.radians(angle1)
radians2 = math.radians(angle2)
uy1 = u1*math.sin(radians1)
ux1 = u1*math.cos(radians1)
uy2 = u2*math.sin(radians2)
ux2 = u2*math.cos(radians2)

x2_coordinate=[]
y2_coordinate=[]
x1_coordinate=[]
y1_coordinate=[]
time_values1=[]
time_values2=[]

x1, y1=0, 0
x2,y2=0,0
t1=0
t2=0

while y1>=0:
    time_values1.append(t1)
    x1_coordinate.append(x1)
    y1_coordinate.append(y1)
    
    ax=0
    ay=-g

    ux1= ux1+ax*dt
    uy1=uy1+ay*dt
    x1= x1+ux1*dt
    y1= y1+uy1*dt
    t1 =t1+dt
while y2>=0:
    x2_coordinate.append(x2)
    y2_coordinate.append(y2)
    time_values2.append(t2)

    ax2=0
    ay2=-g
    ux2= ux2+ax2*dt
    uy2=uy2+ay2*dt
    x2= x2+ux2*dt
    y2= y2+uy2*dt
    t2 =t2+dt
matplotlib.pyplot.plot(x1_coordinate,y1_coordinate,color="red",label=f"Projectile with velocity {u1} m/s and angle {angle1}°")
matplotlib.pyplot.plot(x2_coordinate,y2_coordinate,color="blue",label=f"Projectile with velocity {u2} m/s and angle {angle2}°")
matplotlib.pyplot.legend()
matplotlib.pyplot.title("projectile motion")
matplotlib.pyplot.xlabel("Horizontal distace in m")
matplotlib.pyplot.ylabel("vertical distance in m")

matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()
