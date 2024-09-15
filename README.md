# PDF Extractor :pencil2::bookmark_tabs:

This is my attempt at a python scipt that accepts user inputted boards as text files, solves them, and outputs to the console.

## Description

This program, though uncomplete currently works as follows: I have created sudoku text files, there are simply 9 character wide and 9 line tall files representing sudoku boards.  This script has custom objects for each tile that contain a value as well as a list of possible values.  It then parses through the board looking or spaces that have only 1 possible option, or spaces where in its row, column, and 
ninth it can only be 1 number.  It is incomplete currently as it cannot solve every board, as some reach states where there is no certain next move based on the descriptors I have created.

## Possible future improvements.

I would like to incorporate depth-first search as I think that may be able to make it solveable for any board, by essentially brute forcing it.

## Executing program

* The board to solve is currently located on line 21, but will eventually be turned into an argument in the command.
```
python3 sudokusolverattempt2.py
```

## Authors

:key: ListenToAJ


## Version History

* 0.1
    * Initial version which only would look for spots where a space can only be 1 number.
* 0.2
* Second version which also checks possible options for row, col, and ninth and marks when there is only 1 space that can be a specific num

## License

This isn't liscened, come on man it's like 14 lines of code.

## Acknowledgments

* [README-Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [GeeksforGeeks](https://www.geeksforgeeks.org/working-with-pdf-files-in-python/)