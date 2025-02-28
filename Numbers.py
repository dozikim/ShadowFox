# 2.1 Format function usage
formatted_str = "{:o}".format(145)  # 'o' stands for octal representation
print("Octal representation of 145:", formatted_str)

# 2.2 Calculate the area of the pond
radius = 84
pi_value = 3.14
pond_area = pi_value * (radius ** 2)
water_per_sq_meter = 1.4
total_water = int(pond_area * water_per_sq_meter)
print("Total amount of water in the pond (without decimals):", total_water)

# 2.3 Calculate speed
distance = 490  # meters
time = 7 * 60   # seconds (7 minutes converted to seconds)
speed = int(distance / time)
print("Speed in meters per second:", speed)
