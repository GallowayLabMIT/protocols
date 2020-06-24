from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition

import sphinx.locale
from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

class time_estimate(nodes.Admonition, nodes.Element):
    pass


class TimeEstimateDirective(SphinxDirective):
    # this enables content in the directive
    has_content = True

    def run(self):
        estimate_node = time_estimate('\n'.join(self.content))
        #print(self.content)
        #print(self.content.data[0])
        #estimate_node += nodes.title('Estimated time', 'Estimated time: {}'.format(self.content.data[0]))
        #del self.content.data[0]
        self.state.nested_parse(self.content, self.content_offset, estimate_node)
        return [estimate_node]

def visit_time_estimate(self, node, name=''):
    sphinx.locale.admonitionlabels['admonition-time'] = 'Estimated time'
    try:
        self.visit_admonition(node, 'admonition-time')
    except TypeError:
        self.visit_admonition(node)
        self.body.append('{Estimated time:}')
    #if not isinstance(node[0], nodes.title):
    #    node.insert(0, nodes.title('time', _('Estimated time')))

def depart_time_estimate(self, node=None):
    self.depart_admonition(node)

def setup(app):
    app.add_directive('time', TimeEstimateDirective)

    app.add_node(time_estimate,
        html=(visit_time_estimate, depart_time_estimate),
        latex=(visit_time_estimate, depart_time_estimate),
        text=(visit_time_estimate, depart_time_estimate)
    )