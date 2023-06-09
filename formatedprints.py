def print_format(rates):
    rounded = "{:.2f}".format(rates[2])
    if rates[4]:
        print(f"\033[1;32;49m{rounded}\033[0m")
    else:
        print(f"\033[1;31;49m{rounded}\033[0m")


def print_history(db):
    for item in db:
        rounded = "{:.2f}".format(item[2])
        if item[4]:
            print(
                f"{item[3]} {item[0]} {item[1]} \033[1;32;49m{rounded}\033[0m")
        else:
            print(
                f"{item[3]} {item[0]} {item[1]} \033[1;31;49m{rounded}\033[0m")
