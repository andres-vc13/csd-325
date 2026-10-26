def countdown(bottles):
    #range function for countdown#
    for remaining in range(bottles, 0, -1):
        if remaining == 1:
            print("Time to buy more beer!")
        else:
            print(f"{remaining} bottles of beer on the wall, {remaining} bottles of beer!")
            if remaining - 1 == 1:
                print("Take one down and pass it around, 1 bottle of...")
            else:
                print(f"Take one down and pass it around, {remaining - 1} bottles of beer on the wall!")

#verify input for whole numbers#
def main():
    while True:
        try:
            bottles = int(input("How many bottles of beer are on the wall? "))
            if bottles < 1:
                print("There's got to be some beer, somewhere!?")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    countdown(bottles)

#run program#
if __name__ == "__main__":
    main()