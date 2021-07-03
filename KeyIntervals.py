video_title = "Key Intervals"

definitions = {

"Key Interval": r'''
    This is a way to specify a certain interval above a specified note, usually this note will be fundamental to the underlying tonal structure, such as the key's root tone. Thus given a key's root $ \overline{\mathcal{K}}$

	\[
	\boxed{x^{\hspace{-0.1cm}\urcorner} = \overline{\mathcal{K}} + x}
	\]

  For example, if $ \overline{\mathcal{K}} = \overline{9}$, then

	$3^{\hspace{-0.1cm}\urcorner} = \overline{9} + 3 = \overline{0}$
''',

}

######## START OF CONTENT ############

before_key_intervals = [
 r"Let's say $\mathcal{K} =  \overline{0} \mid 0 \ 2 \ 4 \ 5 \ 7 \ 9 \ 11$ (C major) and we are looking at the RIC $\overline{0} \mid 0 \ 4 \ 7 \ 11$ .",

 r"Now we change keys and we're now in the key of $ \mathcal{K} =  \overline{9} \mid 0 \ 2 \ 4 \ 5 \ 7 \ 9 \ 11$ (A major), to specify the same kind of interval collection (one that starts on the key's root) we would write $ \overline{9} \mid 0 \ 4 \ 7 \ 11$.",

 r"This notation doesn't really convey what's going on. In this situation $ \overline{9} \mid 0 \ 4 \ 7 \ 11$ is going to have the same effect as $ \overline{0} \mid 0 \ 4 \ 7 \ 11$ as they're both a chord which is constructed of the same intervals from the root of the key. ",

 r"To be able to support this type of equality we will develop a new definition."
]


before_def_page = [before_key_intervals]

pages_of_content = [
[
r"So far we have been using rooted interval notation to specify a set of notes.",

r"We will develop a similar notation that takes one step back from that.",

r"To understand what I mean we will start with some examples."
],
[
 r"Consider any melody, if you add $n$ to every one of the notes in the melody you have a melody that uses a different set of notes (as long as $n \not\equiv 0 \ (\bmod \ 12)$)",
 r"Even though the set of notes has changed, something is still invariant. Namely the intervals measured between consecutive notes is still the same. As in the guitar example, it is because",
r"$ I\left(\overline{x}  +  n, \overline{y}  + n\right) =  \left( y  -  n \right)  -  \left( x  -  n \right) =  y  -  x =  I\left(\overline{x}, \overline{y}\right)$"
],
[
 r"Additionally if you played a solo, and then that same solo, but with $n$ added to every note, most listeners would say that your new solo was the same as your old one.",
 r"Fundamentally all I'm saying is that when we listen to the same song in different key, we are still able to identify the song and it should convey the same intervallic information.",
 r"Let's now focus on a way we can improve our notation by looking at how the old notation performs.",
],
before_key_intervals,
[
 r"Now we have a method that allows us to see equality between songs, melodies and chords (RICs) even when the notes that are used are different.",
 r"This will allow us to find patterns in songs that are at a deeper level then just the notes used, and allows you to not focus on the key, but rather on the intervals above the keys root.",
 r"This type of notation is useful for when you are concerned with the qualities of notes rather than the pitches.",
 r"In a later video I will attempt to formally define the quality of a set of notes."
], 
[
 r"I hope you enjoyed learning about this new notation, it will be quite fundamental in other videos I make from now onward.",
 r"Thanks, and if you have questions, join the zulip chat."
]

]
