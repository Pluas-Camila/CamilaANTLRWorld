//Created a g4 file which specifically
//identifies files that are ANTLR grammar files.

grammar Grammar;

start: (expr)* EOF;

// Expression rules
expr: expr ('*'|'/') expr     # MulDivExpr
    | expr ('+'|'-') expr     # AddSubExpr
    | INT                     # IntExpr
    | '(' expr ')'            # ParenExpr
    ;

// Lexer rules
NEWLINE : [\r\n]+ ;           // Match newlines
INT     : [0-9]+ ;            // Match integers
WS      : [ \t]+ -> skip ;    // Ignore whitespace