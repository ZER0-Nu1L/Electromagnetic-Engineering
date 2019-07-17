#物理程序的计算部分
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

if __name__ == "__main__":
#Python使用utf-8,可以用特殊符号
     I, I0, a, b, r, v, x, t = symbols('I, I0, a, b, r, v, x, t')
     ω, π, µ, φ, ε = symbols('ω, π, µ, φ, ε')
     case = 3
     I = I0 * cos(ω * t)
     x = v * t

     lst = []
#特殊情况的计算
     #面积相等的三角形对应的电动势随边长比的变化
     if case == 1:
          φ = integrate(µ*I/(2*π*r)*(x+b-r)*a/b, (r, x, x+b))
          ε = -diff(φ, t)
          for a_t in range(60):
               b_t = 1 / (a_t+1)   #面积不变的情况下
               lst.append(ε.evalf(subs={µ: 4.0e-7*pi, \
               π: pi, I0: 1, b: b_t, x: 1, v: 1, t: 1, ω:2*pi, a:a_t+1}))   # 2* pi """
     
     #三角形线框对应的电动势随时间的变化
     elif case == 3:
          φ = integrate(µ*I/(2*π*r)*(x+b-r)*a/b, (r, x, x+b))
          ε = -diff(φ, t)
          for s in range(60):
               lst.append(ε.evalf(subs={µ: 4.0e-7*pi, \
               a:10, b:5*sqrt(3), π: pi, I0: 10, x: 10, v: 10, t: (s+1)/6, ω: 2*pi, a: 1})*10**5)
     
     #矩形线框对应的电动势随时间的变化
     elif case == 4:
          φ = integrate(µ*I/(2*π*r)*a, (r, x, x+sqrt(3)/2*a))
          ε = -diff(φ, t)
          for s in range(60):
               lst.append(ε.evalf(subs={µ: 4.0e-7*pi, \
               a:10, π: pi, I0: 10, x: 10, v: 10, t: (s+1)/6, ω: 2*pi, a: 1})*10**5)
     
     #正五边形线框对应的电动势随时间的变化
     elif case == 5:
          φ = integrate(\
               µ*I/(2*π*r)*(\
                    a*2*sin(54/180*π) + ( 2*sin(54/180*π) - 1 )/ cos(72/180*π) * (r-x-a*cos(72/180*π))\
                         )\
                    ,\
               (r, x, x+a*cos(72/180*π) )\
               ) + \
          integrate(\
               µ*I/(2*π*r)*(\
                    a*2*sin(54/180*π) + 2*sin(54/180*π)/cos(54/180*π)*(x-r)\
                         )\
                    ,\
              (r, x+a*cos(72/180*π), x+a*cos(72/180*π)+a*cos(54/180*π))\
          )
          ε = -diff(φ, t)
          for s in range(60):
               lst.append(re(ε.evalf(subs={µ: 4.0e-7*pi,
               a: 10, π: pi, I0: 10, x: 10, v: 10, t: (s+1)/6, ω: 2*pi, a: 1})*10**5))
     
     #正六边形线框对应的电动势随时间的变化
     elif case == 6:
          φ = integrate(\
               µ*I/(2*π*r)*(2*a+2/sqrt(3)*(r-x-sqrt(3)/2*a))\
                    ,\
                (r, x, x+sqrt(3)/2*a)\
               ) + \
          integrate(\
               µ*I/(2*π*r)*(2*a+2/sqrt(3)*(x-r))\
                    , \
               (r, x+sqrt(3)/2*a, x+sqrt(3)*a)\
               )
          ε = -diff(φ, t)
          for s in range(60):
               lst.append(ε.evalf(subs={µ: 4.0e-7*pi, \
               a: 10, π: pi, I0: 10, x: 10, v: 10, t: (s+1)/6, ω: 2*pi, a: 1})*10**5)
     
     #正七边形线框对应的电动势随时间的变化
     elif case == 7:
          φ = integrate( \
               µ*I/(2*π*r) * (\
                    a*(1+2*sin(38.57/180*π)) + 2*sin(38.57/180*π)/cos(38.57/180*π)*(r-x-(a*cos(38.57/180*π))) \
                              )\
                        , \
              (r, x, x + a*cos(38.57/180*π) ) \
               ) + \
          integrate(\
              µ*I/(2*π*r) * (\
                  a*(1+2*sin(38.57/180*π)) + 2*sin(12.85/180*π)/cos(12.85/180*π)*(x-r)
                              )\
                         ,\
              (r, x + a*cos(38.57/180*π), x + a*cos(38.57/180*π) + a*cos(12.85/180*π))\
               ) + \
          integrate(\
              µ*I/(2*π*r) * (\
                  a*(1+2*sin(38.57/180*π)) + (1+2*sin(38.57/180*π))/cos(64.28/180*π)*(x-r)\
                         )\
                    ,\
               (r, x + a*cos(38.57/180*π) + a*cos(12.85/180*π), x + a*cos(38.57/180*π) + a*cos(12.85/180*π)+a*cos(64.28/180*π))\
               )
          ε = -diff(φ, t)
          for s in range(60):
               lst.append(re(ε.evalf(subs={µ: 4.0e-7*pi, \
               a: 10, π: pi, I0: 10, x: 10, v: 10, t: (s+1)/6, ω: 2*pi, a: 1})*10**5))
     
     an = np.array(lst)  # , dtype=np.float
#可视化
     fig = plt.figure(figsize=(6, 5))
     plt.title('Curve of electromotive force with time', \
               fontsize='large', fontweight='bold')
     # fig.suptitle('电动势随时间变化曲线', fontsize=14, fontweight='bold')
     ax = fig.add_subplot(111)
     fig.subplots_adjust(top=0.85)
     ax.set_xlabel('t (time)')
     ax.set_ylabel('ε (electrodynamic force)')

     plt.plot(range(60), an)
     plt.show()
