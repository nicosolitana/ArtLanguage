# ArtLanguage
Project Repository for Theory of Programming Language class

The following describes the ART Programming language.

1. Shapes
  Defines which shape a particular Identifier is.
  Format: SHAPE_TYPE IDENTIFIER
  Supported Types: Rectangle, Circle, Square, Dot
  Example Declaration: 
    Rectangle rect
    Circle circ
    Square sqr
    Dot dt

2. Size
  Draws the supported shapes on 1
  Format:
    - Rectangle: IDENTIFIER DOT SIZE PARENTHESIS_START X, Y, WIDTH, HEIGHT PARENTHESIS_END
    - Circle: IDENTIFIER DOT SIZE PARENTHESIS_START X, Y, RADIUS PARENTHESIS_END
    - Square: IDENTIFIER DOT SIZE PARENTHESIS_START X, Y, SIDE PARENTHESIS_END
    - Dot: IDENTIFIER DOT SIZE PARENTHESIS_START X, Y PARENTHESIS_END
  Example:
    - Rectangle: rect.size(0,0,500,200)
    - Circle: circ.size(250,250, 100)
    - Square: rect.size(0,0,500)

3. Lines
  Defines suppoted lines of the languages.
  Format: LINE_TYPE IDENTIFIER
  Supported Type: Straight
  Example Declaration:
    Straight ln

4. DRAW
  Draws the supported lines on 3
  Format:
   - Straight: IDENTIFIER DOT SIZE PARENTHESIS_START X1, Y1, X2, Y2 PARENTHESIS_END
  Example:
   - ln.draw(0,0, 250, 250)

5. Colors
  Defines the color to be specified on the fill and outlines of shapes and lines
  Format: 
    - Fill: IDENTIFIER DOT FILL PARENTHESIS_START COLOR, OPACITY PARENTHESIS_END
    - Outline: IDENTIFIER DOT FILL PARENTHESIS_START THICKNESS, COLOR, OPACITY PARENTHESIS_END
      where: COLOR is RGB PARENTHESIS_START RED, GREEN, BLUE PARENTHESIS_END

6. Code Structure (in terms of precedence)
   CONSTART_VARIABLES
   GLOBAL VARIABLES
   FUNCTIONS
      CODES
      LOOPS
      CONDITIONS
   MAIN

7. Other Data Types
   Defines other supported data types:
   Format: 
    - Pixel: PIXEL IDENTIFIER (acts as the integer as the drawing is performed by pixel)
    - Bool: BOOL IDENTIFIER
   Examples:
    - Pixel: Pixel px
    - Bool: Bool bl

8. Constants
   Defines values that are the same throughout the execution of the program.
   Note: This is strictly pixel/int value only.
   Format: CONSTANT PIXEL 
   Example:
     const PIXEL px = 5
     
8. Global
   Defines values that are on global scope.
   Note: This is strictly pixel/int value only.
   Format: GLOBAL PIXEL 
   Example:
     global PIXEL px = 5

9. Function
   Subroutines used to group codes that are frequently used in different parts of the code.
   Note: Parameters are strictly pixel/int only.
   Format: 
        DEF FUNCTION_NAME PARENTHESIS_START PARAMS* PARENTHESIS_END 
        CURLY_BRACE_START
            (CODE|LOOPS|CONDITIONS)
        CURLY_BRACE_END
   Example:
        def CreateCircle(x, y, radius)
        {
            ...
        }

10. Codes
    This can be any code specified above such as declaration, function calls etc.

11. Loops
    Specifies iteration and groups process/codes that are repetitively executed.
    Format: 
        FOR PARENTHESIS_START INIT ; STOP_CONDITION ; INCREMENT_DECREMENT ; PARENTHESIS_END
        CURLY_BRACE_START
            (CODE|LOOPS|CONDITIONS)
        CURLY_BRACE_END

        INIT : IDENTIFIER ASSIGNMENT_OPERATOR INTEGER
        STOP_CONDITION : IDENTIFIER|VALUE CONDITIONAL_OPERATOR IDENTIFIER|VALUE
        INCREMENT_DECREMENT : INTEGER(++|--)
    Example:
        for(i=0; i <5; 1++)
        {
            ...
        }

        1++ means i is incremented once.
        1-- means i is decremented once

12. Conditions
    Specifies conditional operations. Groups codes/processes that are executed only if they satisfy the condition.
    Supported relational operations: ||, &&
    Supported conditional operations: ==, !=, <, >, >=, <=
    Format:
        IF PARENTHESIS_START CONDITION PARENTHESIS_END 
        CURLY_BRACE_START
            (CODES|LOOPS|CONDITIONS)*
        CURLY_BRACE_END
        ELIF PARENTHESIS_START CONDITION PARENTHESIS_END 
        CURLY_BRACE_START
            (CODES|LOOPS|CONDITIONS)*
        CURLY_BRACE_END
        ELSE
        CURLY_BRACE_START
            (CODES|LOOPS|CONDITIONS)*
        CURLY_BRACE_END
    Example:
        if(a > 5){
            ...
        }
        elif(a != 3) {

        } 
        else {

        }

10. Main
    This is the core of the application. All created functions must be called through the main function as it is the starting point of execution of the program.
    Format: 
        DEF MAIN PARENTHESIS_START PARENTHESIS_END
        CURLY_BRACE_START
            (CODES|LOOPS|CONDITIONS)*
        CURLY_BRACE_END
    Example:
        def main(){
            ...
        }

11. Canvas
    Specifies the size of the canvas where the elements will be drawn.
    Format: CANVAS PARENTHESIS_START WIDTH, HEIGHT PARENTHESIS_END
    Example:
        canvas(500,500)

ON TESTING
Instructions on testing the project:
1. Source codes are available on [sample-codes] folder
   - bird.art : draws a bird on a branch
   - fibonacci.art : draws squares with varying sized based on fibonacci sequence
   - fractal.art : draws the Sierpiński triangle
   - southpart.art : draws a southpark character
   - sample_code_w_bugs.art : to demonstrate bug detection of the tokenizer, parser and interpreter

2. Copy any source codes on [1] to sample.art file
3. Execute the code using the ArtLanguage.ipynb

PRE-REQUISITES:
1. Python must be installed on the machine.
2. Install the following dependency.
   pip install pyglet

DEVELOPERS OF THE PROJECT:
- Eugenio, Patricia Anne
- Hermida, Hernand
- Leyesa, Jose Miguel
- Liwag, Mark Christian
- Solitana, Nico