import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.colors import LogNorm

# Shows the distribution of the numbers of the given tipps. The goal is to
# see that all number are distributed equally or where the blacklist items
# have impact.
class HistogramBase:
    # needs to be called before drawing to a new sub plot, see
    # matplot doc for info
    def newplot(self, idx, name):
        plt.subplot(2, 1, idx, label=name)
    
    def tipps(self, tipps):
        self.newplot(1, 'Tipps')
        self.tipps_do(tipps)

    def tipps_do(self, tipps):
        1
        
    def skipped(self, skipped):
        self.newplot(2, 'Skipped')
        self.skipped_do(skipped)

    def skipped_do(self, skipped):
        1

    def show(self):
        plt.show()

class Histogram(HistogramBase):
    def tipps_do(self, tipps):
        numbers = []
        for t in tipps:
            numbers += t.numbers()
        plt.hist(numbers, bins=49, color='tab:blue')
        plt.title('Tipps')
        
    def skipped_do(self, skipped):
        numbers = []
        for s in skipped:
            numbers += s.tipp.numbers()
        plt.hist(numbers, bins=49, color='tab:red')
        plt.title('Skipped')

class Histogram2d(HistogramBase):
    def _draw(self, name, tipps):
        plotdata = [[0. for x in range(7)] for y in range(7)] 
        for t in tipps:
            coords = t.get_coords()
            for coord in coords:
                plotdata[coord[1]][coord[0]] += 1.

        if len(tipps):
            for i in range(7):
                for j in range(7):
                    plotdata[i][j] = plotdata[i][j] / float(len(tipps)) * 7.;

        plt.pcolormesh(
                plotdata,
                norm=colors.Normalize())
        plt.gca().invert_yaxis()
        plt.colorbar()
        plt.title(name)


    def tipps_do(self, tipps):
        self._draw('Tipps', tipps)
        
    def skipped_do(self, skipped):
        self._draw('Skipped', [s.tipp for s in skipped])

