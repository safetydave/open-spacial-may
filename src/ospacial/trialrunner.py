from ospacial.officegraph import OfficeGraph
from ospacial.occupancy import Occupancy
from ospacial.solver import Solver


class TrialRunner:

    def __init__(self, trials, ps, logger=None):
        self.trials = trials
        self.ps = ps
        self.results = []
        self.logger = logger

    def run(self):
        for p in self.ps:
            s = 0
            for i in range(self.trials):
                # set up office and scenario
                og = OfficeGraph()
                occupancy = Occupancy(og.back_row(), og.all_desks(), p)
                og.apply_occupancy(occupancy.seating)
                # solve and tally result
                solver = Solver(og)
                pos = solver.can_haz_food(occupancy.source)
                s = s + pos
                # log stuff
                if self.logger:
                    self.logger.log(p, i, pos, (og, solver, occupancy.source))

            self.results.append(s / self.trials)

        if self.logger:
            self.logger.finalise()

    def summary(self):
        s = "Number of samples for each p: {}\n".format(self.trials)
        for i, p in enumerate(self.ps):
            s += ("{:.1f} {:.3f}\n".format(p, self.results[i]))
        return s
