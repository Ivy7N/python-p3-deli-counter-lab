katz_deli = []
def line():
    if not katz_deli:
        print("The line is curreently empty.")
    else:
        current_line = ", ".join(f"{index + 1}. {name}" for index, name in enumerate(katz_deli))
        print(f"The line is currently: {current_line}")

def take_a_number(line, name):
    line.append(name)
    position = len(line)
    print(f"Welcome, {name}. You are number {position} in  line.")

def now_serving(line):
    if not line:
        print("There is nobody waiting to be served!")
    else:
        serving_person = line.pop(0)
        print(f"Now serving {serving_person}.")

take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)
take_a_number(katz_deli, "Matz")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)