expressão = input("Para validar coloque a sequência correta:")
x = 0
pilha = []
while x < len(expressão):
    if expressão[x] == "(":
        pilha.append("(")

    if expressão[x] == "[":
        pilha.append("[")

    if expressão[x] == "{":
        pilha.append("{")

    if expressão[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")
            break

    if expressão[x] == "]":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append("]")
            break

    if expressão[x] == "}":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append("}")
            break

    x = x + 1
if len(pilha) == 0:
    print("Certo")
else:
    print("Errado")