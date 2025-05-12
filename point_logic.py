import time

num_replace = {
    "K": 1000,
    "M": 1000000,
    "B": 1000000000
}


def pure_number(string, number):
    """
    :param string: String with an abbreviations for a thousand, million, billion. ("k", "m", "b")
    :param number: Int
    :return: Returns the pure integer without abbreviations or commas for betting.
    """
    mult = 1.0
    if string in num_replace:
        x = num_replace[string]
        mult *= x
        return int(number * mult)


def get_points(current_points):
    """
    get_points and pure_number work in tandem to return an integer from our displayed channel points.
    :param current_points:
    :return: An integer
    """
    if "K" in current_points:
        num = float(current_points.split("K")[0])
        character = current_points[len(current_points) - 1:]
        current_points = pure_number(string=character, number=num)
    elif "M" in current_points:
        num = float(current_points.split("M")[0])
        character = current_points[len(current_points) - 1:]
        current_points = pure_number(string=character, number=num)
    return int(current_points)


def how_much_to_bet(six_p, current_loop):
    """
    :param six_p: 6.25% of our total
    :param current_loop: Current loop iteration
    :return: 6.25% of our total * the current loop
    """
    if current_loop == 1:
        return six_p
    elif current_loop == 2:
        return six_p 
    elif current_loop == 3:
        return six_p
    elif current_loop == 4:
        return six_p


def time_set(total_time):
    """
    Sleeps until there are only 5 seconds remaining on an active prediction.
    
    :param total_time: Total time remaining on an active prediction in "mm:ss" format.
                       If total_time starts with "Prediction", the function returns immediately.
    :return: None
    """
    # Check if total_time indicates a non-numeric value.
    if total_time.startswith("Prediction"):
        return

    # Split the total_time string at the colon.
    minutes_str, seconds_str = total_time.split(":")
    minutes = int(minutes_str)
    seconds = int(seconds_str)
    
    # Calculate total time in seconds.
    total_seconds = minutes * 60 + seconds
    
    # If total time is 5 seconds or less, there's no sleeping to be done.
    if total_seconds <= 5:
        return
    
    # Sleep for total_seconds minus 5 seconds, so that 5 seconds remain.
    sleep_time = total_seconds - 5
    time.sleep(sleep_time)
