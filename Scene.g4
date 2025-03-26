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

H        : 'h' ;
Y        : 'y' ;
ND       : 'nd' ;
OBJ      : 'obj' ;
NEAR_OBJ : 'near_obj' ;
END      : 'end' ;

WS : [ \t\r\n]+ -> skip ;
