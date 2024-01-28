for amount_loaded in range(0, 101, 5):
    print(amount_loaded)
    if amount_loaded == 25:
        print("Your are 1/4 of the way there!")
    elif amount_loaded == 50:
        print("Your are 1/2 of the way there!")
    elif amount_loaded == 75:
        print("Your are 3/4 of the way there!")
    elif amount_loaded == 100:
        print("Loading Complete!")