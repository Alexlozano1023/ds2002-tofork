#!/usr/bin/env python3
import os
fav_color = input("What is your favorite color? ")
birth_year = input("What year were you born? ")
hobby = input("What is your favorite hobby? ")
os.environ["FAV_COLOR"] = fav_color
os.environ["BIRTH_YEAR"] = birth_year
os.environ["HOBBY"] = hobby
print("\nStored Environment Variables:")
print("Favorite Color:", os.getenv("FAV_COLOR"))
print("Birth Year:", os.getenv("BIRTH_YEAR"))
print("Hobby:", os.getenv("HOBBY"))

