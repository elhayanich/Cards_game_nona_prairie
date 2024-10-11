import random

# création des cartes
tt_les_cartes = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

# début de la partie (ca devra devenir une fonction)
def partie(strat_humain, strat_robot):
    # melange des cartes
    random.shuffle(tt_les_cartes)
    # distribution
    state = {
        "robot hand": tt_les_cartes[:5],
        "human hand": tt_les_cartes[5:],
        "point robot": 0,
        "point humain": 0,
        "tour": 0,
        "CR": None,
        "CH": None,
        "winner": ""
    }
    for i in range(1, 6):
        state["tour"] += 1
        state["CR"] = None
        state["CH"] = None
        state["CR"] = strat_robot(state)
        state["CH"] = strat_humain(state)
        if state["CR"] >= state["CH"]:
            state["point robot"] += 1
        else:
            state["point humain"] += 1
    # déterminer le gagnant (il faudra ici retrouner le resultat de la partie)
    if state["point robot"] > state["point humain"]:
        state['winner']= "robot"
    else:
        state['winner']= "human"
    return state

def plays(n, strat_humain, strat_robot):
    tt_parties = []
    for _ in range(n):
        tt_parties.append(partie(strat_humain, strat_robot))
    return tt_parties



import strat
print(
    plays(n = 10,
          strat_humain = strat.coucou,
          strat_robot = strat.coucou
          )
    )

