import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

t.shape(image)

cordinates = pd.read_csv("50_states.csv")
cordinates["state"] = cordinates["state"].str.lower()
# print(cordinates[cordinates["state"] == answer_state.lower()][["x", "y"]])
all_states = cordinates["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?")

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states, columns=["States"])
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state.lower() in all_states and answer_state.lower() not in guessed_state:
        guessed_state.append(answer_state)
        state_data = cordinates[cordinates["state"] == answer_state.lower()]
        print(state_data.x.item())
        x = state_data.x.item()
        y = state_data.y.item()
        new_state = t.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x, y)
        new_state.write(answer_state)



t.mainloop()
