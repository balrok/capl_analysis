from CaplListener import CaplListener
import copy
import re

if __name__ is not None and "." in __name__:
    from .CaplParser import CaplParser
else:
    from CaplParser import CaplParser

from AST import Variable, Function


def extract_text(file_content, start, stop):
    sl = start.line
    sc = start.column
    el = stop.line
    ec = stop.column + 1# + len(stop.text)
    lines = file_content[sl-1:el]
    lines[0] = lines[0][sc:]
    lines[-1] = lines[-1][:ec]
    return lines

class CaplToCListener(CaplListener):
    in_global_ctx = True
    global_vars = []
    all_functions = []
    current_function = None

    file_content = None

    def enterDeclaration(self, ctx:CaplParser.DeclarationContext):
        raw = "\n".join(extract_text(self.file_content, ctx.start, ctx.stop)).strip("/\\ \n\r")
        vb = Variable(ctx.getText(), raw)
        vb.type = ctx.declarationSpecifiers().getText()

        s = ctx.declarationSpecifiers()
        for ss in s.declarationSpecifier():
            q = ss.typeSpecifier()
            if q is not None:
                vb.name = q.getText()

        l = ctx
        vlist = []
        while True:
            l = l.initDeclaratorList()
            if l == None:
                break
            v = copy.copy(vb)
            vlist.append(v)
            i = l.initDeclarator()
            v.name = i.declarator().getText()
            v.name = re.sub("\[.*","", v.name)
            if i.initializer() is not None:
                v.setInit(i.initializer().getText())
        if len(vlist) == 0:
            vlist.append(vb)
        for v in vlist:
            if self.in_global_ctx:
                self.global_vars.append(v)

    def enterFunctionDefinition(self, ctx:CaplParser.FunctionDefinitionContext):
        raw = "\n".join(extract_text(self.file_content, ctx.compoundStatement().start, ctx.compoundStatement().stop))
        raw_head = "\n".join(extract_text(self.file_content, ctx.start, ctx.compoundStatement().start)).strip(" \n\r{")
        if raw_head.startswith("on"):
            raw_head = raw_head.replace("on timer ", "void func_")
            raw_head = raw_head.replace("on sysvar ", "void func_")
            if raw_head.startswith("on start"):
                raw = raw[:-1] + "return 0;}"
                raw_head = raw_head.replace("on start", "int main")
            if raw_head.startswith("on message *"):	
                raw_head = raw_head.replace("on message *", "void handle_message")
                raw = "{ message * msgthis;" + raw[1:]
            raw_head += "()"
        raw_head = raw_head.replace("matrix[][]", "matrix[][40]")
        raw_head = raw_head.replace("[][]", "[][10]")
        if "msg." in raw or "this." in raw:
            for i in range(9):
                raw = raw.replace("byte(%d)"%i, "byte_%d"%i)
                raw = raw.replace("word(%d)"%i, "word_%d"%i)
            raw = raw.replace("msg.", "msg->")
            raw = raw.replace("this.", "msgthis->")

        raw = raw_head + raw

        f = Function(ctx.getText(), raw, raw_head+";")
        if ctx.declarationSpecifiers() is not None:
            f.type = ctx.declarationSpecifiers().getText()
        if ctx.declarator() is not None:
            d = ctx.declarator().directDeclarator()
            if d is not None:
                if d.directDeclarator() is not None:
                    d = d.directDeclarator()
                f.name = d.getText()

        self.all_functions.append(f)
        self.current_function = f

    def enterVariablesDeclaration(self, ctx:CaplParser.VariablesDeclarationContext):
        self.in_global_ctx = True
    def exitVariablesDeclaration(self, ctx:CaplParser.VariablesDeclarationContext):
        self.in_global_ctx = False
