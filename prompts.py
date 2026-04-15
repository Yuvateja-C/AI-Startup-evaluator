def get_prompt(mode):
    if mode == "Shark":
        return "You are a ruthless investor like Shark Tank judge. Be harsh."
    elif mode == "Strict":
        return "You are a strict startup evaluator."
    else:
        return "You are a friendly startup mentor."