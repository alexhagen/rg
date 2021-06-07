"""A module for capturing research progress in a graph form."""
import networkx as nx
import matplotlib.pyplot as plt
from grave import plot_network

class RG(nx.DiGraph):
    """A class for capturing research progress in graph form.

    RG is technically a ``networkx.DiGraph`` under the hood, so it can do
    anything that a ``networkx.DiGraph`` can do, with some extra things like
    a bibliography and better visualization.

    :param str project_name: The title for the project.
    """
    def __init__(self, project_name, *args, **kwargs):
        self.project_name = project_name
        super().__init__(*args, **kwargs)

    def add_branch(self, branch_name, branch_description, parent=None):
        """Add a branch of research to the project.

        :param str branch_name: The name of this branch
        :param str branch_description: A quick description of this branch
        :param str parent: The branch_name of research from which this research
            originated.  Leave as ``None`` if this is either an off the wall
            idea, or the start of a graph.
        """
        self.add_node(branch_name, description=branch_description)
        if parent is not None:
            self.add_edge(parent, branch_name)
        return self

    def plot(self):
        """Plot the research graph as a typical matplotlib graph."""
        #pos = nx.drawing.nx_pydot.graphviz_layout(self, prog='dot')
        #nx.draw(self, pos)
        plot_network(self)
        plt.show()
        return self
