from classes import *
how_it_works = [
    [
        r"A guitar is a device which produces notes from the 12 tone equal temperament system.",

        r"Frets are the metal bars that can be found on the fretboard, by pressing our finger on the frets we pin one part of the string to the fret so that when the string is plucked the string vibrates at a certain frequency.",

        r"The construction of the guitar is made so that when you move inward by one fret, the new tone that is produced is a single semitone higher than the previous note, and also when you move outward by one fret the pitch decreases by one semitone."
    ]
]


conventions = [
    [
        r"From here on out we will say that when you move towards the center of the guitar, this is called inward movement, and in the opposite direction will be called outward movement. This type of movement will be called stringwise movement",

        r"We will also call the other type of movement, that is movement where you stay on the same fret but change strings fretwise movement, and we will say if you move towards the thickest string, you are moving down by n strings, and if you move towards the smaller string you go up by $n$ strings",

        r"We will specify a fret number by calling the open string fret 0, and subsequent frets (moving inward) by increasing integers."
    ]
]

tuning = [
    [
        r"In the standard tuning the largest string is tuned to a frequency of $82.4\text{Hz} = 440 \cdot  2^{-2}\cdot 2^\frac{4}{12}$, in our system that is $\overline{4_{\cdot\cdot}}$. ",

        r"Then for the next lowest string we can define it in terms of the previous string, that is we take $\overline{4_{\cdot\cdot}}$ and add 5 semitones to it. So in other words the next thickest string is $\overline{9_{\cdot\cdot}}$.",

        r"Likewise, we jump by another $5$ semitones to get to the $\overline{2_\cdot}$ string, then add another 5 semitones to get to $\overline{7_\cdot}$.",
        "Now comes something different, we add 4 semitones this time to get to $\overline{11_\cdot}$, but then moving to the thinnest string moves us up 5 semitones from $\overline{11_\cdot}$, so that makes $\overline{4}$ the highest string."
    ],
    [
        r"To sum that all up, the consecutive jumps are simply $5, 5, 5, 4, 5$, and just considering the notes, we would have:",
        "$\overline{4_{\cdot\cdot}} \ (\stackrel{\leftrightharpoons}{\pm5}) \ \overline{9_{\cdot\cdot}} \ (\stackrel{\leftrightharpoons}{\pm5}) \ \overline{2_\cdot} \ (\stackrel{\leftrightharpoons}{\pm5}) \ \overline{7_\cdot} \ (\stackrel{\leftrightharpoons}{\pm4}) \ \overline{11_\cdot} \ (\stackrel{\leftrightharpoons}{\pm5}) \ \overline{4}$.",
        r"Notice that I've added plus or minus, this is because  depending on the direction you move you are either adding that many semitones or taking away that many semitones",
        r"So instead of memorizing all the notes explicitly, we can just remember $5, 5, 5, 4, 5$ and that the lowest string is $ \overline{4}$ , this way we can synthesize the information when needed and over time we will implicitly remember the string notes.",
    ],
    [
        r"Without considerations for the octave a note lives in, we will generally write the string notes as $\overline{4}_L, \overline{9}, \overline{2}, \overline{7}, \overline{11}, \overline{4}_H$, where L stands for Low and H stands for High.",

        r"At this point we have all the information we need to understand the following fretboard diagram"
    ]
]

# load in the fretboard diagram

#def create_fretboard_text_with_animation():

fretboard_examples_with_animation_data = [
    (r"Based on the notation we have developed thus far, we can see that if you play the $0$-th fret on the $\overline{7}$ string, you get the note $\overline{7}$ and  we can see that by moving inward by one fret we should get $\overline{7} + 1 = \overline{8}$. ",[Voicing([[0,3, "\overline{7}"]], 1), Voicing([[1,3,"\overline{8}"]], 1)]),
    ( r"In general  if we're on string $X$ (where $X \in \left\{\overline{4}_L, \overline{9}, \overline{2}, \overline{7}, \overline{11}, \overline{4}_H  \right\}$ ) and we move to fret $n$, then the note produced is simply $X + n$.", []),
    (r"So if $X = \overline{9}$  and $n = 5$ the new note would be $\overline{9} + 5 = \overline{9 + 5} = \overline{2}$", [Voicing([[0, 1, "\overline{9}"]], 1), Voicing([[5, 1, "\overline{2}"]], 1)]),
    (r"Next up we will understand horizontal movement in more detail.", []),
    ( r"It's clear by construction that if you play $\overline{4}_L$ and then $\overline{9}$ that it is 5 semitones higher.", [Voicing([[0,0,"\overline{4}"], [0,1,"\overline{9}"]], 1)]),
    (r"It may be seen that if you play on fret $n$ of $\overline{4}_L$, and then fret $n$ of $\overline{9}$, that the second note is also 5 semitones higher, further it can be seen that this holds for any other two consecutively fretted notes, except for one going from string $\overline{7}$ to $\overline{11}$, because this one will have a gap size of 4 semitones.", [Voicing([[8, 0, "\overline{0}"],[8, 1, "\overline{5}"]], 1),Voicing([[2, 1, "\overline{11}"],[2,2,"\overline{4}"]], 1),Voicing([[12,3, "\overline{7}"],[12,4, "\overline{11}"]], 1)]),
    (r"To understand why this phenomena holds, will employ intervals. Let's start by writing our previous observations in interval notation.",[])
]

fretboard_examples = [
    [
    r"First we can see that $I(\overline{4}, \overline{9}) = 5$, and that the notes produced by playing the $n$-th fret on $\overline{4}_L$ would be $\overline{4 + n}$ , and then the $n$-th fret on the $\overline{9}$ string would be $ \overline{9 + n}$.",

    r"Then to calculate the interval between the two notes we use the formula for the interval between any two notes we derived, so we get",

    r"$I\left( \overline{4 + n}, \overline{9 + n}\right) = \left( 9 + n \right)  -  \left( 4 + n \right) = 9 - 4 = 5$",
    ],

    [
        r"So in general we can see that between any two open strings $ \overline{k}, \overline{j}$ we have:",

    r"$I\left( \overline{k + n}, \overline{j + n}\right) = \left( j + n \right)  -  \left( k + n \right) = j - k = I\left(\overline{k},\overline{j}\right)$",

    r"So this allows us to move two fingers on any two strings inwards and outwards the same number of frets without changing the interval between the two notes. We will advance this idea further later on when we start constructing chords.",
    ]
  ]

anchor_point_examples_with_animation_data = [
    (r"So let's suppose our anchor point is on the $\overline{4}_L$ string, then moving up 1 string increases us by 5 semitones, if we move up another string we increase our previous note by another 5 semitones, that is in relation to the $\overline{4}_L$ string, this new note is 10 semitones higher, to get to the $\overline{7}$ string from the $\overline{4}_L$ string you will add $(5 + 5 + 5) = 3$ semitones", []),
    ("By filling out this whole fret position, we get ...",[Voicing([[10, 0, "0"], [10, 1, "5"], [10, 2, "10"], [10, 3, "3"], [10, 4, "7"], [10, 5, "0"]], 1)]),
    (r"So horizontal movement from an anchor point on the $\overline{4}_H$ creates the following intervallic pattern: $0, 5, 10, 3, 7, 0$ but generates these notes on the fretboard",[Voicing([[10, 0, "\overline{2}"], [10, 1, "\overline{7}"], [10, 2, "\overline{0}"], [10, 3, "\overline{5}"], [10, 4, "\overline{9}"], [10, 5, "\overline{2}"]], 1)]),
    (r"Notice the duality of intervals and notes, we can either think of this row by the notes that it generates or by the intervals above the base tone $\overline{2}$",[Voicing([[10, 0, "0"], [10, 1, "5"], [10, 2, "10"], [10, 3, "3"], [10, 4, "7"], [10, 5, "0"]], 1), Voicing([[10, 0, "\overline{2}"], [10, 1, "\overline{7}"], [10, 2, "\overline{0}"], [10, 3, "\overline{5}"], [10, 4, "\overline{9}"], [10, 5, "\overline{2}"]], 1)]),
    (r"Let's do another example, let's generate the line of the $16$-th fret with an anchor point on string $\overline{11}$, we can start by realizing that $ 16  \equiv 4 \ (\bmod \ 12) $, so we just have to add 4 semitones to the open string to find the new note. So that note would be $\overline{3}$. This time we will only draw the intervals",[Voicing([[16, 0, "5"], [16, 1, "10"], [16, 2, "3"], [16, 3, "8"], [16, 4, "0"], [16, 5, "5"]], 1)]),
    (r"We call these ``lines generated by an anchor point'', or simply ``lines'' and they are fundamental to being able to construct interval collections on the fly (improvising chords)", []),
]

# line template [[[f, 0, "x"], [f, 1, "x"], [f, 2, "x"], [f, 3, "x"], [f, 4, "x"], [f, 5, "x"]]]

[Voicing([[19, 0, "2"], [19, 1, "7"], [19, 2, "0"], [19, 3, "5"], [19, 4, "9"], [19, 5, "2"]], 1)]

constructing_basic_interval_collections_fretboard_examples = [
    (r"As you know from the previous video we have interval collections, these specify a set of notes (or intervals - more on that in another video) to play by giving a root note and a set of intervals above that root note, in the standard system these are called chords.", []),
    (r"Let's construct a few interval collections.", []),
    (r"$\overline{2} \mid 0 \ 4 \ 7 \ 11$: In the standard system this would be called a D major 7th chord.", []),
    (r"The first step to building this will be to find ourselves a $\overline{2}$ on the fretboard. Let's find it on the $\overline{7}$ string.", []),
    (r"We know that $\overline{7} + 7 = \overline{14} = \overline{2}$, so the seventh fret on this string will be our starting location.", [Voicing([[7, 2, "\overline{2}"]], 1)]),
    (r"By recalling our pattern of $5, 5, 5, 4, 5$, and that $\overline{2}$ is 0 semitones away from $\overline{2}$ we can generate this line", [Voicing([[7, 3, "0"],[7, 4, "4"], [7, 5, "9"], [7, 2, "7"], [7, 1, "2"], [7, 0, "9"]], 1)]),
    (r"We can see that this line already contains 3 out of the 4 intervals we need, namely it has $0, 4, 7$ since all we need is the $11$ we can modify the string which represents the interval $9$ by moving two frets up. And we've made our interval collection", [Voicing([[7, 3, "0"],[7, 4, "4"], [7, 5, "9"], [7, 2, "7"], [7, 1, "2"], [7, 0, "9"]], 1), Voicing([[7, 3, "0"],[7, 4, "4"], [9, 5, "11"], [7, 2, "7"]], 1)]),
    (r"Also notice that there are many ways to generate the same interval collection, each possible way to construct it is called a voicing. For example, let's make the same interval collection but on a different string. Let's make it on the $\overline{11}$ string, where we can see that $\overline{11} + 3 = \overline{2}$, so we construct a line on the third fret", [Voicing([[3,4,"0"], [3,5,"5"], [3,3,"8"], [3,2,"3"], [3,1,"10"], [3,0,"5"]], 1)]),
    (r"Notice that our line is incorrect if $\overline{4}_L$ and $\overline{4}_H$ dont't have the same intervals, this is because $I(\overline{4}_L, \overline{4}_H) = 24 \equiv 0$", [Voicing([[3,4,"0"], [3,5,"5"], [3,3,"8"], [3,2,"3"], [3,1,"10"], [3,0,"5"]], 1)]),
    (r"We observe that this line doesn't contain any of the intervals we need aside from 0. But we see that the following modfications are possible $5 \mapsto 7, 8 \mapsto 11, 3 \mapsto 4$, and so we get this possibility:",[Voicing([[3,4,"0"], [3,5,"5"], [3,3,"8"], [3,2,"3"], [3,1,"10"], [3,0,"5"]], 1), Voicing([[3,4,"0"], [5,5,"7"], [6,3,"11"], [4,2,"4"] ], 1)] ),
    (r"Finally we will consider another line that we haven't considered so far in our constructions.", []),
    (r"We must not forget that at any point in time, no matter where our fretting hand is positioned, we always have access to the open strings, so to have even more freedom with our constructions, we should also consider these intervals. I recommend doing this once you are comfortable creating RICs using the standard line.", []),
    (r"To understand what these intervals are, we must find the interval which is formed between the open strings note, and our current root. Let's say in this example that we are looking to construct the interval collection $\overline{9} \mid 0 \ 3 \ 7 \ 10$", []),
    (r"So, we can measure the interval of each of the open strings against $\overline{9}$.", []),
    (r"$I(9, 4) = 4 - 9 \equiv 7, \ I(9, 9) = 9 - 9 \equiv 0, \ I(9, 2) = 2 - 9 \equiv 5, \ I(9, 7) = 7 - 9 \equiv 10, \ I(9, 11) = 11 - 9 \equiv 2, \ I(9, 4) = 4 - 9 \equiv 7$ (as with the lowest string). Therefore we can see that many of the open strings will be available to us", [Voicing([[0, 0, "7"], [0, 1, "0"], [0, 2, "5"], [0, 3, "10"], [0, 4, "2"], [0, 5, "7"]], 1)]),
    (r"This time, let's have our root on string $\overline{2}$, where we know that being on fret 7 will give us $\overline{9}$, but not only that, also fret $12 + 7$ will work too, because $\overline{2} + 7 + 12 \equiv \overline{2} + 7$, so let's start on fret $19$", [Voicing([[19, 2, "0"]], 1)]),
    (r"Since we have all the intervals on fret 0 available to us as well, we can consider it along with the line generated at this new fret, so we would have", [Voicing([[0, 0, "7"], [0, 1, "0"], [0, 2, "5"], [0, 3, "10"], [0, 4, "2"], [0, 5, "7"],[19, 0, "2"], [19, 1, "7"], [19, 2, "0"], [19, 3, "5"], [19, 4, "9"], [19, 5, "2"]], 1)] ),
    (r"Let's use the $7$ and $0$ from the $0$-th fret and let's modify $0 \mapsto 10$ and   $5 \mapsto 3$ on from the $19$-th fret, so we get this voicing.", [Voicing([[0, 0, "7"], [0, 1, "0"], [0, 2, "5"], [0, 3, "10"], [0, 4, "2"], [0, 5, "7"],[19, 0, "2"], [19, 1, "7"], [19, 2, "0"], [19, 3, "5"], [19, 4, "9"], [19, 5, "2"]], 1), Voicing([[17, 2, "10"], [17, 3, "3"], [0, 5, "7"], [0,1,"0"]], 1)]),
]


conclusion = [
    [
        r"I hope you enjoyed learning the basics of the guitar.",
        r"If you have questions or want to discuss, join the zulip chat",
    ]
]

guitar_basics_data = [ how_it_works, conventions, tuning, fretboard_examples]
