repeat_symbol = r'\%'

blues_base = [
    ["0 | 0 3 7 10", repeat_symbol,  repeat_symbol, repeat_symbol],
    ["5 | 0 3 7 10", repeat_symbol,  "0 | 0 3 7 10", repeat_symbol],  
    ["7 | 0 3 7 10", "5 | 0 3 7 10",  "0 | 0 3 7 10", repeat_symbol]
]

lady_bird = [
    ["0 | 0 4 7 11", repeat_symbol, "5 | 0 3 7 10", "10 | 0 4 7 10"],
    ["0 | 0 4 7 11", repeat_symbol, "10 | 0 3 7 10","3 | 0 4 7 10"],  
    ["8 | 0 4 7 11", repeat_symbol, "9 | 0 3 7 10", "2 | 0 4 7 10"],
    ["2 | 0 3 7 10", "7 | 0 4 7 10", ["0 | 0 4 7 11", "3 | 0 4 7 11"], ["8 | 0 4 7 11", "1 | 0 4 7 11"]]
]

take_the_a_train = [
    ["0 | 0 4 7 11", repeat_symbol, "2 | 0 4 6 10", repeat_symbol],
    ["2 | 0 3 7 10", "7 | 0 4 7 10", "0 | 0 4 7 11",  [repeat_symbol, "0 | 0 4 7 10"]],  
    ["5 | 0 4 7 11", repeat_symbol, repeat_symbol, repeat_symbol],
    ["2 | 0 4 7 10",repeat_symbol, "2 | 0 3 7 10", "7 | 0 4 7 10 1"]
]

there_will_never_be_another_you = [
    ["0 | 0 4 7 11", repeat_symbol, "11 | 0 3 6 10", "4 | 0 4 7 10"],
    ["9 | 0 3 7 10", repeat_symbol, "7 | 0 3 7 10", "0 | 0 4 7 10"],

    ["5 | 0 4 7 11", "5 | 0 3 7 9", "0 | 0 4 7 11", "9 | 0 3 7 10"],
    ["2 | 0 4 7 10", repeat_symbol, "2 | 0 3 7 10", "7 | 0 4 7 10"],

    ["0 | 0 4 7 11", repeat_symbol, "11 | 0 3 6 10", "4 | 0 4 7 10"],
    ["9 | 0 3 7 10", repeat_symbol, "7 | 0 3 7 10", "0 | 0 4 7 10"],

    ["5 | 0 4 7 11", "5 | 0 3 7 9", "0 | 0 4 7 11", ["6 | 0 3 6 10", "11 | 0 4 7 10"]],
    [["4 | 0 3 7 10", "5 | 0 4 7 11"], ["4 | 0 3 7 10", "9 | 0 4 7 10"], ["2 | 0 3 7 10", "7 | 0 4 7 10"], ["0 | 0 4 7 11", "7 | 0 4 7 10"]]
]

autumn_leaves = [
    ["2 | 0 3 7 10", "7 | 0 4 7 10", "0 | 0 4 7 11", "5 | 0 4 7 11"],
    ["11 | 0 3 7 10", "4 | 0 4 7 10", "9 | 0 3 7 9", repeat_symbol],
    ["11 | 0 3 7 10", "4 | 0 4 7 10", "9 | 0 3 7 9", repeat_symbol],
    ["2 | 0 3 7 10", "7 | 0 4 7 10", "0 | 0 4 7 11", repeat_symbol],
    ["11 | 0 3 7 10", "4 | 0 4 7 10", ["9 | 0 3 7 10", "8 | 0 4 7 10"],["7 | 0 3 7 10", "6 | 0 4 7 10"]],
    ["5 | 0 4 7 11", "4 | 0 4 7 10", "9 | 0 3 7 9", repeat_symbol]
]

all_the_things_you_are = [
    ["5 | 0 3 7 10", "10 | 0 3 7 10", "3 | 0 4 7 10", "8 | 0 4 7 11"],
    ["1 | 0 4 7 11", "7 | 0 4 7 10", "0 | 0 4 7 11", repeat_symbol],
    ["0 | 0 3 7 10", "5 | 0 3 7 10", "10 | 0 4 7 10", "3 | 0 4 7 11"],
    ["8 | 0 4 7 11", "2 | 0 4 7 10", "7 | 0 4 7 11", repeat_symbol],
    ["9 | 0 3 7 10", "2 | 0 4 7 10", "7 | 0 4 7 11", repeat_symbol],
    ["6 | 0 3 6 10", "10 | 0 4 7 10 1", "4 | 0 4 7 11", "0 | 0 4 7 10 8"],
    ["5 | 0 3 7 10", "10 | 0 3 7 10", "3 | 0 4 7 10", "8 | 0 4 7 11"],
    ["1 | 0 4 7 11", "6 | 0 4 7 10", "0 | 0 3 7 10", "11 | 0 3 6 9"],
    ["10 | 0 3 7 10", "3 | 0 4 7 10", "8 | 0 4 7 11", "0 | 0 4 7 10 1"],
]

one_six_two_five = [
    ["0 | 0 4 7 11", "9 | 0 3 7 10", "2 | 0 3 7 10", "7 | 0 4 7 10"]
]

all_diatonics = [
    [r"\text{Major}", r"\text{Minor}", r"\text{Harmonic}", r"\text{Melodic}"],
    ["0 | 0 4 7 11", "0 | 0 3 7 10", "0 | 0 3 7 11", "0 | 0 3 7 11"],
    ["2 | 0 3 7 10", "2 | 0 3 6 10", "2 | 0 3 6 10", "2 | 0 3 7 10"],
    ["4 | 0 3 7 10", "3 | 0 4 7 11", "3 | 0 4 8 11", "3 | 0 4 8 11"],
    ["5 | 0 4 7 11", "5 | 0 3 7 10", "5 | 0 3 7 10", "5 | 0 4 7 10"],
    ["7 | 0 4 7 10", "7 | 0 3 7 10", "7 | 0 4 7 10", "7 | 0 4 7 10"],
    ["9 | 0 3 7 10", "8 | 0 4 7 11", "8 | 0 4 7 11", "9 | 0 3 6 10"],
    ["11 | 0 3 6 10", "10 | 0 4 7 10", "11| 0 3 6 9", "11 | 0 3 6 10"]
]



#https://www.youtube.com/watch?v=VP1Aj4csH58

neo_soul_VP1Aj4csH58 = [
        [["8 | 0 4 7 11", "11 | 0 3 6 9"], "0 | 0 3 7 10",  ["8 | 0 4 7 11", "7 | 0 4 7 10"], "0 | 0 3 7 10"]
]


