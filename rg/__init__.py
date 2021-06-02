import networkx as nx


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
        return self