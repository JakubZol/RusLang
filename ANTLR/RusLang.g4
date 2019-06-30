grammar RusLang;

/*
Tokens
*/

T_END_LINE      :('.');
T_NUMBER        :('номер');
T_STRING        :('надпись');
T_BOOL          :('логический');
T_VOID          :('пустой');
T_IF            :('если');
T_ELSE          :('еще');
T_ELIF          :('иначе_если');
T_FOR           :('для');
T_FROM          :('от');
T_TO            :('до');
T_WHILE         :('цикл');
T_NOT           :('не');
T_AND           :('и');
T_OR            :('или');
T_FUNCTION      :('функция');
T_RETURN        :('ответ');
T_PRINT         :('показ');
T_TRUE          :('правда');
T_FALSE         :('ложный');
T_END           :('конец');
T_BREAK         :('стоп');
T_CONTINUE      :('продолжать');
T_PLUS          :'+';
T_MINUS         :'-';
T_MUL           :'*';
T_DIV           :'/';
T_POW           :'^';
T_CONCAT        :'++';
T_ASSIGN        :'<-';
T_G             :'>';
T_L             :'<';
T_EQ            :'=';
T_GEQ           :'>=';
T_LEQ           :'<=';
T_NEQ           :'/=';
T_DOTS          :':';
T_LBRACKET      :'(';
T_RBRACKET      :')';
T_LSQUARE       :'[';
T_RSQUARE       :']';
T_COMMA         :',';
T_COMMENT       :('#'[a-zA-Z_ąćęłńóśźżБбвГгДдЁёЖжЗзИиЙйкЛлмноПптУФфЦцЧчШшЩщЪъЫыЬьЭэЮюЯя0-9 \t;]*[\n] | '#{'[a-zA-Z_ąćęłńóśźżБбвГгДдЁёЖжЗзИиЙйкЛлмноПптУФфЦцЧчШшЩщЪъЫыЬьЭэЮюЯя0-9 \t\n;]*'}#');
T_NUMBER_VAL    :[-]?[0-9]+([.][0-9]+)?;
T_STRING_VAL    :'"'[a-zA-Z_ąćęłńóśźżБбвГгДдЁёЖжЗзИиЙйкЛлмноПптУФфЦцЧчШшЩщЪъЫыЬьЭэЮюЯя0-9 \t\n;]*'"';
T_VAR_ID        :[a-zA-Z_БбвГгДдЁёЖжЗзИиЙйкЛлмноПптУФфЦцЧчШшЩщЪъЫыЬьЭэЮюЯя][a-zA-Z0-9_БбвГгДдЁёЖжЗзИиЙйкЛлмноПптУФфЦцЧчШшЩщЪъЫыЬьЭэЮюЯя]*;
T_WHITESPACE    :(' ' | '\t' | '\n') -> skip;


/* left= , right=*/
/*GRAMMAR*/

var_type:
    T_NUMBER | T_STRING | T_BOOL;

listValue:
    T_LSQUARE valueList T_RSQUARE;

listExpression:
    listValue | listExpression T_CONCAT listValue;

value:
    stringExpression | booleanExpression | arithmeticExpression | listExpression |T_VAR_ID;

varDeclaration:
    var_type T_VAR_ID T_ASSIGN value;


varAssignment:
    T_VAR_ID T_ASSIGN value;


arithmeticExpression:
    T_LBRACKET arithmeticExpression T_RBRACKET |
    arithmeticExpression (T_MUL | T_DIV) arithmeticExpression |
    arithmeticExpression (T_MINUS | T_PLUS) arithmeticExpression |
    T_NUMBER_VAL | T_VAR_ID;


stringExpression:
    stringExpression T_CONCAT stringExpression | T_STRING_VAL | T_VAR_ID | T_LBRACKET stringExpression T_RBRACKET;


booleanExpression:
    booleanExpression (T_AND | T_OR) booleanExpression | stringExpression (T_EQ | T_NEQ) stringExpression |
    arithmeticExpression (T_G | T_L | T_LEQ | T_GEQ | T_EQ | T_NEQ) arithmeticExpression | T_FALSE | T_TRUE |
    T_VAR_ID | T_NOT booleanExpression | T_LBRACKET booleanExpression T_RBRACKET;


printExpression:
    T_PRINT value | T_PRINT T_LBRACKET value T_RBRACKET;


expression:
    varDeclaration | varAssignment | printExpression | forLoopExpression | whileLoopExpression |
    conditionalExpression T_END | functionCall | functionDeclaration;


code:
    expression T_END_LINE |
    expression T_END_LINE code |
    T_COMMENT code;


program:
    code EOF;


forLoopExpression:
    T_FOR T_VAR_ID T_FROM arithmeticExpression T_TO arithmeticExpression T_DOTS loopCode T_END;


whileLoopExpression:
    T_WHILE booleanExpression T_DOTS loopCode T_END;


loopCode:
    code | loopCode (T_BREAK | T_CONTINUE) T_END_LINE loopCode |
    loopCode (T_BREAK | T_CONTINUE) T_END_LINE |
    (T_BREAK | T_CONTINUE) T_END_LINE loopCode;


conditionalExpression:
    T_IF booleanExpression T_DOTS code |  T_IF booleanExpression T_DOTS code elifExpression elseExpression |
    T_IF booleanExpression T_DOTS code elifExpression | T_IF booleanExpression T_DOTS code elseExpression;


elifExpression:
    T_ELIF booleanExpression T_DOTS code | elifExpression T_ELIF booleanExpression T_DOTS code;


elseExpression:
    T_ELSE T_DOTS code;


functionDeclaration:
    T_FUNCTION T_VAR_ID T_LBRACKET fullArgList T_RBRACKET T_DOTS code T_RETURN value T_END_LINE T_END |
    T_FUNCTION T_VAR_ID T_LBRACKET fullArgList T_RBRACKET T_DOTS code T_END |
    T_FUNCTION T_VAR_ID T_LBRACKET fullArgList T_RBRACKET T_DOTS T_RETURN value T_END_LINE T_END;



argList:
    var_type T_VAR_ID | argList T_COMMA var_type T_VAR_ID;


fullArgList:
    T_WHITESPACE | argList;


functionCall:
    T_VAR_ID T_LBRACKET fullValueList T_RBRACKET;


valueList:
    value | valueList T_COMMA value;


fullValueList:
    T_WHITESPACE | valueList;