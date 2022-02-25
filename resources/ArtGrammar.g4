grammar ArtGrammar;

expr           : (consts)* (glob)* (func)* EOF ;

func           : DEF IDENTIFIER PAREN_START PAREN_END CURLY_START (code)* CURLY_END
               | DEF IDENTIFIER PAREN_START func_params PAREN_END CURLY_START (code)* CURLY_END;

consts         : CONSTANT PIXEL init_int;   

glob           : GLOBAL PIXEL init_int; 

func_params    : IDENTIFIER 
               | IDENTIFIER SEPARATOR func_params ;

code           : dec
               | init 
               | init_int
               | init_bool
               | init_str
               | lst_access
               | lst_add_val
               | concat
               | conv_tostr
               | print_text
               | init_lst
               | math_expr 
               | size_shape 
               | draw_shape
               | canvas_def
               | fill_def
               | outline_def
               | func_call 
               | if_else
               | loop; 

dec            : data_type (init_int|init_bool|init_str|init_lst);

loop           : FOR PAREN_START loop_init loop_cond loop_incdec PAREN_END loop_body; // loop_init loop_cond loop_incdec
loop_body      : CURLY_START (code)* CURLY_END;
loop_init      : init_int SEMICOL_SEP // cannot detect init
               | math_expr SEMICOL_SEP;
loop_cond      : condition_body SEMICOL_SEP;
loop_incdec    : INTEGER INCDEC_OP;

init           : data_type IDENTIFIER ;

init_int       : IDENTIFIER ASSIGN_OP (INTEGER|IDENTIFIER);

init_bool      : IDENTIFIER ASSIGN_OP ((TRUE|FALSE)|IDENTIFIER); 

init_str       : IDENTIFIER ASSIGN_OP STR_LITERAL;

init_lst       : IDENTIFIER ASSIGN_OP lst_def;

lst_def        : SQR_START SQR_END
               | SQR_START lst_val SQR_END  ;

lst_val        : (INTEGER SEPARATOR)* INTEGER
               ; 

lst_access     : (PIXEL)* IDENTIFIER ASSIGN_OP IDENTIFIER SQR_START (INTEGER|IDENTIFIER) SQR_END
               ;

lst_add_val    : IDENTIFIER DOT_NOTATION LST_ADD PAREN_START (INTEGER|IDENTIFIER) PAREN_END
               ;  

conv_tostr     : (STRING)* IDENTIFIER ASSIGN_OP TOSTR PAREN_START (IDENTIFIER|INTEGER) PAREN_END
               ;

func_call      : IDENTIFIER PAREN_START PAREN_END 
               | IDENTIFIER PAREN_START call_params PAREN_END;

call_params    : value_type (SEPARATOR value_type)*;

print_text     : PRINT PAREN_START (IDENTIFIER|STR_LITERAL) PAREN_END;

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

math_expr      : IDENTIFIER ASSIGN_OP computation       //(IDENTIFIER ASSIGN_OP computation) 
               | IDENTIFIER INCDEC_OP;
               
//computation    : value_type math_op value_type;

computation    : compute
               | mcomputes
               | gcompute
               | cgcompute
               | ugcompute
               ;

cgcompute      : PAREN_START ((gcompute|value_type) math_op)+ (gcompute|value_type) PAREN_END;
gcompute       : PAREN_START compute PAREN_END;
ugcompute      : (value_type math_op)+ mcomputes
               | (mcomputes) (math_op value_type)+
               | (mcomputes)+ math_op value_type math_op (mcomputes)+
               | (mcomputes)+ math_op (mcomputes)+ math_op (mcomputes)+
               ;

mcomputes      : gcompute
               | cgcompute
               | compute
               ;

compute        : value_type math_op value_type
               ;

math_op        : ADD
               | SUB
               | MUL
               | DIV
               ;

concat         : (STRING)* IDENTIFIER ASSIGN_OP (IDENTIFIER|STR_LITERAL) AMPSAND (IDENTIFIER|STR_LITERAL)
               ;

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

value_type     : IDENTIFIER | INTEGER | TRUE | FALSE;


data_type      : CIRCLE
               | RECTANGLE
               | SQUARE
               | CIRCLE
               | DOT
               | STRAIGHT
               | ARC
               | PIXEL
               | BOOL
               | STRING
               | LIST
               ;


TOSTR          :   ('tostr');
PRINT          :   ('print');
LST_ADD	       :   ('add');
TRUE	         :   ('true');
FALSE	         :   ('false');
BOOL	         :   ('Bool');
RECTANGLE      :   ('Rectangle');
SQUARE	       :   ('Square');
CIRCLE	       :   ('Circle');
DOT	           :   ('Dot');
STRAIGHT	     :   ('Straight');
ARC	           :   ('Arc');
PIXEL	         :   ('Pixel');
IF	           :   ('if');
ELSE	         :   ('else');
ELIF	         :   ('elif');
OUTLINE	       :   ('outline');
DRAW	         :   ('draw');
SIZE	         :   ('size');
FOR	           :   ('for');
DEF	           :   ('def');
FILL	         :   ('fill');
CANVAS	       :   ('canvas');
RGB 	         :   ('rgb');
CONSTANT 	     :   ('const');
GLOBAL   	     :   ('global');
BREAK   	     :   ('break');
CONTINUE   	   :   ('continue');
LIST           :   ('List');
STRING         :   ('String');
SQR_START      :  '[';
SQR_END        :  ']';
STR_LITERAL    :   '"' ( '""' | ~["\r\n] )* '"';
INTEGER	       :   [0-9]+;
IDENTIFIER     :   [a-zA-Z][a-zA-Z0-9]* ;
ADD            :   ('+');
SUB            :   ('-');
MUL            :   ('*');
DIV            :   ('/');
INCDEC_OP      :   ('++'|'--');
COND_OP    	   :   ('<='|'<'|'>'|'>='|'!='|'==');
LOGICAL_OP     :   ('&&'|'||');
PAREN_START    :   '(';
PAREN_END      :   ')';
CURLY_START    :   '{';
CURLY_END      :   '}';
DOT_NOTATION   :   '.';
ASSIGN_OP      :   '=';
AMPSAND        :   '&';
SEPARATOR	   :   (',');
SEMICOL_SEP    :   (';');
WS             :   [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines 