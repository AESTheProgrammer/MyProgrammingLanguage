grammar Expr;

prog: func+ EOF                     # Program
    ;

func: 'def' ID '(' params ')' blok  # FunctionDecl
    ;

blok: '{' (decl | expr | stmt)+ '}' # Block
    ;

stmt: 'if' '(' expr ')' blok        # IfStmt
    | ID '=' expr                   # Assignment
    ;

params: (INT_TYPE ID ',')*          # Parameters
    ;

decl: ID ':' INT_TYPE '=' NUM       # Declaration
    ;

expr: '(' expr ')'                  # ParenthesizedExpr
    | expr ('*'|'/') expr           # MulOrDiv
    | expr ('+'|'-') expr           # SubOrAdd
    | expr ('<') expr               # LessThan
    | ID '(' (expr ',')* ')'        # FunctionCall
    | ID                            # Variable
    | NUM                           # Number
    ;

ID: [a-z][a-zA-Z0-9_]*;
NUM: '0' | '-'?[1-9][0-9]*;
INT_TYPE: 'INT';
//FLOAT_TYPE: 'FLOAT';
COMMENT: '--' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;