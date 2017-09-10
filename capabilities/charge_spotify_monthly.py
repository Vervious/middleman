import datetime

# on the 10th day of every month, charge everyone $2.5
def charge_spotify_monthly(state):
    month =  datetime.datetime.today().month
    if ("spotify-last-paid-month" in state and state["spotify-last-paid-month"] == month):
        return
    if (datetime.datetime.today().day != 10):
        return
    state["ben-$"] = state.get("ben-$", 0) + 15
    state["wei-$"] = state.get("weilian-$", 0) - 2.5
    state["mic-$"] = state.get("weilian-$", 0) - 2.5
    state["ray-$"] = state.get("weilian-$", 0) - 2.5
    state["lucia-$"] = state.get("weilian-$", 0) - 2.5
    state["spotify-last-paid-month"] = month
