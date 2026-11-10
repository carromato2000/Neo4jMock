from antlr4 import InputStream, CommonTokenStream
# Importa las clases generadas en el paso 1 (asegúrate de que estén en tu ruta o paquete)
from CypherLexer import CypherLexer
from CypherParser import CypherParser
from CypherVisitor import CypherVisitor

class MyCypherVisitor(CypherVisitor):
    def visitMatch(self, ctx):
        print("¡Cláusula MATCH detectada!")
        return self.visitChildren(ctx)

def parse_cypher(query: str):
    # 1. Crear el flujo de entrada
    input_stream = InputStream(query)
    
    # 2. Pasar la entrada al Lexer para generar tokens
    lexer = CypherLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    # 3. Pasar los tokens al Parser
    parser = CypherParser(token_stream)
    
    # 4. Iniciar el parsing desde la regla principal (por lo general 'oC_Cypher' o 'script')
    tree = parser.oC_Cypher() 
    
    # 5. Opcional: Recorrer el árbol con tu Visitor personalizado
    visitor = MyCypherVisitor()
    visitor.visit(tree)
    
    print("¡Consulta parseada exitosamente sin errores sintácticos!")

if __name__ == "__main__":
    query_ejemplo = "MATCH (n:Person {name: 'Alice'}) RETURN n.age"
    parse_cypher(query_ejemplo)
