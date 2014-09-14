from jompy.matscience.diffusion import Fick1

# Steel plate at 700ºC, in steady-state, how much carbon transfers
# from the rich to the deficient side?
C1 = 1.2  # kg/m3 at 5 mm
C2 = 0.8  # kg/m3 at 10 mm
D = 3*10**(-11)  # m2/s at 700ºC

flux = Fick1(d=D, c2=C2, c1=C1, thick=0.005).flux()
print("flux [kg/m2 s] = ", flux)