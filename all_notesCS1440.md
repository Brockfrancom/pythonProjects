

Lecture 1: Nov_12/notes.md
================================================================

# CS1440 - Mon Nov 12

# Announcements

## ACM-W CS Study Night

All are welcome
Wednesday, November 14
ENGR 302 from 5pm - 11pm
Food and snacks provided


## Assignment 5 due date moved back

Assignment #5 is now due on Wednesday 11/28, a week after the beginning of
Thanksgiving break.


### Clarification added to Assignment #5


Find usage examples at the bottom of the assignment description on Canvas

https://usu.instructure.com/courses/518265/assignments/2547057#usage


We are scheduled to discuss the Abstract Factory pattern this Wednesday.

In preparation for this discussion, the assignment has been updated with
hyperlinks to an article about this concept.  Read through the linked article
before our next meeting.

The assignment also asks that you create a new types of fractal.  The
assignment has been updated with hyperlinks to articles describing other
fractal types, including Mandelbrot^3, Mandelbrot^4, Phoenix, BurningShip, and
BurningShipJulia.

We will discuss how new types of fractals fit into this program next time.





## Thanks for your feedback on Assignment 4

Thank you to those who took the Fractal Assignment Improvement Survey.  Your
feedback has been very helpful.  If you haven't yet taken the anonymous survey,
it's open through this Wednesday, Nov 14th.

https://usu.instructure.com/courses/518265/quizzes/690905



## IDEA Surveys coming soon

The regular three week long window for IDEA Student Rating of Instruction (SRI)
opens next week.  You will receive a personalized email with a link to complete
your survey on November 19th.

Your IDEA feedback is very important to me, and each semester I take many
useful suggestions and incorporate them into my future courses.  Much of what I
do I owe to your suggestions.  The more input I get from you the better I am
able to improve as an instructor.  My goal is to reach 80% participation.

To that end I am offering 50 points of sweet, sweet *extra credit* for your
response.  Your responses remain anonymous, and I will not even see them until
after finals week.  The extra credit is automatically applied to your grade by
Canvas within 48 hours of your taking the anonymous survey.

When you take the survey, please take into consideration the IDEA learning
outcomes which this course has been designed to meet:

* Learn fundamental principles, generalizations, or theories
* Learn to Apply Course Material to improve thinking, problem solving, and decisions
* Develop specific skills, competencies, and points of view needed by professionals in the field



----------------------------------------------------------------------------
## Exam 2 Review

======================================================================
Right now, are you able to see your answers on Exam #0? (IP Filter)
What about Exam #1? (no IP Filter)
======================================================================


### Advanced git

[Getting the most out of git](https://usu.instructure.com/courses/518265/pages/getting-the-most-out-of-git)

* What does `HEAD~4` mean?
* What does `master~2` mean?
* What does `Assn4~12` mean?
* Manipulating and viewing branches
    * How to list branches?
    * How to list *all* branches, including those from remote repositories?
    * How to create branches in git?
    * How to move between branches?
    * How to show which commits belong to which branch?
    * How to delete branches, both safely and forcibly?
* Undoing whoopsies
    * How to restore *uncommitted* changes (a.k.a. discard uncommitted changes)
    * How to restore *committed but unpushed* changes
    * How to restore *committed and pushed* changes
    * Understand the limits of what git is able to restore for you
* How does one view the `reflog`?
* Which git command can tell you who wrote a line of code, and when they did it?



### Programming paradigms

* Identify the defining characteristics of these important programming paradigms:
    * Imperative
    * Procedural
    * Structured
    * Modular (Like raviolli)
    * Functional
    * Declarative
    * Object-Oriented



### Assigned Readings

#### *The Mythical Man-Month* "Plan to throw one away"

* Why does Brooks suggest that you first build a throwaway prototype?
* Which specific techniques for "designing a system for change" does Brooks suggest?
    * Careful modularization
    * Precise and complete definition of intermodule interfaces
    * Complete documentation
* Why is it highly probable that a bug fix will introduce another bug?
* Why does Brooks think that systems become harder to maintain over time?



#### *The Mythical Man-Month* "The Second System Effect "

* An architect's first work is apt to be spare and clean
* Why is the second system the most dangerous system to build?
* How to avoid the second-system effect?



#### *Pragmatic Programmer* Chapter 5 

* What is The Law of Demeter for Functions?
    * What are its benefits?
    * What are its costs?
* What is Metadata?
* What three benefits do Hunt and Thomas give for metadata-driven, highly-configurable systems?



#### *Pragmatic Programmer* Chapter 6

* As programs evolve, must we reconsider our earlier design decisions?
    * Why?
* What is refactoring at its heart?
* Should your refactor *and* add functionality at the same time (e.g. within the same git commit?)
* Before refactoring should you create unit tests?  Why or why not?



### Review from Exam #1

* What is a software failure?
* What is a software error?
* Can your testing be thorough enough to detect *all* errors in a program?
* Characteristics of dictionaries
    * what may they contain
    * what order are their contents in
    * performance profile vs. other data structures
* Python uses ______ sorting
* Programming Products, Programming Systems, Programming Systems Products


Lecture 2: Nov_14/notes.md
================================================================

# CS1440 - Wed Nov 14

# Announcements

## ACM-W CS Study Night

All are welcome
Wednesday, November 14
ENGR 302 from 5pm - 11pm
Food and snacks provided


# Topics:
1. What is a Design Pattern?
2. What problem does the Abstract Factory Pattern solve?




----------------------------------------------------------------------------
## 1. What is a Design Pattern?

There are many ways in which we might reuse code.  What are some ways you know about?

* Copy & Paste
* Functions
* Libraries (standard or otherwise)
* Loops
* Classes
* Templates
* Polymorphism



### Code Reuse

[5: Code Reuse](https://usu.instructure.com/courses/518265/pages/5-readings-and-resources#code-reuse)



* Which forms of reuse are the most flexible?
    + Copy & Paste: just drop it in and go
    + Functions: reduce many lines of inline code to a single function call


* Which forms of reuse take the most work to utilize?
    + Copy & Paste: may need to rename variables
    + Design Patterns: require some effort to apply to your situation


* How will I know when to use which types of reuse?  Or, what is "Good Reuse"
  and what is "Bad Reuse"?
  
### Table from _Think Like a Programmer_ by V. Anton Spraul:

| Good Reuse                                    | Bad Reuse                                                              |
|-----------------------------------------------|------------------------------------------------------------------------|
|Promotes understanding                         | Enables risky behaviors                                                |
|Following a blueprint                          | Copying someone else’s work                                            |
|Magnifies and extends your capabilities        | Falsifies your capabilities                                            |
|Helps you learn                                | Helps you avoid learning                                               |
|Saves time in the short term and the long term | May save time in the short term but may lengthen time in the long term |
|Results in a working program                   | May result in a program that doesn’t work anyway                       |


Blindly copying code from Stack Overflow is an example of a risky behavior -
how do you know that code wasn't planted there by a Russian agent?  This
research paper demonstrates that well-intentioned Stack Overflow answers can
introduce security issues into your code:

[Secure Coding Practices in Java: Challenges and Vulnerabilities](https://arxiv.org/pdf/1709.09970.pdf)


* Are some forms of reuse better than others?  If so, what makes them so?
    + The answer to this is "it depends".  Take into consideration your
      experience and level of understanding, your time constraints and the
      impact your decision will have on your team.


* Why do professors sometimes insist that you don't use standard libraries in
  homework assignments?
    + Your goal in school isn't to create robust and elegant code.  It is to
      learn the principles behind creating robust and elegant code.  Anybody
      can blindly follow SO advice.  What the world really needs are software
      engineers who can bring wisdom and experience.
    + Besides, [blindly following online advice](https://arxiv.org/pdf/1709.09970.pdf)
      has security costs.



### What, then, is a Design Pattern?

[5: Design Patterns](https://usu.instructure.com/courses/518265/pages/5-readings-and-resources#design-patterns)

[Design Patterns on SourceMaking](https://sourcemaking.com/design_patterns)




----------------------------------------------------------------------------
## 2. What problem does the Abstract Factory Pattern solve?

Problem: my original `main.py` was 125 lines of code long (not counting
comments or blank lines).  It embodied the following concepts:

1. Import all of my concrete Fractal and Gradient classes
2. Accept user input from the command line
3. Read a fractal configuration file and convert it into a configuration object
4. Choose which fractal to create
4. Read an optional 2nd command-line parameter and choose a subclass of Gradient to create
5. Decide what to do with invalid input
6. Create and display the fractal image


Solution: My refactored `main.py` is now 39 lines long.  After removing
unneeded imports, comments and blank lines there are 15 lines of code.
It now has the following responsibilities:

1. Accept user input from the command line
2. Decide what to do with invalid input
3. Use factories to create a fractal and a gradient object
4. Create and display the fractal image

The idea isn't to be brief for brevity's sake.  The point is that `main.py` has
one responsibility: to provide the UI.  The other code was and is still
necessary.  Moving the code into Factory classes follows the principle of
*encapsulation* where each responsibility is fenced in to its own area.  This
is what allows `main.py` to serve a single purpose.

We didn't reduce the amount of work our entire system needs to do by moving the
code into another file.  However, by moving this responsibility into another
location (from the *nice* part of town into the industrial section, so to
speak) we have made our program easier to extend and update.

As an example, suppose that later on we add a new sort of fractal to our
system.  When that happens we will leave `main.py` alone and instead add a few
lines to `FractalFactory.py`.  The other team which is responsible for making
the GUI are likewise isolated from this change, and won't need to update their
code because of our work.

> One of my most productive days was throwing away 1000 lines of code.
> -- Ken Thompson

> Deleted code is debugged code.
> -- Jeff Sickel


[Abstract Factory Pattern on SourceMaking](https://sourcemaking.com/design_patterns/abstract_factory)


Lecture 3: Nov_16/notes.md
================================================================

# CS1440 - Fri Nov 16

# Announcements

## HackUSU is today!
Eccles Conference Center
Make sure you're registered on https://hackusu.org



============================================================================
# Call on 3 designated questioners
============================================================================




# Topics:
1. What is a code smell?
2. What's the big deal with global variables?



----------------------------------------------------------------------------
## 1. What is a code smell?

> In computer programming, a code smell is any characteristic in the source
> code of a program that possibly indicates a deeper problem.  Determining what
> is and is not a code smell is subjective, and varies by language, developer,
> and development methodology.
>
> -- [Wikipedia](https://en.wikipedia.org/wiki/Code_smell)


Consider the programming paradigms we have learned about

* Imperative (Can lead to spaghetti code)
* Procedural
* Structured
* Modular (Ravioli code, not spaghetti)
* Functional
* Declarative
* Object-Oriented

One way to think of a code smell would be a construct which might be
appropriate under one paradigm but goes against the expectations and
best-practices in another paradigm.

For example, this wouldn't necessarily be considered *bad* in imperative
programming, but it's quite uncalled for in Python:

[The Python Charmer](http://thedailywtf.com/articles/Python-Charmer)

The DailyWTF is a programming humor site dedicated to underappreciated
programmers and the muck they must walk through in their daily work.




### Non-idiomatic code indicative of a Python n00b

This code isn't wrong *per se*:

	if x == 4:
		a()
	elif x == 5:
		b()
	elif x == 6:
		c()
	elif x == 7:
		d()
	elif x == 8:
		e()

but could be expressed more elegantly by combining two Python features,
*dictionaries* and *first-class functions*:

	mapping = {
		4: a,
		5: b,
		6: c,
		7: d,
		8: e,
	}
	mapping[x]()



Noticing patterns like this is one way you can get in the head of another
programmer; the if-elif tree was obviously written by a C/C++/Java/C#
programmer who really wanted to create a switch statement (a feature
conspicuously missing from Python).  A Python/Ruby/Perl/JavaScript programmer
writing in one a staticall-typed language will make similarly conspicuous
gaffes.

Perhaps this "forensic code analysis" is not immediately practical; you could
use a tool such as `git blame` to more accurately establish authorship over a
piece of code, or use `Gource` to make a neat movie out of it.  But it is data,
and programmers are nothing if not data-driven.

* [Gource in Bloom](https://www.youtube.com/watch?v=NjUuAuBcoqs)
* [Gource](https://gource.io/)


### A catalogue of Code Smells

[Code Smells on SourceMaking](https://sourcemaking.com/refactoring/smells)



### Somebody collected an entire repository of smelly Python code

[Python Code Disasters](https://github.com/sobolevn/python-code-disasters.git)

    git clone https://github.com/sobolevn/python-code-disasters.git
Cloning into 'python-code-disasters'...

Let's look at a few examples.  With your neighbors list on your *mud cards*
what you find to be problematic with these examples and why:

* python-code-disasters/python/my_first_calculator.py
* python-code-disasters/python/send_email.py
* python-code-disasters/python/PhyRe.py





----------------------------------------------------------------------------
## 2. What's the big deal with global variables?

![One does not simply...](one_does_not_simply.jpg)

<Demo: readability/>


![I, too, like to live dangerously](live_dangerously.png)


Lecture 4: Nov_19/notes.md
================================================================

# CS1440 - Mon Nov 19

# Announcements

============================================================================
# Call on 3 designated questioners
============================================================================

# Topics:
1. Exam 2 recap 
2. Assignment 5 final discussion
3. How does `git bisect` help me win the debugging battle?



----------------------------------------------------------------------------
## 1. Exam 2 recap

__Question 2__ (65% answered correctly)

* Q:  A software failure is
* A:  Runtime behavior that is not expected


__Question 21__ (70% answered correctly)

* Q:  Which well-known techniques for designing a system for change does Brooks list?
      (Select all that apply)
* A:
    + Complete documentation
    + Precise and complete definition of intermodule interfaces
    + Careful modularization
    + Extensive Subroutining


__Question 27__ (79% answered correctly)

* Q:  Simply put, The Law of Demeter for Functions is
* A:  Minimize coupling between modules


__Quesiton 30__ (68% answered correctly)

* Q:  What are the benefits cited by Hunt and Thomas for metadata-driven,
      highly-configurable systems?
      (Select all that apply)
* A:
    + It forces you to create a more robust, abstract design by deferring details
    + It forces you to decouple your design, resulting in a more flexible program
    + You can customize your program without rewriting or recompiling it




----------------------------------------------------------------------------
## 2. Assignment 5 final discussion

This assignment is due on 11/28, the Wednesday following the break.  We will
need to move on into the final module at that time, so if you have any
outstanding questions about this assignment, now's the time to bring them up.



### FractalFactory and GradientFactory may be modules

If you have already written these to be classes, don't change it now.  It
doesn't really matter *how* you implement these, so long as they simplify 


----------------------------------------------------------------------------
## 3. Debugging


> If debugging is the process of removing bugs, then programming must be the
> process of putting them in.                                        
> 
> -- Edsger W. Dijkstra



### Origin of the term

The terms "bug" and "debugging" are popularly attributed to Admiral Grace
Hopper in the 1940s.

While she was working on a Mark II computer at Harvard University, her
associates discovered a moth stuck in a relay and thereby impeding operation,
whereupon she remarked that they were "debugging" the system. However, the term
"bug", in the sense of "technical error", dates back at least to 1878 and
Thomas Edison.

In the ACM's digital library, the term "debugging" is first used in three
papers from 1952 ACM National Meetings. Two of the three use the term
in quotation marks. By 1963 "debugging" was a common enough term to be
mentioned in passing without explanation on page 1 of the CTSS manual.


### Debugging
The process of finding software errors (the causes of failures) and then
correcting those errors.



### How do I debug anything in 4 easy steps?

### 3.1. Test the software to find failures.

It is a best practice to *not* have programmers do their own testing. As
paradoxical as this may sound, a programmer's expectations about what the
program is and how it should work prevents them from really pushing the
boundaries and being effective at finding problems.

Testing provides critical information about failures:

* The circumstance in which the failure occurs
* Test cases which reliably reproduce the failure



### 3.2. Uncover the error which gives rise to the failure.

Once the failure is known, the developer can use a combination of techniques to
uncover the cause and produce a fix.

* Interactive debugging - stepping through a program with the aid of a tool
  which lets the developer inspect the internal state of the program as it runs
    - variable inspector
    - execute function calls
    - examine memory, CPU registers
    - call stack
    - watchpoints

* Remote debugging - interactive debugging of a program running on a different
  system from the debugger. For example, you may connect to another system over
  the internet and attach an interactive debugger. Another example is debugging
  an embedded device from a PC

* Protocol analysis - using diagnostic tools to analyze network messages
  sent/received by the system, examine interactions with external hardware or
  an OS.

* Post-mortem debugging - debugging a program after it has already crashed. An
  example of this is inspecting a core dump file. Also includes reading an
  error message in the log file or on the console after a crash.

* Print debugging - causing the program to print messages to a console or a log
  file which indicate how a program's execution evolves over time.

* "Wolf fence" algorithm - locate a bug in a program by dividing it into
  halves, further partitioning the half containing the bug until you pinpoint
  it.  You might do this with breakpoints, log messages, or specially-crafted
  function calls (hooks).  Git bisect is an example of this technique applied
  to the revision history of a project.


The original article
[The "Wolf Fence" algorithm for debugging](https://dl.acm.org/citation.cfm?id=358695)

Oh, it's behind a paywall :(

[Use the cheatcode to log into the USU library](http://dist.lib.usu.edu/login?url=http://portal.acm.org/dl.cfm?coll=portal)

Then access it at the first link



### 3.3. Create a fix

Once the problem is uncovered, fix it (if possible). Hopefully it's simply a
problem with your code and *not* with your design.

At this point you may elect to put *assertions* into the code which cause the
program to terminate with a specific error message, alerting developers (or
users) when this specific error recurrs.



### 3.4. Re-run the tests

Return to the test cases created in step #3.1 to ensure that

* The failure no long exists, once the error has been found and corrected.

* The fix did not introduce new errors.  This is harder to guarantee and
  necessitates further testing.

Many programmers, after investing significant time and effort into fixing a
bug, fail at this step.  Don't undermine all of your work by slacking off in
the home stretch!



--------------------------------------------------------------------------------
## 4. How does `git bisect` help me win the debugging battle?

Like everything else we've done this semester, we can apply our general
problem-solving techniques to the problem of debugging.

* Always Have a Plan
* Restate the Problem
* Divide the Problem
* Start With What You Know
* Reduce the Problem
* Look For Analogies
* Experiment
* Don't Get Frustrated



Git's commit history of your code is an invaluable resource to help understand
the evolution of your project. However, it can become an unmanageable resource
due to its size.

Git bisect is a power tool which tames the unmanageable size of your
repository. Use it to perform a *binary search* on your git repo to identify
the commit which introduced a bug.


We can use `git bisect` on the source code for the Vim text editor to find when
a particular bug was introduced

[Vim no longer de-indents shell script code](https://github.com/vim/vim/issues/2151#issuecomment-331970759)


### Let's track this bug down for ourselves

    $ git clone https://github.com/vim/vim.git
    $ cd vim
    $ ./configure --prefix=/usr
    $ make -j$(nproc)
    $ src/vim -N -u NONE -i NONE -c 'so $VIMRUNTIME/indent/sh.vim'


If I enter in this text:
if this;
    then
    fi

Vim should do the (de)indenting for me. In the latest version of Vim this bug
is fixed, so what we see is the correct behavior.


The comment on GitHub mentions that when a user updated to Vim version
8.0.1127, this auto-indent feature broke.  Let's go back to that commit and
reproduce the reported error.


I'll use some shell functions so that this process is more convenient.

    $ function rebuild() { ./configure --prefix=/usr; make -j$(nproc); }
    $ function testvim() { src/vim -N -u NONE -i NONE -c 'so runtime/indent/sh.vim'; }
    $ git checkout v8.0.1127
    $ rebuild


Ah, now we can see the problem.


### Perform a bisect

To use `git bisect` you must have three things:

1. A commit in which the code worked
2. A commit where the bug is evident
3. A test to determine the presence of the bug.


From the bug report, we read that Gary noticed the problem once he built
8.0.1127, and that it wasn't there in version 8.0.691. Somewhere between those
two builds the bug was created.

That's only 436 git commits to test... this shouldn't take too long.


To begin a bisect, checkout one of the boundary commits and run this command:

	$ git bisect start


Tell git whether this commit is a good one or a bad one. We'll assume that
we're starting from a place where the bug is present, and want to search back
in time to find where the bug was first introduced:

	$ git bisect bad


Next, tell git which commit represents the other boundary; this will be the
last commit which we know did not possess this bug:

	$ git bisect good v8.0.0691


Git will then take us to the commit right in the middle between our 'good' and
'bad' boundaries. We'll do whatever it takes to test the presence of the bug;
in class this involved re-building Vim, running it and typing some text to see
whether Vim automatically handled indentation.

When we observe the absence or presence of the bug, we tell git whether
this commit was a good one or a bad one by running either

	$ git bisect good

or

	$ git bisect bad

We repeat this process until git converges on the commit which introduced the
bug.

Once we're all done, we run

    $ git bisect reset

To tell git to restore our code to the way it was when we began with `git
bisect start`.



### Why this is awesome

Obviously, it's awesome because we were able to cover 436 commits in only 8
steps. `git bisect` is an example of the "Wolf Fence" debugging technique.

This technique works best when you create many small, focused commits. We can
ask the question "would it be easier to locate this bug if there were 1/10th as
many commits which were 10x larger?" 

The key to remember is that the hard part isn't locating the bad commit. The
key is that when we arrive at the bad commit our job's only just begun.

The difference between 436 commits and 43 commits isn't that great when we
apply a binary search. We can cover 436 commits in about 8 steps, and 43
commits in 5 steps.

If the commit which introduced the bug is small and focused on a single
feature, it won't take too much work to figure out what went wrong. Now imagine
that this commit involves 10x as many changes as before. How long will it take
you to evaluate 120 lines of code instead of 12 lines of code?


### TL;DR

Make many small commits instead of a few big ones!


Lecture 5: Nov_28/notes.md
================================================================

# CS1440 - Wed Nov 28

# Announcements

## CS Tutor Room Schedule Next Week
Next week is the last week for the CS Tutor room. There is one slight change in the regular schedule.

Monday from 4:30-5:30 the tutor room will be closed for a staff meeting.


============================================================================
# Call on 3 designated questioners
============================================================================

# Topics:
1. Assignment #6: Recursive Web Crawler
2. demo_urlparse.py: Anatomy of a URL
3. demo_requests.py: GETting data from the web
4. demo_beautifulsoup.py: Finding order in chaos




----------------------------------------------------------------------------
## 1. Assignment #6: Recursive Web Crawler


----------------------------------------------------------------------------
## 2. demo_urlparse.py: Anatomy of a URL


----------------------------------------------------------------------------
## 3. demo_requests.py: GETting data from the web


----------------------------------------------------------------------------
## 4. demo_beautifulsoup.py: Finding order in chaos




Lecture 6: Nov_30/notes.md
================================================================

# CS1440 - Fri Nov 30

# Announcements
# Advent of Code 2018
https://adventofcode.com/

Opens tomorrow night (12/1) @ midnight EST

# Topics:


## Recursion
What is recursion, really?


----------------------------------------------------------------------
## What is recursion, really?
     ___
    |_ _|n order to understand recursion,
     | |  one must first understand recursion.
    |___|


### Droste Effect
https://en.wikipedia.org/wiki/Droste_effect

https://www.youtube.com/watch?v=rDIos-t5Syo&feature=youtu.be&t=39s



https://en.wikipedia.org/wiki/Recursion_(computer_science)

Recursion is characterized by repetition through self-reference.

Repetition is a fundamental technique of computation, and programming languages
give us many ways to express the idea of "do this thing N times" or "do this
thing until it is done".  Thus far in your studies you have been using loops to
achieve this.  Here is a Python function which uses a loop to compute the Nth
Factorial:

    def loopFactorial(n):
        r = 1
        for i in range(1, n+1):
            r *= i
        return r


In this example we are *explicit* about

* What happens at each iteration of the loop
  (`i` takes on a value from 1 to n inclusive)

* When to stop looping
  (when i becomes equal to n+1)



But we weren't explicit about

* How control goes from the bottom of the loop back to the top

You've just come to accept that the amount of indentation controls the extent
of the loop, but you didn't have to tell the computer how to move from one
iteration to the next.


Using recursion means that we are explicit about everything that happens:

    def recursiveFactorial(n):
        if n <= 2:
            return n
        else:
            return n * recursiveFactorial(n - 1)

* What happens at each iteration of the loop 
  (At each loop we either return `n`, or the product of `n` with `recursiveFactorial(n - 1)`)


* When to stop looping
  (When `n` becomes less-than-or-equal to 2)

* How control goes from the bottom of the loop back to the top
  (Repetition happens when we call `recursiveFactorial(n - 1)`)

Instead of using the `range()` function to generate a list of numbers to loop
over, we start from `n` and count down with each successive call.
 


### Recursion: A beautiful and elegant way to solve all of life's problems

In the scheme of our problem-solving strategies, recursion is a means of
"Dividing the Problem" where you break the problem into do-able chunks.  Most
problems naturally contain smaller sub-problems.  Solving these smaller pieces
is progress.

Recursion means to apply a function repeatedly by calling itself from within
itself instead of using a loop to repeat the function's invocation.  With each
iteration of a loop we get one step closer to our desired solution.  Recursion
is the same, but instead of hitting the bottom of a loop we explicitly call a
routine to return to the beginning of the sequence of instructions we wish to
repeat.

In a recursive solution we use the program's call-stack as a data structure to
keep track of information needed by the computation as opposed to manually
maintaining this data.

Any iterative algorithm can be transformed into an equivalent recursive
algorithm and vice-versa, though going from recursion to iteration requires the
addition of an auxiliary data structure.


When is it appropriate to use recursion?
----------------------------------------


     _ _                                           _ _
    ( | ) To iterate is human, to recurse divine. ( | )
     V V                                           V V
                                    -- L. Peter Deutsch



Q: May we only apply recursion to problems which have the naturally occurring
property of recursion?

A: We can apply recursion to any problem for which it makes sense. For some
problems, like traversing a directory structure or crawling the WWW, a
recursive solution just feels "natural".  At other times the overhead of the
call stack doesn't justify a recursive solution.

As with many of the things we've studied in this class, we get to make a
judgement call by weighing the pros and cons of either approach.  Knowing
*when* to do something is as important as knowing *how* to do it.


V. Anton Spraul's "Big Recursive Idea"
--------------------------------------

If you follow certain conventions in your coding, you can pretend that no
recursion is taking place.

When you realize that a `while` or `for` statement is playing two roles
(testing and repeating) it is easier to think about how we might separate those
tasks into two lines of code.  Thus, we may more easily express any repetitive
process as a series of recursive function calls.

On the other hand, for those problems which themselves embody recursion,
recursive solutions tend to be simpler and easier than iterative solutions.  It
is possible to create an iterative solution to any recursive problem.  To do so
we must supply a data structure which fills the role of the call stack.



Head vs. Tail recursion
-----------------------

<Demo: recursion.py>

Consider the differences between recursiveCount() and recursiveCountBackward().
Where does the recursive call occur?

The recursive call happens *after* printing the number in recursiveCount(),
which results in printing the numbers in ascending order.  When the recursion
is the *last thing* done in the function it is called *Tail* recursion.

The recursive call happens *before* printing the number in
recursiveCountBackward(), resulting in the numbers appearing in the reverse
order from the former function.  When the recursion happens *before* the main
body of processing in a function it is known as *Head* recursion.


Consider 

* What's the difference to us?
  Not very much, besides the result being backwards.  For a function such as
  recursiveFactorial(), the result does not change when the order of operations
  is reversed.

* Is recursiveFactorial() an instance of head recursion or tail recursion?
  Is the call to `recursiveFactorial()` the very last thing to happen in this
  function?  No, it isn't.  The multiplication of `n` with the result of the
  call to `recursiveFactorial()` is the last thing to happen.  This function is
  *not* tail recursive.

* What's the difference to a compiler?
  It can make all of the difference in the world!  More on this on Monday.




Mutual recursion
----------------
A recursive function *may* call itself directly, but it doesn't have to.
"Mutual Recursion" happens when we have one function which calls another,
which ultimately results in the original function being called again.

Consider the functions oddCount() and evenCount().  'odd' calls 'even', which
in turn calls 'odd', and so on.  

Because one function is head recursive and the other function is tail
recursive, we find an interesting pattern in the output.

* Which of `oddCount()` and `evenCount()` is tail recursive?  


Wrapper functions
-----------------
For convenience we may define a function which provides a simpler interface to
another function.  Perhaps a function has lots of parameters, each of which
must have a very particular value.  Instead of requiring the user to memorize
tedious details such as this we may write a *wrapper* function to cover another
function call like a wrapper on candy.

Wrapper functions are quite common with recursive functions because the
parameters to a recursive function carry vital information and it is important
that they do not begin with the wrong value.  Wrapper functions are used in
cases where such a parameter has a default value that may be hard coded, 


Lecture 7: Dec_03/notes.md
================================================================

# CS1440 - Mon Dec 03

# Announcements

## Don't forget to take the IDEA survey

The window of opportunity is closing soon.
Don't pass up on your chance for extra credit!



# Topics:
1. Why do I make you use recursion in HW6?
2. Conquering Stack Overflow
3. Hands-on recursion



----------------------------------------------------------------------------
## 1. Why do I make you use recursion in HW6?

I asked you to think about this question last time.  What reasons did you come
up with?

* Expose you to a new way of thinking
* It's the easy way to solve this particular problem
* Recursion is a good habit to get into


For all of its mystery and seeming complexity, recursion can lend itself to
very short and elegant solutions to problems which have one of these
properties:

* The data structure underlying the problem is itself recursive

* You can identify a trivial "base case" *and* an inductive step which changes
  a complex case into something that's closer to being the base case.




Problems with these properties include:

* Search algorithms (i.e. a chess engine)

* Parsing programming languages (your compiler or interpreter is recursive)

* Traversing a recursive data structure


However, any iterative algorithm can be converted into an equivalent recursive
algorithm, even if the above properties don't necessarily apply.

Let's consider an algorithm with a straightforward iterative solution which may
be converted into a more elegant recursive form.


<Demo: change.py>




----------------------------------------------------------------------------
## 2. Conquering Stack Overflow

I think this is what most of you think using recursion is like:

[Look at this Blue Screen of DEATH](https://www.youtube.com/watch?v=L22keLHfEjc)

Some of you may be worried that recursion can use too much memory.
How far can we go before this limitation becomes a practical problem?

The answer is "it depends".

<Demo: depthfinder.py>



It depends upon how much memory your computer has, whether you're using head
recursion or tail recursion as well as which programming language you wrote the
recursive routine in.



### Compilers and recursion


Apart from the naturally recursive problem of compiling source code into a
program, what is the relationship between compilers and recursive programs?

You can find out what happens when we perform infinite recursion by playing
with the programs under the recursion/ subdirectory.

I have written the same program in 4 languages: Python3, C, C++ and
Scheme

<Demo: song/>

To try out the Scheme program you will need to install the Chicken Scheme interpreter.
On Debian-based Linux distributions you can install this by running:

    $ sudo apt install chicken-bin

Or, you can download pre-built package for your OS from
https://wiki.call-cc.org/platforms



### Tail Call Optimization

*Q*: Can our compiler save us from running out of memory?
*A*: Yes! It's called "Tail-Call Optimization" (TCO).

When the very last thing which a recursive function has to do is make the call
to itself, the compiler can treat that like a 'goto' and jump back to the top
of function, updating the value of the function parameters.

This works out-of-the-box for the C and Scheme programming languages.  For C++
it takes just a bit of coaxing to allow the complier to realize that it can
perform TCO.  Python3 just falls flat on its face :/




----------------------------------------------------------------------------
## 3. Hands-on recursion

### Merge Sort Algorithm

I need 15 volunteers to come fill the first 4 rows of the classroom like so:

    # # # # # # # #
     #   #   #   #
       #       #
           #

<Demo: MergeSort.pseudo>


Tips for thinking about problems recursively:
---------------------------------------------
* Start with what you know - this means to identify the base case(s).
  The base case(s) are states of the problem for which the answer to the
  problem are self-evident.

* Divide the problem - this means to break the problem into smaller chunks
  and solve those first.  Discover operations which transform your current
  state into one that is one step closer to a base case.

* Reduce the problem - add constraints to the problem such that you end up
  excluding extraneous, unneccesary details which complicate a recursive
  solution. Problems which may be divided into pieces which do not need to
  rely on each other's state are good candidates for a recursive solution;
  such recursive solutions could be run in a distributed system taking
  advantage of parallel processing.




## Can you find recursive solutions to these problems?

Scrabble tiles
--------------
* Detecting Palindromes ("level", "civic", "tacocat", "A man, a plan, a canal, Panama")
* Fisher-Yates Shuffle (an efficient way to mix up an ordered collection of items)
* Find all permutations of N tiles (order matters: {123, 132, 213, 231, 312, 321})
* Find all combination of N tiles  (order doesn't matter: {123} == {321})


Cards
-----
* Merge Sort (MergeSort.pseudo)
* Quick Sort
* Linear-Search
* Binary-Search


Towers of Hanoi
---------------
* The classical solution is recursive; can you find it?
  (Hint: begin with fewer disks)

* Can you devise an iterative solution?



Lecture 8: Dec_05/notes.md
================================================================

# CS1440 - Wed Dec 05

# Announcements

## The Utah DefCon group DC435 is starting in January!!!

DC435 meets at 7:00pm every First Thursday of every month at Bridgerland
Technology West Campus located at 1410 N 1000 W

I'm super excited about this, it's just what we need in the Valley.  I hope to
see all of you there on January 3rd.

[DC435](https://dc435.org/)


## Making a career in cybersecurity

I invited James and John Pope of [Pope Tech](https://pope.tech/) to be guest
lecturers in my web development class earlier this afternoon.  When speaking to
them after the lecture, it came up that many agencies and organizations are
facing a severe shortage of cybersecurity personnel.

Entry level wages are ~$60k, and this can go up as high as ~$120k with a few
years' experience.  

If you can pass a background test and a drug test, you could get a job with the
FBI today (a person who hires for the federal government told James that he
really likes to hire Utahans because they tend to not have problems passing
these sorts of tests.)

Notice that no mention of skills, training, or degrees is mentioned here.
The most important qualification (after passing the tests) is merely having an
*interest* in cybersecurity.

The jobs are out there.  Pull on your hoodie and go get 'em!



# Topics:
1. Thinking like a Programmer
2. Wisdom vs. Knowledge
3. Catalog your strengths and weaknesses
4. Suggested activities to continue your growth as a programmer
5. Things which have made me a better programmer



--------------------------------------------------------------------------------
## 1. Thinking like a Programmer

This lecture is about applying our problem solving strategies to the problem of
becoming a better programmer.

As stated in the course syllabus, the purpose of this course has been to teach
you how to analyze, strategize, and form a problem-solving plan; manage
complexity; improve software quality; leverage existing solutions; and select
the best tool to solve the problem at hand.

As we wrap up this semester, let's take a moment to think back upon some of the
new programming skills you have learned about:


* Design before you code
* UML diagrams
* Refactoring
* Git!  Git all of the things!
* Different programming paradigms exist (not everything looks like a Python solution)
* Break a bigger problem down into smaller tractable pieces
* Don't overdesign your solution
* File I/O - how to read (and write!) files to/from the disk




--------------------------------------------------------------------------------
## 2. Wisdom vs. Knowledge

Having learned these things has increased your *knowledge* about programming.
There are still many techniques that you'll need to learn about, but this is a
good first step.  Another important ingredient, *wisdom* comes only with
experience and time.


#### The difference between wisdom and knowledge
Knowing *when* to use a technique is just as important as knowing *how* to do it

> Knowledge is knowing that a tomato is a fruit, but wisdom is knowing to not
> put a tomato into a fruit salad.
>
> -- someone wiser than I

* What is the cost of applying a technique inappropriately?
    + It could take longer - both from a computational perspecive, and from a
      productivity perspecive
    + You can introduce bugs - subtle design errors instead of


* How will you know when you should do something in a particular way?
    + It's not going as easily as planned
    + Your problems are more "accidental" in nature than "essential"
    + You find yourself running into lots of "unintended consequences" (the bad
      kind of consequences)



We all understand how to increase our knowledge, that's as simple as opening a
book or finding a blog.  But how can you intentionally increase your wisdom?
One must have experiences to learn *when* and *why* to do things in a particular
way.  Here is one way you can find those experiences that will give you the best
return on your time investment:


#### Exploratory Learning
Explicitly allot time for learning new components as a general task.

#### As-needed Learning
Search for a component to solve a specific problem facing you now.


Much of the time you will spend engaged in learning as a professional programmer
will be in the "as-needed" category.  When your boss asks you to do something
that you've never done before, you now *need* to figure it out.

More rewarding is the learning you will do (usually on your own time) pursuing
subjects that you find most interesting.  One result of this is that you may
become *the expert* of that thing in the office, and more tasks that you are
interested in doing will begin to come your way.  Or, perhaps it won't work out
quite so well...

[The Expert](https://www.youtube.com/watch?v=BKorP55Aqvg)



--------------------------------------------------------------------------------
## 3. Catalog your strengths and weaknesses

Another way to identify areas for you to focus on is to make a list of your
strengths and weaknesses, and devise activities to turn your weaknesses into
newfound strengths.



#### What are your weaknesses?

* Convoluted designs
* Can't get started
* Don't finish anything
* Fail to test
* Overconfident
* Weak at X

Are there any others?


#### What are your strengths?

* Eye for detail
* Fast learner
* Fast coder
* Never gives up
* Super problem-solver
* Tinkerer
* Mull it over
* Curious!!!
* Able to work on many piecses at once
* Good at doing up-front research
* Find all of the ways *not* to do it

What else are you great at?

> Curiosity and an unstoppable drive to learn and improve are indispensable
> attributes of the fledgling Computer Scientist, and their cultivation is the
> focus of this course.  

     _ _                                _ _ 
    ( | ) Do only what only you can do ( | )
     V V                                V V 
          -- Edsger W. Dijkstra




--------------------------------------------------------------------------------
## 4. Suggested activities to continue your growth as a programmer

The good news is that you can minimize your weaknesses and increase your
strengths through study and practice.

If there were topics in this class or other classes which you don't feel that
you possess a mastery of, spend a little bit of time on them over the Summer so
that when you return you'll feel confident and deserving of your place in the
next challenges which will come your way, whether those are new classes or an
internship or a new career.



### Curate a portfolio of programming artifacts

Keep every bit of code you ever write.  This is easier than ever if you're
using git.

* It's nice to look back upon your old programs and to see that you've
  improved.  

* Someday you'll face a problem and say to yourself "I think I've solved this
  once before".  If you are keeping track of your code you'll be able to reach
  into an ever-growing library of past solutions and find something that may be
  adapted to your current task.

One of my greatest regrets is that I have long since lost the code to the very
first programs I ever wrote in CS1 and CS2 (no git in those days).  I do have
code from CS3 and onward, and every now and then I'll look at that code and
laugh at it.



### Explore the world of Open Source software

Most "real world" programming is not writing a new solution completely from
scratch, but rather supplementing or modifying an existing code base.

Between GitLab, Bitbucket and GitHub it is easier than ever to get involved
with an Open Source software project.  Find a project that you're curious about,
clone the code, and dive in.  You will learn just as much from *reading* code as
you do from *writing* code.


### Learn a new programming language

http://www.99-bottles-of-beer.net/

This will be beneficial to you for so many reasons:

1. When your only tool is a hammer, you'll have sore thumbs.  I first learned to
   think in C++.  It took me years to reverse the brain damage that caused.  But
   now I can think about problems in higher-level terms because I understand
   alternative ways to approach them.

2. You will gain context.  "Why does language X have this feature?"  You can
   reason about trade-offs in the design of languages because you will have more
   and varied points of comparison.  You have available more handholds by which
   you can understand new concepts.  Seeing new code (and the same code in
   different styles) is not as perplexing as it once was.

3. Each new language will teach you a bit more about logical thinking and
   computation.  The pace of learning accelerates with each new language you
   learn.

4. Like human languages, programming languages are embedded within their unique
   cultures.  My advice is to learn at least one programming language which is
   embedded in an "academic" culture (How can you tell if a language is
   academic?  Good signs are that its website doesn't look very good, and it was
   created as someone's dissertation).

I've personally learned very much from the Scheme hackers that I've hung out
with.  The level of discourse is so much higher there than in other places.
There's probably something to gain from every language culture, but make sure
that you are going to the Opera instead of a NASCAR event once in a while.

The point isn't to learn just those things that look neat on your résumé, but
to learn things that are neat to you.  Besides, the more languages you know,
the more of a language snob you get to become.

![The programmer hierarchy](hierarchy.jpg)

![The programmer hierarchy for LISP hackers](lisp_hierarchy.jpg)





### Take part in coding competitions/challenges

There are plenty of these out there; here are a few I've enjoyed:

* https://programmingpraxis.com/
* https://projecteuler.net/
* http://exercism.io/
* https://adventofcode.com/

Combine these challenges with a new language for double the benefit.  In fact,
when you pick a new language it's helpful to have some project in mind to focus
your effort on.  These coding challenges serve that need well.





### Connect with the broader community of programmers

By this I mean "connect with programmers IRL".  Get involved with other hackers
at meetings in meatspace.

There are lots of clubs and events on campus during the school year.

This coming spring (April 10th - 12th) you should definitely check out
[OpenWest](https://openwest.org/).  You can score a free ticket by submitting a
talk proposal that's accepted.

Oh, you don't think you're qualified to give a talk?  Don't let little things
like posessing qualifications hold you back from doing what you want; I don't.  




--------------------------------------------------------------------------------
## Things Which Have Made Me a Better Programmer

### Learning the History of the Field

Learning about the challenges of the past gives us the context to understand
the status quo, and informs our efforts to improve it. In general, things aren't
the way they are because the people who came before were idiots, and you
probably aren't the first person to have that cool idea.

Studying the earliest calculation devices from the days of Charles Babbage
through the Manchester "Baby" and the ENIAC not only gives one a better
appreciation for modern technology, but encourages us to better use it. We often
think that through the magic of Moore's law that we have moved past the concerns
and challenges of the first generation of computers. But we'd do well to
remember their struggles because:

1. Our predecessors had to do really clever things out of necessity. We don't
   work under the same privations as they did, and so we don't think very much
   or very hard about what we're doing. We justify this to ourselves because
   we're not working with crappy plugboards or punch cards.

   It is true that we shouldn't have to think very hard about clever
   algorithms. The reason is not because our hardware is better, but because
   those guys and gals were good enough to write papers and books about it.

   There is a point where over-thinking the situation becomes a bad thing.
   I argue that we are usually very far away from that place.

2. Moore's law is not a natural law that governs or guarantees future
   performance. It just an observation that happens to explain how things have
   worked so far. We've already had to employ cleverness to work around the
   limitations we've already run into. Relying on it to mitigate out problems
   doesn't work now, and becomes less viable as time goes on.

   Also, Gordon Moore himself notes that:
     _ _                                               _ _ 
    ( | ) Moore's law is a violation of Murphy's law. ( | )
     V V  Everything gets better and better.           V V 

                        -- "Moore's Law at 40 - Happy birthday".
                The Economist. 2005-03-23. Retrieved 2006-06-24.

Computer Science is a young field. There is no excuse for being ignorant of its
beginnings while there are still people living who were born before it began.


### Understand and Appreciate the Fundamentals of Computation

When I was younger, I thought that computers were magical things, and I didn't
want the magic to end by uncovering the wizard behind the curtain. Now I am
ashamed of myself that I ever felt that way toward gaining knowledge.  The more
I know about how these things work, my youthful awe is replaced by a sense of
disbelief that everything works as well as it does. Computers hold very nearly
the same sense of magical wonderment as before, it is just tempered by cynicism
now (or, that's just a result of being an old grump). I am still in awe, but I
can do something about it.

Writing a compiler made me a better user of compilers and languages. Learning
assembly language enables me to debug and fix problems that have puzzled people
for years. Learning Artificial Intelligence lets me understand how seemingly
"magical" things can be possible through the application of a lot of data to
statistical analysis.

You will write better code faster because you aren't fighting with your own
faulty assumptions. Nor will you waste time trying to get the computer to do
something that it just can't do.

Many say that they do not wish to be bogged down by lots of fiddly details.
Neither do I, but for me it is a conscious choice that I can make, not a
limitation imposed upon me by the circumstance of my ignorance.


Lecture 9: Dec_07/notes.md
================================================================

# CS1440 - Fri Dec 07

# Announcements

## Participation Points Policy

If you want to earn more points in the participation category, you have until
the due date of the final assignment, Dec 8 at midnight to add to the
discussion on Canvas.  After the final assignment is due there is nothing more
you can do to contribute to an environment of supportive learning in the class.

The points you earn here are determined by the *quality* of your participation,
not the quantity.  Spammers need not apply.


# Final Exam Review

### Git 
* It is *not* Erik's advice to save up all of your changes in order to make one
  large git commit at the end of the workday
* It is *not* Erik's advice to keep all of your code for all of your different
  projects in the same git repository
* Which git feature lets you freely and safely experiment and try out new
  possibilities in code without jeopardizing already working code?
* Which git command helps you quickly identify which developer is responsible
  for a questionable line of code?
* Which git command embodies the strategy of "Wolf-Fence Debugging" by zeroing
  in on a commit which introduced a bug?
* Which git command lists the branches in your repository?
* Which git command should you use when you don't remember which git command to use?



### Problem-Solving
* Knowing when to use a technique - or when not to use it - is as important as knowing
* What is "Exploratory Learning", and how does it differ from "As-Needed Learning"
* In the "real world" do you spend more time writing new code or maintaining existing code?
* Why are global variables discouraged?
* Essential vs. Accidental difficulties

#### General Problem-Solving Techniques
+ Always Have a Plan
+ Divide the Problem
+ Start with What You Know
+ Restate the Problem
+ Reduce the Problem
+ Look for Analogies
+ Experiment
+ Don't get Frustrated



### Software testing and verification
* What is software testing?
* Software failures vs. software errors
* What is a unit test?
* What is a regression test?
* What is an integration test?
* Verification vs. validation
* Remember, a sufficiently thorough testing method will *never* uncover all
  possible types of errors in all programs!



### UML
* The purpose of a UML diagram is to describe what your design is rather than how it shall work
* UML is a general-purpose, developmental, modeling language in the field of Software Engineering
* If it's hard to capture in a UML class diagram, it's likely an "Accidental" quality of your system
* What does a class look like in a UML class diagram?
* Associations vs. Dependencies - appearance and meaning
* What is a "multiplicity constraint"?



### Refactoring
* What is refactoring?
* Why do we refactor code?
* How can git support your refactoring efforts?
* How can a unit test support your refactoring efforts?



### Design Patterns and Code Reuse
_Note: I may replace this question about "good" vs. "bad" code reuse on the exam if we can't find the lecture notes where this is presented.  I'll leave this on the review for your own information_

_Update to previous note: I found what I was looking for in the lecture notes from Nov 14th, under the heading **Code Reuse**_
[Code Reuse](https://bitbucket.org/erikfalor/fa18-cs1440-lecturenotes/src/master/Nov_14/notes.md#markdown-header-code-reuse)

* How will I know when to use which types of reuse?  Or, what is "Good Reuse"
  and what is "Bad Reuse"?
  
### Table from _Think Like a Programmer_ by V. Anton Spraul:

| Good Reuse                                    | Bad Reuse                                                              |
|-----------------------------------------------|------------------------------------------------------------------------|
|Promotes understanding                         | Enables risky behaviors                                                |
|Following a blueprint                          | Copying someone else’s work                                            |
|Magnifies and extends your capabilities        | Falsifies your capabilities                                            |
|Helps you learn                                | Helps you avoid learning                                               |
|Saves time in the short term and the long term | May save time in the short term but may lengthen time in the long term |
|Results in a working program                   | May result in a program that doesn’t work anyway                       |


Blindly copying code from Stack Overflow is an example of a risky behavior -
how do you know that code wasn't planted there by a Russian agent?  This
research paper demonstrates that well-intentioned Stack Overflow answers can
introduce security issues into your code:

[Secure Coding Practices in Java: Challenges and Vulnerabilities](https://arxiv.org/pdf/1709.09970.pdf)

* What is a "code smell"?
    + Anything in the code which seems "off", and indicates that a bigger
      problem is lurking in the code
* What is a Design Pattern?
* What benefit does the Abstract Factory Pattern give?
* What does it mean for classes to be Polymorphic?
* What is Duck Typing?
* What is an Abstract Class?
* What does it mean to "override a method"?
* What is the Law of Demeter for Functions?



### Recursion
* Which of our general problem-solving principles does a recursive solution best embody?
* What is head recursion?
* What is tail recursion?
* What is "Tail Call Optimization"?
* What steps are involved in designing a recursive solution?
* Why do complex data structures benefit from being processed recursively?
* What is V. Anton Spraul's "Big Recursive Idea"?
* Must a problem possess the essential quality of recursion for a recursive
  solution to be applied?

* Common beginner mistakes with recursion are
1. too many parameters
2. relying on globals

* What happens if you never reach the base case?
* Recursion can be imitated with an iterative algorithm using an explicitly managed stack
* What is a wrapper function?
