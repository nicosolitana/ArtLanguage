grammar ArtGrammar;

expr : (func)* EOF ;

func : DEF IDENTIFIER PAREN_START PAREN_END CURLY_START (code)* CURLY_END
     | DEF IDENTIFIER PAREN_START func_params PAREN_END CURLY_START (code)* CURLY_END;
     
func_params : IDENTIFIER 
            | IDENTIFIER SEPARATOR func_params ;

code : init | math_expr | size_shape; 

init : data_type IDENTIFIER ;

math_expr : IDENTIFIER ASSIGN_OP computation;
computation : value_type MATH_OP value_type;

//draw : IDENTIFIER DOT_NOTATION DRAW PAREN_START draw_dimensions PAREN_END;
size_shape : IDENTIFIER DOT_NOTATION SIZE PAREN_START params PAREN_END ;
params : two_params
       | two_params SEPARATOR value_type
       | two_params SEPARATOR two_params ;

two_params : value_type SEPARATOR value_type;

value_type : IDENTIFIER | INTEGER ;


data_type : CIRCLE
          | RECTANGLE
          | SQUARE
          | CIRCLE
          | DOT
          | STRAIGHT
          | ARC
          | PIXEL
          ;

RECTANGLE       :   ('Rectangle');
SQUARE	        :   ('Square ');
CIRCLE	        :   ('Circle ');
DOT	            :   ('Dot ');
STRAIGHT	    :   ('Straight');
ARC	            :   ('Arc');
PIXEL	        :   ('Pixel');
OUTLINE	        :   ('outline');
DRAW	        :   ('draw');
SIZE	        :   ('size');
FOR	            :   ('for');
DEF	            :   ('def');
FILL	        :   ('fill');
CANVAS	        :   ('canvas');
INTEGER	        :   [0-9]+;
IDENTIFIER      :	[a-zA-Z][a-zA-Z0-9]* ;
MATH_OP         :   ('++'|'--'|'-'|'+'|'*'|'\\');
COND_OP    	    :   ('<='|'<'|'>'|'>=');
PAREN_START     :   '(';
PAREN_END       :   ')';
CURLY_START     :   '{';
CURLY_END       :   '}';
DOT_NOTATION    :   '.';
ASSIGN_OP       :   '=';
SEPARATOR	    :   (','|';');
WS              :   [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines