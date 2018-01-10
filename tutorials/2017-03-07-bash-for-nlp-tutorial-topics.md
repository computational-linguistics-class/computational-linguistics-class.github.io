---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: John's Bash for NLP tutorial, advanced topics
active_tab: resources
release_date: 2018-01-10
---

Advanced bash for NLP tutorial
===============================

Bash can be used to do complex things faster than you could whip up a Python script to do the same things.
However, because of tricky syntax and not altogether intuitive semantics, it tends to push people away when it tries to show love.
In other words, *it's frequently misunderstood.* 
As computer scientists, we surely can empathize with bash, and give it a another chance.

This tutorial is composed of topical case studies resolving around either solving a specific problem or becoming proficient with a specific tool. 
It assumes you've read through the basic tutorial hosted on this site, and beyond that, have had some time twiddling around on the command line to get a feel for the ropes.


## Disclaimer: *bash operates on strings*
I can't stress this enough. File paths are strings. output is strings. 
Command names are strings. 
There are no types; there is nothing but string.

### Process Substitution
*Credit for this, my favorite bash tidbit, must be shared with Jonathan May.*

Many tools used in bash scripts take a variable number of arguments, each of which must be the location of a file. 
For example, I use `paste` to take a side-by-side look at two similar files:

        paste model_output.ug gold_standard.ug

However, frequently the data we're trying to analyze may be the output of processes. 
In this case, we have to redirect `stdout` to a file for each process, and then paste together the results:

       tr ' ' '\n' < model_output.ug | sort | uniq -c | sort -n > model_types.freq
       tr ' ' '\n' < gold_standard.ug | sort | uniq -c | sort -n > gold_types.freq
       paste model_types.freq gold_types.freq

These commands count the frequency of space-separated words in a file, sort them, output them to a file, and then pastes them side-by-side for human analysis.

Sometimes we want these temporary files (e.g. `model_types.freq`, `gold_types.freq`); other times we do not.

**Process Substitution** allows us to treat the output of each command as a file object without actually writing anything to disk. This has obvious I/O benefits, as well as potentially eliminating unwanted temporary files, and allowing for quicker re-execution of similar code. The syntax is as follows:

        command_that_takes_files.sh file1.txt <(foo.sh arg1 arg2 ) file3.txt

Here, the stdout of `foo.sh` is treated as if we had printed it to a file, and then included that file in the command. 
Now, let's re-write the type-frequency command sequence:

        paste <(tr ' ' '\n' < model_output.ug | sort | uniq -c | sort -n) \
              <(tr ' ' '\n' < gold_standard.ug | sort | uniq -c | sort -n)

*More later on how to chain together process substitution commands to make some unnecessarily complex, beautiful bash commands.*

### `for` loops

`for` loops in bash iterate over various types of strings. The easiest and most common use is to iterate over the contents of a directory.

#### Iterating over the contents of a directory

To iterate over the contents of the directory at the current directory , use the following;

        for i in $( ls . ); do
          echo $i
        done

Let's go through a few subtle aspects of this. 
 - First, note that in each iteration of the loop, the variable `i` is assigned the value of some file in the directory at ``. To access the value of the variable `i` and not the *string* `i`, we use the dollar sign, thus `$i`. 
 - Second, note the `$()` structure. This (I think?) runs the `ls` command. You can omit the first space, as in `$(ls path )`, but **not** the second space. In other words, `$( ls path)$ is invalid, since you're looking for the path `path)`. 
 - Third, note that the `for` is matched with a corresponding `do` and a final `done`. 
 - Fourth, the semicolon is necessary. However, the command could be inline'd as in 

        for i in $( ls path ); do echo $i; done
 
 The semicolon after $i is necessary because the command `echo $i` must be terminated before the loop is terminated.
 - Fifth, let's say I'm iterating over the contents of some absolute path:

        for i in $( ls /nlp/users/johnhew/goldstandarddata ); do echo $i; done
 
 This will fail! Why? Because the variable `i` just stores the path relative to `/nlp/users/johnhew/goldstandarddata`. Instead, I should run 

        goldpath=/nlp/users/johnhew/goldstandarddata
        for i in $( ls $goldpath ); do echo $goldpath/$i; done

 Note that the value $goldpath/$i merely concatenates the two parts of the filepath together with a `/` in the middle, since *bash only works with strings.* This accesses the files where they actually are, not pretending they're in the current working directory. 

#### Iterating over a sequence or otherwise

What if you want to iterate over something like a sequence of numbers, or a pre-specified set of values?
It's not going to be a problem.

To iterate over a squence of integers, first test the `seq` command as follows:

        seq start_integer end_integer
        seq 1 10

Now recall that bash works on strings, and will be willing to iterate over the string that `seq` produces as follows:

        for i in `seq 1 10`; do echo $i; done

We're introduced to new syntax, the backtick (\`\`) notation. This means "execute the command within these bakticks and consider its output as part of the string that bash operates on". It gets pretty meta.
So, what would have happened had we omitted the backticks? the command 

        for i in seq 1 10; do echo $i; done

Prints out

        seq
        1
        10

Which is hilarious, I think, but also the solution to our other question "how do I iterate over a sequence of pre-specified values". 

#### Tips on `for` iteration
 - You'll frequently want to *just* iterate over files, or over directories, or over just all `.tsv` files. Modify the `ls` command to do this for you, as in the last two cases:

          for i in $( ls -d */ ); do echo "$i is a directory"; done
          for i in $( ls *.tsv ); do echo "$i is a .tsv"; done

 - You can nest these loops, and life really gets fun then. For example, I use indirected directories when I'm storing over 1 million files. Thus, you could do something that looks like

          for i in $( ls $root ); do
            for j in $( ls $root/$i ); do
              for k in $( ls $root/$i/$j ); do
                cat $root/$i/$j/$k;
              done
            done
          done


### branching; `if` conditionals
Conditionals are very easy if you'd like to check something related to a file system. 
To check for the existence of a file, the syntax is the following:

        if [ -f path_to_file ]; then echo "woo!"; fi

I usually use ifs in the middle of iterating over a directory, for example if you're looping
through directories and you want to check some kind of output if and only if the output file
exists for that directory. (You know, because each directory has 1 experiment, and not all of
the experiments have finished, but you're really impatient.)

        for dirpath in $( ls path_to_dirs ); do if [ -f $dirpath/results.txt ]; then cat $dirpath/results.txt; fi; done

Note that you have to close the `if`s and `for`s properly, or bash gives you some well-meaning
but useless syntax error.

### `while` loops

### Path and file manipulation : `sed`, advanced `grep`

### File manipulation: `cut`, `paste`, `column`

### File mainpulation: `sort`, `uniq`

### Arithmetic: the dark arts

### Case study on `xargs` : when you have too many files.

### Case study on efficiency in filesystems

### Symbolic links
Symoblic links are great when you want to deal with nice pretty filepaths, but your data is in
a shared location / on some mega disk somewhere else.
They make it seem like there's a path, right in your cozy directory of choice, to some
aribtary other path.
The general syntax is: 

        ln -s ugly_target_filepath_to_type_once nice_filepath

Note that, to be very clear, `ugly_target_filepath_to_type_once` _already exists_,
and you're creating a ``file" at `nice_filepath` that will act like the ugly path.

Some caveats: symbolic links aren't quite the same as having the directory right there.
Sometimes the behavior is the same. If you try the following:

        ls nice_filepath
        ls ugly_target_filepath_to_type_once

you get the same thing!
However, if you try the following, attempting to calculate the total number of bytes
stored under each filepath,

        du -sh nice_filepath
        du -sh ugly_target_filepath_to_type_once

the ugly filepath will give you the correct answer, but the nice filepath will give
you 0.
Instead, you should run

        du -sh nice_filepath/

(yes, the trailing forward slash makes all the difference) in order to get the correct
answer.
Intuitively, this trailing slash forces bash to treat the symbolic link as its directory,
not as the vacuous file that it actually is in your directory.


![CC-Attribution-ShareAlike 4.0](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)
