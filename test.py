from lexer import PL0Lexer
from pygments.lexers.go import GoLexer

pl0code = """  

VAR x, squ;

PROCEDURE square;
BEGIN
   squ:= x * x
END;

BEGIN
   x := 1;
   WHILE x <= 10 DO
   BEGIN
      CALL square;
      ! squ;
      x := x + 1
   END
END.
"""

gocode = """
package main
  
import "fmt"

func main() {
	fmt.Println("Hello")
}
"""

def f(lexer, code):
	for token in lexer.get_tokens(code):
		print(token)

lexer, code = PL0Lexer(), pl0code
# lexer, code = GoLexer(), gocode
f(lexer, code)
