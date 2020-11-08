grammar Graph;

TYPE: 'graph' ;
fragment DIGIT: [0-9];
NUMBER: DIGIT+;
LETTER: [A-Za-z];
CHAR: LETTER+DIGIT+;
EDGE: WHITESPACE'-''-'WHITESPACE;
WEIGHT: [0-9]+;
BRACKET: ('[' | ']') -> channel(HIDDEN);
WHITESPACE: (' ' | '\t') -> channel(HIDDEN);
NEWLINE: ('\r' | '\n') -> channel(HIDDEN);
IGNORE: ('"' | '{' | '}' | 'name=' | 'weight=') -> channel(HIDDEN);
SEMICOLON: ';' -> channel(HIDDEN);

graph: typegraph namegraph node+ edge+;
typegraph: TYPE;
namegraph: LETTER;
// nodeatrr: (name);
nodeindex: NUMBER+;
node: (nodeindex name);
name: (CHAR | LETTER+);
edge: (source EDGE destination weight);
weight: NUMBER+;
source: NUMBER+;
destination: NUMBER+;