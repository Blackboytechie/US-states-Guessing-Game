import turtle
import pandas as pd
from states import States

t = turtle.Turtle()
s = turtle.Screen()
st_obj = States()

s.title('The Indian States Game')
s.setup(width=700, height=600)
img = "blank_states_img.gif"
s.addshape(img)
t.shape(img)
is_game_on = True
while is_game_on:
    ans_states = s.textinput(title=f"guess states ({st_obj.guessed}/{st_obj.total_states})", prompt='Whats the next '
                                                                                               'states?').title()
    if ans_states == 'Exit':
        break
    if len(st_obj.guessed_states) < 50:
        st_obj.create_state(ans_states)
    else:
        is_game_on = False
unguessed = [x for x in st_obj.all_states if x not in st_obj.guessed_states]
# unguessed = []
# unguessed = st_obj.all_states.copy()
# for x in st_obj.guessed_states:
#     unguessed.remove(x)
unguessed_dist = {"states": unguessed}
unguessed_data = pd.DataFrame(unguessed_dist)
unguessed_data.to_csv("states_to_learn.csv")
print(unguessed_dist)