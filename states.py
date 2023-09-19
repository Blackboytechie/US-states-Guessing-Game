import turtle
import pandas as pd


class States:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.all_states = []
        self.guessed = 0
        self.guessed_states = []
        self.total_states = 0

    def create_state(self, ans_states):
        data = pd.read_csv("50_states.csv")
        self.all_states = data.state.to_list()
        self.total_states = len(data.state)
        if ans_states in self.all_states and ans_states not in self.guessed_states:
            self.guessed_states.append(ans_states)
            state_data = data[data.state == ans_states]
            self.guessed += 1
            self.x = int(state_data.x)
            self.y = int(state_data.y)
            st = turtle.Turtle()
            st.hideturtle()
            st.penup()
            st.goto(self.x, self.y)
            st.write(f"{ans_states}", move=True, align="center", font=("Aerial", 10, "normal"))
        elif ans_states in self.guessed_states:
            print("you already guessed this")
        else:
            print("spell correct!!!")
