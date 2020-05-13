import pandas as pd
from ospacial.graphdraw import draw_graph


class DrawLogger:

    def __init__(self, trials, ps, basedir):
        self.trials = trials
        self.ps = ps
        self.case_limit = 10
        self.pos_count = {p: 0 for p in ps}
        self.neg_count = {p: 0 for p in ps}
        self.draw_fname_str = basedir + '/prop_{:.1f}_graph_{:s}_{:d}.png'

    def log(self, p, i, pos, payload):
        og = payload[0]
        solver = payload[1]
        source = payload[2]
        if pos:
            if self.pos_count[p] < self.case_limit:
                path = solver.path_to_food(source)
                draw_graph(og, self.draw_fname_str.format(p, 'pos', self.pos_count[p]), source=source, path=path)
                self.pos_count[p] = self.pos_count[p] + 1
        else:
            if self.neg_count[p] < self.case_limit:
                draw_graph(og, self.draw_fname_str.format(p, 'neg', self.neg_count[p]), source=source)
                self.neg_count[p] = self.neg_count[p] + 1

    def finalise(self):
        pass


class DataLogger:

    def __init__(self, trials, ps, basedir):
        self.trials = trials
        self.ps = ps
        self.case_limit = 100
        self.count = {p: 0 for p in ps}
        self.data = {p: [] for p in ps}
        self.data_fname_str = basedir + '/prop_{:.1f}.csv'

    def log(self, p, i, pos, payload):
        og = payload[0]
        if pos and self.count[p] < self.case_limit:
            self.data[p].append(og.hot_list())
            self.count[p] = self.count[p] + 1

    def finalise(self):
        for p, d in self.data.items():
            df = pd.DataFrame(d)
            df.to_csv(self.data_fname_str.format(p))