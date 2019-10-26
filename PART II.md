# PART 2

## You asked me to design a spoken english to written english conversion system that can be continuously matured as you discover more and more conversion rules.

I've made the code work with the 'Replacement Rulebook.txt' for that very reason. You can add or subtract rules as per
your liking.

You could censor foul language by typing **FUCK=****** 

Even expand texting abbreviations like **IYKWIM=if you know what I mean** or **LOL=laughing out loud**

## For example, you may not have taken care of punctuation rules in the previous part of the exercise. Can you design in a way that such rules can be easily added without having to re-test all the previous rule implementations?

I'd actually suggest POS tagging for correct grammatical text output. Know what part of speech each word belongs to will make 
punctuating much easier. 

**Eg. A bunch of common nouns grouped in a sentence would need commas to separate them.**

Even without POS tags, simpler modifications to code can be made to punctuate certain words properly.

**Eg. Convert all "i" to "I" or convert "im" to "I'm"**

Some of these grammatic modifications are already present in my rulebook, you can add as many as you can think of and as long as 
the .txt above is not changed, you won't need to re-test all the previous rule implementations.
