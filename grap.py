import graphviz as gv
from graphviz import Digraph

dot=Digraph(comment='Automata Impar')
#dot  #doctest: +ELLIPSIS
dot.node('P','p')
dot.node('Q','q')
dot.node('R','r')

dot.edges(['PP','PQ','QQ','QR'])
dot.render('test-output/grap.gv', view=True)