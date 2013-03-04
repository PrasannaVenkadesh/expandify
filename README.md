Today People are present everywhere in Internet, let it be Social networks, IRC's, Mailing lists, etc.,
People on IRC's & Social Network uses IS/CS - Internet Slang / Computer Slang
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

It gives back you in complete phrase when you press ENTER and then copy paste in your Email or Mailing list.

My preffered way is to use xclip

		$./expandify.py | xclip -sel clip

Pipelining the output to xclip automatically copies the text to your clipboard which saves your time of copying (much more lazier), now all you need to do is to paste it wherever you like.

