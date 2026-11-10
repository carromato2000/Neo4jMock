from antlr4 import InputStream, CommonTokenStream, Token, TerminalNode
# Importa las clases generadas en el paso 1 (asegúrate de que estén en tu ruta o paquete)
from CypherLexer import CypherLexer
from CypherParser import CypherParser
from CypherVisitor import CypherVisitor

class MyCypherVisitor(CypherVisitor):
    def visitMatch(self, ctx):
        print("¡Cláusula MATCH detectada!")
        return self.visitChildren(ctx)

def print_tree(node, parser, prefix="", is_last=True):
    branch = "└── " if is_last else "├── "

    if isinstance(node, TerminalNode):
        symbol = node.getSymbol()
        token_type = symbol.type
        if token_type == Token.EOF:
            name = "EOF"
        elif 0 <= token_type < len(parser.symbolicNames) and parser.symbolicNames[token_type]:
            name = parser.symbolicNames[token_type]
        else:
            name = "TOKEN"

        label = f"{name}: {symbol.text!r}"
    else:
        label = parser.ruleNames[node.getRuleIndex()]

    print(prefix + branch + label)

    child_prefix = prefix + ("    " if is_last else "│   ")
    children = [node.getChild(i) for i in range(node.getChildCount())]

    for i, child in enumerate(children):
        print_tree(child, parser, child_prefix, i == len(children) - 1)

def parse_cypher(query: str):
    # 1. Crear el flujo de entrada
    input_stream = InputStream(query)
    
    # 2. Pasar la entrada al Lexer para generar tokens
    lexer = CypherLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    # 3. Pasar los tokens al Parser
    parser = CypherParser(token_stream)
    
    # 4. Iniciar el parsing desde la regla principal (por lo general 'oC_Cypher' o 'script')
    tree = parser.oC_Cypher() 
    for token in token_stream.tokens:
        tipo = token.type

        if tipo == Token.EOF:
            nombre = "EOF"
        elif 0 <= tipo < len(lexer.symbolicNames) and lexer.symbolicNames[tipo]:
            nombre = lexer.symbolicNames[tipo]
        elif 0 <= tipo < len(lexer.literalNames) and lexer.literalNames[tipo]:
            nombre = lexer.literalNames[tipo]
        else:
            nombre = f"TOKEN_{tipo}"

        print(f"{nombre} (tipo {tipo}): {token.text!r}")

    print("\nÁrbol de parseo:")
    print_tree(tree, parser)

    # 5. Opcional: Recorrer el árbol con tu Visitor personalizado
    visitor = MyCypherVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    query_ejemplo = "MATCH (n:Person {name: 'Alice'}) RETURN n.age"
    parse_cypher(query_ejemplo)
