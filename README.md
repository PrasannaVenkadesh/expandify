Today People are present everywhere in Internet, let it be Social networks, IRC's, Mailing lists, etc.,
People on IRC's & Social Network uses IS/CS - Internet Slang / Computer Slang;
People on Mailing list and official Emails uses - Complete English

But our fingers are more used to IS/CS and even I am lazy to type the complete phrase. So I use expandify.

What it is?
===========
Expandify expands most commonly used IS/CS to complete english phrase, so that you type IS/CS and you get in full form.

How to Use it?
==============
In your Terminal

		$./expandify.py

and type one or more sentences without a line break.

Example:
		
		$./expandify.py
		AFAIK & IMPOV this is True

and press ENTER to see what happens!, then copy paste where you want it to be in complete english

My preffered way is to use xclip

		$./expandify.py | xclip -sel clip

Pipelining the output to xclip automatically copies the text to your clipboard which saves your time of copying (much more lazier), now all you need to do is to paste it wherever you like.

Lot of IS are missing?
======================
Yes, indeed they are missing, I am adding them one by one, and if you have free time or atleast make some free time to add here if you wish. Just Fork it; add it; send me a merge request ;-)
