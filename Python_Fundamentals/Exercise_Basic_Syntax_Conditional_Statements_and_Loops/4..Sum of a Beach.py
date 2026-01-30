text = input().lower()  # make everything lowercase

sand_count = text.count("sand")
water_count = text.count("water")
fish_count = text.count("fish")
sun_count = text.count("sun")

finale_count = (sand_count + water_count + fish_count + sun_count)
print(finale_count)
