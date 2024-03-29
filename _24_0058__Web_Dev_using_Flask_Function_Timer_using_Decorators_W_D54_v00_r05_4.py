import time

current_time = time.time()
print(f"\nNow in seconds is: {current_time}")  # seconds since 12:00am on Jan 1st, 1970

# write your code below 👇
def outter_function(main_function):
    def speed_calc_decorator():

        start_time_processing = time.time()
        print(f"\nStarting time for {main_function.__name__} is: {start_time_processing}")

        executes_main_function_and_stores_result = main_function()

        end_time_processing = time.time()
        print(f"Ending time for {main_function.__name__} is: {end_time_processing}")

        # calculates the time difference to get the timer for each function:
        time_duration = end_time_processing - start_time_processing

        # prints the final value of `i` for each function
        print(f"Total execution time: My program counted {executes_main_function_and_stores_result} total integers for {main_function.__name__} in {time_duration} seconds")

        return executes_main_function_and_stores_result

    return speed_calc_decorator

@outter_function
def fast_function():
    for i in range(1000000):
        i * i
    return i+1  # return the final value of i+1

@outter_function
def slow_function():
    for i in range(10000000):
        i * i
    return i+1  # return the final value of i+1

fast_function()
slow_function()
