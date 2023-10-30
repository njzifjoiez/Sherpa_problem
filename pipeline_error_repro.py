from sherpa.astro import ui as sherpa
import sys


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

    sherpa.plot_fit(0)
    import matplotlib.pyplot as plt

    plt.show()
    return None
