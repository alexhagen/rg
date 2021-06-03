import networkx as nx
import matplotlib.pyplot as plt


class RG:
    def __init__(self, project_name):
        self.project_name = project_name
        self.G = nx.DiGraph()

    def add_branch(self, branch_name, branch_description, parent=None):
        self.G.add_node(branch_name, description=branch_description)
        if parent is not None:
            self.G.add_edge(self.G.nodes[parent], branch_name)
        return self

    def plot(self):
        pos = nx.drawing.nx_pydot.graphviz_layout(self.G, prog='twopi')
        nx.draw(self.G, pos)
        plt.show()
        return self