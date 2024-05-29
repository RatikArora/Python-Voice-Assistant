from AppOpener import open, close, mklist, give_appnames
# appnames = give_appnames() # Save appnames as dictionary
# print(appnames)
# # if 'brave' in appnames:
# # open('brave',throw_error=True)
def appopen(key):
    try:
        open(key,match_closest=True,throw_error=True)
    except:
        print("wrong syntax spoken try again")
def appclose(key):
    try:
        close(key,match_closest=True,throw_error=True)
    except:
        print("wrong syntax spoken try again")