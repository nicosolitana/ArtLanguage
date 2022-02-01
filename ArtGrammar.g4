grammar ArtGrammar;

expr           : (consts)* (glob)* (func)* EOF ;

func           : DEF IDENTIFIER PAREN_START PAREN_END CURLY_START (code)* CURLY_END
               | DEF IDENTIFIER PAREN_START func_params PAREN_END CURLY_START (code)* CURLY_END;

consts         : CONSTANT init_int;   

glob           : GLOBAL data_type init_int; 

func_params    : IDENTIFIER 
               | IDENTIFIER SEPARATOR func_params ;

code           : init 
               | init_int
               | math_expr 
               | size_shape 
               | draw_shape
               | canvas_def
               | fill_def
               | outline_def
               | func_call 
               | if_else
               | loop; 

loop           : FOR PAREN_START loop_init loop_cond loop_incdec PAREN_END loop_body; // loop_init loop_cond loop_incdec
loop_body      : CURLY_START (code)* CURLY_END;
loop_init      : init_int SEMICOL_SEP // cannot detect init
               | math_expr SEMICOL_SEP;
loop_cond      : condition_body SEMICOL_SEP;
loop_incdec    : INTEGER INCDEC_OP;

init           : data_type IDENTIFIER ;

init_int       : IDENTIFIER ASSIGN_OP INTEGER;

func_call      : IDENTIFIER PAREN_START PAREN_END 
               | IDENTIFIER PAREN_START call_params PAREN_END;

call_params    : value_type (SEPARATOR value_type)*;

if_else        : if_cond 
               | if_cond elif_cond else_cond 
               | if_cond else_cond;

if_cond        : IF condition ifel_body;
elif_cond      : (ELIF condition ifel_body)+;
else_cond      : ELSE ifel_body;
condition_base : PAREN_START condition_body PAREN_END;
condition_body : value_type COND_OP value_type;
condition      : condition_base 
               | PAREN_START (condition_base LOGICAL_OP)* condition_base PAREN_END; 
ifel_body      : CURLY_START (code)* CURLY_END;

math_expr      : IDENTIFIER ASSIGN_OP computation;
computation    : value_type MATH_OP value_type;

canvas_def     : CANVAS PAREN_START two_params PAREN_END;

outline_def    : IDENTIFIER DOT_NOTATION OUTLINE PAREN_START outline_params PAREN_END;
outline_params : value_type SEPARATOR rgb_def SEPARATOR value_type;
rgb_def        : RGB PAREN_START two_params SEPARATOR value_type PAREN_END ;

fill_def       : IDENTIFIER DOT_NOTATION FILL PAREN_START fill_params PAREN_END;
fill_params    : rgb_def SEPARATOR value_type ;

draw_shape     : IDENTIFIER DOT_NOTATION DRAW PAREN_START draw_params PAREN_END ;
draw_params    : two_params SEPARATOR two_params 
               | two_params SEPARATOR two_params SEPARATOR two_params;

size_shape     : IDENTIFIER DOT_NOTATION SIZE PAREN_START size_params PAREN_END ;
size_params    : two_params
               | two_params SEPARATOR value_type
               | two_params SEPARATOR two_params ;

two_params     : value_type SEPARATOR value_type;

value_type     : IDENTIFIER | INTEGER ;


data_type      : CIRCLE
               | RECTANGLE
               | SQUARE
               | CIRCLE
               | DOT
               | STRAIGHT
               | ARC
               | PIXEL
               ;

RECTANGLE      :   ('Rectangle');
SQUARE	       :   ('Square');
CIRCLE	       :   ('Circle');
DOT	           :   ('Dot');
STRAIGHT	   :   ('Straight');
ARC	           :   ('Arc');
PIXEL	       :   ('Pixel');
IF	           :   ('if');
ELSE	       :   ('else');
ELIF	       :   ('elif');
OUTLINE	       :   ('outline');
DRAW	       :   ('draw');
SIZE	       :   ('size');
FOR	           :   ('for');
DEF	           :   ('def');
FILL	       :   ('fill');
CANVAS	       :   ('canvas');
RGB 	       :   ('rgb');
CONSTANT 	   :   ('const');
GLOBAL   	   :   ('global');
BREAK   	   :   ('break');
CONTINUE   	   :   ('continue');
INTEGER	       :   [0-9]+;
IDENTIFIER     :	[a-zA-Z][a-zA-Z0-9]* ;
MATH_OP        :   ('-'|'+'|'*'|'\\');
INCDEC_OP      :   ('++'|'--');
COND_OP    	   :   ('<='|'<'|'>'|'>=');
LOGICAL_OP     :   ('&&'|'||');
PAREN_START    :   '(';
PAREN_END      :   ')';
CURLY_START    :   '{';
CURLY_END      :   '}';
DOT_NOTATION   :   '.';
ASSIGN_OP      :   '=';
SEPARATOR	   :   (',');
SEMICOL_SEP    :   (';');
WS             :   [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines