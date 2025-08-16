// This grammar defines the Mixtec scene structure for parsing semasiographic elements.
// It expects XML-style tokens like <Human>...</Human>, <Obj>...</Obj>, etc.
// The parser is based on the context-free grammar rules outlined in the project documentation.


// The name of the grammar. This generates SceneLexer, SceneParser, SceneVisitor, etc.
grammar Scene; 

// --------------
// Parser Rules
// --------------

// Entry point of the parser: a full scene is made up of one or more complete sentences (sent), each ending in <End/>
s       : (sent END)+ ;

// A sentence can take three valid forms, according to the grammar:
// 1. A standalone clause
// 2. An object followed by either a date+clause or just a clause
// 3. A date followed by either an object+clause or just a clause

sent    : clause
        | OBJ (date clause | clause)
        | date (OBJ clause | clause)
        ;


// A clause is a sequence of one or more clause fragments (human figures, optionally named or associated with near-objects),
// optionally followed by a date tail or object tail.
clause  : clause_f+ (date_tail | obj_tail)? ;

// A date tail is a continuation that starts with a date, and may optionally include:
// - an object followed by one or more clause fragments
// - or just clause fragments
date_tail : date (OBJ clause_f+ | clause_f+)? ;

// An object tail is a continuation that starts with an object, and may optionally include:
// - a date followed by one or more clause fragments
// - or just clause fragments
obj_tail  : OBJ (date clause_f+ | clause_f+)? ;

// A date consists of a year token, optionally followed by a name-date symbol.
date    : Y ND? ;

// A clause fragment is a human figure, followed optionally by:
// - a name-date symbol or
// - a near-date 
clause_f: H (ND | near_date)? ;

// A near-date is a near-object followed optionally by a name-date.
near_date : NEAR_OBJ ND? ;


// --------------
// Lexer Rules (Tokens)
// These rules define the actual token types used above. 
// Each lexer rule matches a complete XML tag and captures it as a single token.
// --------------

// Lexer rules to match each full tag as a single token

Y        : '<year'     .*? '/>' ;        // Matches <year ... />
H        : '<human'    .*? '/>' ;        // Matches <human ... />
ND       : '<name_date' .*? '/>' ;       // Matches <name_date ... />
OBJ      : '<obj'      .*? '/>' ;        // Matches <obj ... />
NEAR_OBJ : '<near_obj' .*? '/>' ;        // Matches <near_obj ... />
END      : '<end'      .*? '/>' ;        // Matches <end ... />

// Match and skip any whitespace characters: spaces, tabs, carriage returns, and newlines.
// These are ignored by the parser and do not generate tokens.
WS       : [ \t\r\n]+ -> skip ;          // Skip whitespace


// Lexer rules for tags that should be ignored

XML_DECL : '<?xml' .*? '?>' -> skip ;   // Ignore XML declaration
SCENE_OPEN : '<scene>' -> skip ;        // Ignore <scene>
SCENE_CLOSE : '</scene>' -> skip ;      // Ignore </scene>
