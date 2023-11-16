from sherpa.astro import ui as sherpa
from sherpa.models import basic as sherpa_mod
from sherpa.astro.instrument import create_delta_rmf
from sherpa.astro.instrument import create_arf
from sherpa.astro.instrument import Response1D
from scipy.interpolate import splev
from scipy.interpolate import splrep
import sys
import sherpa as bsherpa
import numpy as np
import matplotlib.pyplot as plt
print(bsherpa.__version__)
print(bsherpa.__file__)
#sherpa.set_xschatter(50)


def func_test():
    sherpa.load_pha(0,'S1063_18611.pi')
    sherpa.set_analysis('energy')
    sherpa.set_model(0, sherpa.xsphabs.phabs*sherpa.xsapec.apec)
    sherpa.notice(0.5,7.0)

    phabs.nH = 0.012931465325827
    apec.redshift=0.3475
    apec.Abundanc=0.3
    apec.kT=8.0
    apec.norm=1.

    sherpa.freeze(phabs.nH,apec.redshift)

    sherpa.set_stat('chi2gehrels')
    sherpa.set_method('levmar')
    sherpa.fit(0)
    
    fplot = sherpa.get_fit_plot(0)
    print(fplot.dataplot.x)
    print(fplot.modelplot.x)
    print("---")
    print(fplot.dataplot.y)
    print(fplot.modelplot.y)
    plt.savefig("test.png")

    #sherpa.plot_fit(0)
    #import matplotlib.pyplot as plt

    #plt.show()
    return None

