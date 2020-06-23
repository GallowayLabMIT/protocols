from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

class time_estimate(nodes.Admonition, nodes.Element):
    pass

class TimeEstimateDirective(BaseAdmonition):
    node_class = time_estimate


def visit_time_estimate(self, node, name=''):
    if not isinstance(node[0], nodes.title):
        node.insert(0, nodes.title('time_estimate', _('Estimated time')))

def depart_time_estimate(self, node=None):
    self.depart_admonition(node)

def setup(app):
    app.add_directive('time_estimate', TimeEstimateDirective)

    app.add_node(time_estimate,
        html=(visit_time_estimate, depart_time_estimate),
        latex=(visit_time_estimate, depart_time_estimate),
        text=(visit_time_estimate, depart_time_estimate)
    )