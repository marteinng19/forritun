#distance from the sun on 25. september 2009:
dist_from_sun = 16637e6
#speed traveling from the sun in mph
speed_from_sun = 38241

days_since_str = input("Number of days after 9/25/09: ")
days_since_float = float(days_since_str)

hours_since = days_since_float*24
#calculate the distance in different units
distance_miles_exact = hours_since*speed_from_sun+dist_from_sun
distance_km_exact = distance_miles_exact*1.609344
distance_AU_exact = distance_miles_exact/92955887.6
#make all the numbers round
distance_miles_round = round(distance_miles_exact)
distance_km_round = round(distance_km_exact)
distance_AU_round = round(distance_AU_exact)

print("Miles from the sun:", distance_miles_round)
print("Kilometers from the sun:", distance_km_round)
print("AU from the sun:", distance_AU_round)