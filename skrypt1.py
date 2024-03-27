from os import getcwd
import czas
import importlib
import time

# print("hello world")


current_path = getcwd()

print(czas.aktualny_czas)
time.sleep(20)
print(czas.aktualny_czas)

importlib.reload(czas)

print(czas.aktualny_czas)