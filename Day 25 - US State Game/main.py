import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state_writer = turtle.Turtle()
state_writer.hideturtle()
state_writer.penup()

# Use to get coordinates of mouse
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

state_data = pandas.read_csv("50_states.csv")
states = state_data["state"].to_list()

correct_answers = 0
correct_guesses = []

while correct_answers != 50:
    answer_state = screen.textinput(title=f"{correct_answers}/50 Correct", prompt="What's another State's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in states:
        row = state_data[state_data.state == answer_state]
        x = row.x.item()
        y = row.y.item()
        state_writer.goto(x, y)
        state_writer.write(answer_state)
        correct_answers += 1
        correct_guesses.append(answer_state)


missing_states = []
for state in states:
    if state not in correct_guesses:
        missing_states.append(state)
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")
