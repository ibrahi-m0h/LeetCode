train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# temperature = float(input("Enter temp in Fahrenheit: "))

def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

def c_to_f(c_temp):
  return (c_temp * (9/5) + 32)

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)

print(f100_in_celsius)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force")

def get_energy(mass, c=3*10**8):
  return mass*c**2

bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules")

def get_work(mass, acceleration, distance):
  return mass * acceleration * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print(train_work)


