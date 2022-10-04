
def get_countdown_as_text_using_for(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0 using a for loop
    """
    countdown = []
    for n in range(start_value, 0, -1):
      countdown.append(n)

def get_countdown_as_text_using_while(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0 using a while loop
    """
    countdown = []
    while start_value > -1:
      countdown.append(start_value)
      start_value -= 1


get_countdown_as_text_using_for()
get_countdown_as_text_using_while()


