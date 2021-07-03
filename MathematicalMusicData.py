definitions = {
"Canonical Mapping": r'''
\begin{tabular}{ccccccccccccc} 
	C& $\cdot$ & D& $\cdot$ & E& F& $\cdot$ & G& $\cdot$ & A& $\cdot$ & B & C \\
	$\updownarrow $ & $\updownarrow $ & $\updownarrow $ & $\updownarrow $ & $\updownarrow $ & $\updownarrow $ & $\updownarrow $ & $\updownarrow $ & $\updownarrow $ & $\updownarrow $ & $\updownarrow $ & $\updownarrow $ & $\updownarrow$ \\
	$\overline{0} $ & $\overline{1} $ & $\overline{2} $ & $\overline{3} $ & $\overline{4} $ & $\overline{5} $ & $\overline{6} $ & $\overline{7} $ & $\overline{8} $ & $\overline{9} $ & $\overline{10} $ & $\overline{11} $ & $\overline{0}$\\
\end{tabular}

					''',
"Adding a Number to a Note": r'''
For any $\alpha \in \mathbb{Z} = \{ \dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$

	\[
	\overline{x}  +  \alpha \stackrel{\mathtt{D}}{=} \overline{\left( x  +  \alpha \right)}
	\]
''',

"Interval": r'''
 The interval from  $ \overline{x}$ to $ \overline{y }$ is the number of semitones you have to add to $ \overline{x}$ to get to $ \overline{y}$. By noticing that the following equation holds

	\[
	\overline{x}  +  \left( y  -  x \right) = \overline{x  +  y  -  x} = \overline{y}
	\]

  We know that in general the interval from $ \overline{x}$  to $ \overline{y}$ is $y  - x$ . And we define 


	\[
	I\left( \overline{x}, \overline{y}\right) \stackrel{\mathtt{D}}{=} (y  -  x)
	\]

  For example: $I\left( \overline{4}, \overline{9}\right) = 9  -  4 = 5$ 
''',

"Rooted Interval Collection": r'''
  To specify a collection of notes we may use a root tone $\overline{r}$ and intervals $x_i$, we write:

	\[
		  \overline{r} \mid x_{1} , x_{2} , \dotsc  , x_{n - 1} , x_{n}
	\]

	Which generates the notes: 

	\[
	\overline{r  +  x_{1}}, \overline{r  +  x_{2}}, \ldots, \overline{r  +  x_{n}}
    \]

  Examples

	$\overline{0} \mid 0, 4, 7, 11$ generates the notes $ \overline{0}, \overline{4}, \overline{7}, \overline{11} \leftrightarrow C, E, G, B$ which is a C major 7th chord.

	$ \overline{5} \mid 0, 3, 7$ generates the notes $ \overline{5}, \overline{8}, \overline{0} \leftrightarrow F, Ab, C$ which is a F minor triad '''
}

######## START OF CONTENT ############

before_canonical = [
    "One of the fundamental ideas in music is that notes are cyclic. After going up 12 notes you end up at a new note which has the same name",
    "So our first step into the a new notation is to mirror this cyclic pattern with numbers.",
    "Let's start by making an equivalent mapping into the standard system.",
]
before_adding = [
    r"In the number system, the equivalent question is, which note is 3 steps up from $\overline{4}$",
    r"Analagous to last time we would have: $\overline{4},\overline{5},\overline{6},\overline{7}$ and find that the new note is $\overline{7}$",
    r"Alternatively we could have added 3 to 4. This motivates a new definition.",
]

before_interval = [
    r"In the new  system we can answer this question as follows:",
    r"We would convert the two notes: $C^{\sharp} = \overline{1}$ and $A^{\flat} = \overline{8}$",
    r"We know you have to add 7 to 1 to get 8, in other words we are solving the equation $\overline{1} + z = \overline{8}$ where it is clear that $z = 7$",
    r"It will now be convenient to define an interval.",
]

before_ric = [
    r"Then we can easily consider other RICs, such as $A^{\sharp}$ major or equivalently the set of intervals 0, 2, 4, 5, 7, 9, 11 and root note $\overline{8}$",
    r"$\overline{8 + 0},\overline{8 + 2},\overline{8 + 4},\overline{8 + 5},\overline{8 + 7},\overline{8 + 9},\overline{8 + 11} = \overline{8},\overline{10},\overline{0},\overline{1},\overline{3},\overline{5},\overline{7}$"
]

before_def_page = [before_canonical, before_adding, before_interval, before_ric]

pages_of_content = [
before_canonical,
# Insert canonical_mapping 
[
    r"Note that due to the circular nature of the mapping, $\overline{12}$ is the same note name as $\overline{0}$ and that $\overline{-3}$ would be the same as $\overline{9}$",
    r"More generally, we can see that two notes $\overline{x}$ and $\overline{y}$ represent the same note name when they have the same remainder upon division by 12",
    r"Mathematically we write $ x \equiv y  \ (\bmod \ 12) $ and say that $x$ and $y$ are congruent modulo 12.",
    r"Since every integer is congruent to one of the following numbers:  $0, 1, \dots,  11$,  we will usually refrain from speaking about notes that are outside of that range"
],
[
    "Another fundamental thing in music is the idea that we can measure the interval between any two notes",
    "The interval is defined as the number of atomic steps we need to get from one note to another",
    "The atomic step size is defined to be a semitone - the smallest step in the 12 tone equal temperament system (more on that in another video)"
],
[

    r"In the standard system we can ask ourselves the question, if we have the note E, which note is $3$ steps up from here?",
    r"So if we move up to 3 times: E, F, F$^{\sharp}$ G",
    r"And we can see that G is $3$ steps up from E.",
],
before_adding,
# insert adding_a_number_to_a_note
[
    r"Let's now compare the standard and mathematical system by answering another similar question:",
    r"How many steps do we need to add to C$^{\sharp}$ to get to A$^{\flat}$",
    r"In order to know this quickly, experience in the standard system will be of use, or manually counting the spaces",
    r"In this way we can step through each note: C$^{\sharp}$, D, D$^{\sharp}$, E, F, F$^{\sharp}$, G, G$^{\sharp}$ = A$^{\flat}$ to see that we need to add 7 steps to get there.",
],
before_interval,
# insert interval
[
    r"We will now focus on tonal music, this type of music defines a type of structure by declaring a set of notes which will be used predomiantly throughout the piece (a key)",
    r"When we talk about keys, we refer to them by using a root tone, one such key is called C major",
    r"It consists of the notes C, D, E, F, G, A, B. The reason why we declare it using a root tone is that this is the note, which will be emphasized predominantly throughout the piece.",
    r"We will now delve into the structure of a major key."
],
[
    r"One way of defining a key is to give a set of relative intervals. So for the major scale those set of intervals would be 2, 2, 1, 2, 2, 2, 1.",
    r"The way we construct the notes is by adding that interval to the last note we generated. So for example, we would start at $C=\overline{0}$ and then add 2 to get to $\overline{2}$, then add 2 to get to $\overline{4}$ then add 1 to get to $\overline{5}$ and so on.", 
r"After creating all the notes,  we will have generated: $\overline{0},\overline{2},\overline{4},\overline{5},\overline{7},\overline{9},\overline{11}$",
    r"To generate different major keys, we simply start this process on a different root note"
],
[

    r"Alternatively we could have simply defined a set of intervals with respect to the root tone, rather than using relative ones.",
    r"Therefore to specify the major scale we could specify the set of intervals 0, 2, 4, 5, 7, 9, 11 and a root note",
    r"Notice how this also generates the same notes, when the root tone is $\overline{0}$",
    r"We will call this collection of information a rooted interval collection, and RIC for short"
],
before_ric,
# insert RIC
[
    r"If you have gotten this far, great!",
    r"You now have a set of tools to interact with the standard musical system from a mathematical point of view.",
    r"If you have any questions or want to discuss, join the zulip chat.",
]
]
