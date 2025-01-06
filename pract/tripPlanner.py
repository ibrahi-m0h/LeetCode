def trip_planner_welcome(name):
  print(f"Welcome to tripplanner v1.0 {name}!")

trip_planner_welcome("Ibrahim")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.5)

print(estimate)