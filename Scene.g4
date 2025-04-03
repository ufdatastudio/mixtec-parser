grammar Scene;

s       : (sent END)+ ;
sent    : clause
        | OBJ (date clause | clause)
        | date (OBJ clause | clause)
        ;

clause  : clause_f+ (date_tail | obj_tail)? ;

date_tail : date (OBJ clause_f+ | clause_f+)? ;
obj_tail  : OBJ (date clause_f+ | clause_f+)? ;

date    : Y ND? ;
clause_f: H (ND | near_date)? ;
near_date : NEAR_OBJ ND? ;

// Lexer rules: match full XML blocks as single tokens
H        : '<Human>' .*? '</Human>' ;
Y        : '<Year>' .*? '</Year>' ;
ND       : '<NameDate>' .*? '</NameDate>' ;
OBJ      : '<Obj>' .*? '</Obj>' ;
NEAR_OBJ : '<NearObj>' .*? '</NearObj>' ;
END      : '<End/>' ;

WS : [ \\t\\r\\n]+ -> skip ;
