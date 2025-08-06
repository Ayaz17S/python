def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "az", power="bha")
print_kwargs(name = "az")
print_kwargs(name="az",cla="c",bd="s")