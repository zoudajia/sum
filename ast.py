def get_ast(code):
    # 输入：每次一个方法一行
    asts = []
    try:
        tokens = javalang.tokenizer.tokenize(code)
        parser = javalang.parser.Parser(tokens)
        tree = parser.parse_member_declaration()
    except:
        return asts
    
    flatten = {}
    for i, (path, node) in enumerate(tree):
        flatten[i] = node
        
    
    for i, node in flatten.items():
        ast = {}
        ast["id"] = i
        tmp = str(type(node))
        ast["type"] = tmp.split('.')[-1][:-2]
        # 为每个节点获取子节点
        children = []
        for child in node.children:
            if isinstance(child, javalang.ast.Node):
                children.append(list(flatten.keys())[list(flatten.values()).index(child)])
            elif isinstance(child, list) and child:
                for i in range(len(child)):
                    if child[i] in flatten.values():
                        children.append(list(flatten.keys())[list(flatten.values()).index(child[i])])  

        if children:
            ast["children"] = children

        # 根据type获取value
        if ast["type"] == 'MethodDeclaration' \
                or ast['type'] == 'VariableDeclarator' \
                or ast['type']=='ReferenceType':
            ast["value"] = node.name
        elif ast['type'] == 'BasicType' \
                or ast['type'] == 'FormalParameter':
            ast['value'] = node.name
        elif ast['type'] == 'BinaryOperation':
            ast['value'] = node.operator
        elif ast['type'] == 'MethodInvocation' \
                or ast['type'] == 'MemberReference':
            ast['value'] = node.member
        elif ast['type'] == 'Literal':
            ast['value'] = node.value
        elif ast['type'] == 'Assignment':
            ast['value'] = node.type
        elif ast['type'] == 'ReturnStatement':
            ast['value'] = "return"
        elif ast['type'] == 'ForStatement':
            ast['value'] = 'for'
        elif ast['type'] == 'TryStatement':
            ast['value'] = 'try'
        elif ast['type'] == 'This' \
                or ast['type'] == 'ExplicitConstructorInvocation':
            ast['value'] = 'this'
        elif ast['type'] == 'BreakStatement':
            ast['value'] = 'break'
        elif ast['type'] == 'ContinueStatement':
            ast['value'] = 'continue'
        elif ast['type'] == 'TypeArgument':
            ast['value'] = str(node.pattern_type)
        elif ast['type'] == 'SuperMethodInvocation' \
                or ast['type'] == 'SuperMemberReference':
            ast['value'] = 'super.' + str(node.member)
        elif ast['type'] == 'VoidClassReference':
            ast['value'] = 'void.class'
        elif ast['type'] == 'SuperConstructorInvocation':
            ast['value'] = 'super'

        asts.append(ast)

    return asts


def get_rideof_no_asts(code, nl, func_name, project):
    error = []
    asts = {}
    for k,v in code.items():
        ast = get_ast(v)
        if len(ast) == 0:
            error.append(k)
        else:
            asts[k] = ast

    for k in error:
        del code[k]
        del nl[k]
        del func_name[k]
        del project[k]
        
    return code, nl, func_name, project, asts