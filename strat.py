def coucou(state):
    # si je suis l'humain
    if state["CR"] != None:
        # je joue une carte qui gagne
        for c in state["human hand"]:
            if c > state["CR"]:
                state["human hand"].remove(c)
                return c
        # sinon je joue ma plus petite
        c = min(state["human hand"])
        state["human hand"].remove(c)
        return c
    # si je suis le robot
    # je joue ma plus grosse
    carte = max(state["robot hand"])
    state["robot hand"].remove(carte)
    return carte