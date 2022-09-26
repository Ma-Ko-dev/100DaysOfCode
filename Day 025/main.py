import turtle
import pandas

# constants
FONT = ('Arial', 8, 'normal')
ALIGN = "center"


# function
def move_text(text: str, x: int, y: int):
    """This function displays the name of a state and moves it to a specific location. Needs the state name as string
       and an x and y position as integer. Returns nothing."""
    new_text = turtle.Turtle()
    new_text.penup()
    new_text.ht()
    new_text.goto(x, y)
    new_text.write(text, align=ALIGN, font=FONT)


# set up the data
data = pandas.read_csv("us-states-game-start/50_states.csv")

# set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "us-states-game-start/blank_states_img.gif"
screen.addshape(img)
screen.setup(width=725, height=491)
turtle.shape(img)
running = True
guessed = []
to_learn = []
state_list = data.state.to_list()

while running:
    # getting user data
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What's another state's name?").\
        title()

    # exits the game
    if answer_state == "Exit":
        for state in state_list:
            if state not in guessed:
                to_learn.append(state)
        new_csv = pandas.DataFrame(to_learn)
        new_csv.to_csv("us-states-game-start/states_to_learn.csv")
        running = False

    # checking for user data
    if not data[data.state == answer_state].empty:
        answer = data[data.state == answer_state]
        guessed.append(answer_state)
        move_text(answer_state, int(answer.x), int(answer.y))

screen.exitonclick()
