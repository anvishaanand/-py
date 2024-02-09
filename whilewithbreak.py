# Example of a while loop with break
var = 0
while True:  # Infinite loop
    print( var)
    var += 1

    if var>= 5:
        break  # Exit the loop if count is greater than or equal to 5

print("Loop finished.")