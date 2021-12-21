import numpy as np 
import pickle

def ps_suppression_8param(theta, emul, return_std=False):
    log10Mc, mu, thej, gamma, delta, eta, deta, fb = theta
    # fb = 0.1612
    mins = [11, 0.0, 2, 1, 3,  0.2, 0.2, 0.10]
    maxs = [15, 2.0, 8, 4, 11, 0.4, 0.4, 0.25]
    assert mins[0]<=log10Mc<=maxs[0]
    assert mins[1]<=mu<=maxs[1]
    assert mins[2]<=thej<=maxs[2]
    assert mins[3]<=gamma<=maxs[3]
    assert mins[4]<=delta<=maxs[4]
    assert mins[5]<=eta<=maxs[5]
    assert mins[6]<=deta<=maxs[6]
    assert mins[7]<=fb<=maxs[7]
    theta = [log10Mc, mu, thej, gamma, delta, eta, deta, fb]
    if type(theta)==list: theta = np.array(theta)
    if theta.ndim==1: theta = theta[None,:]
    out = emul.predict_values(theta)#, return_std=True)
    # print(out.shape)
    return out.squeeze()

class use_emul:
	def __init__(self, emul_name):
		self.emul_name = emul_name
		self.load_emulators()
		
		self.fb = Ob/Om
		print('Baryon fraction is set to {:.3f}'.format(self.fb))
		self.load_emulators()
		self.fix_params()

	def load_emulators(self, emul_names=None):
		if emul_names is not None: self.emul_names = emul_names
		emulators = []
		zs = []
		for ke in self.emul_names:
			zs.append(float(ke))
			emu = pickle.load(open(self.emul_names[ke],'rb'))
			emu.options['print_prediction'] = False
			emulators.append(emu)
		print('Emulators loaded.')
		self.emulators = np.array(emulators)
		self.emul_zs   = np.array(zs)

	def fix_params(self):
		mu, gamma, delta, deta = 0.93, 2.25, 6.40, 0.240 
		thej, eta = 4.235, 0.22
		self.mu    = mu
		self.gamma = gamma
		self.delta = delta
		self.deta  = deta 
		self.thej  = thej 
		self.eta   = eta 

	def run(self, log10Mc=13.322, nu_Mc=-0.015, z=0):
		assert 12.3<=log10Mc<=14.5
		assert -0.1<=nu_Mc<=0.01
		assert 0<=z<=2

		if z in self.emul_zs:
			theta = [log10Mc*(1+z)**nu_Mc, self.mu, self.thej, self.gamma, self.delta, self.eta, self.deta, self.fb]
			emu0  = self.emulators[self.emul_zs==z][0]
			# print(emu0)
			ps = ps_suppression_8param(theta, emu0, return_std=False)
			return ps, ks0
		else:
			i0, i1 = nearest_element_idx(self.emul_zs, z)
			theta0 = [log10Mc*(1+self.emul_zs[i0])**nu_Mc, self.mu, self.thej, self.gamma, self.delta, self.eta, self.deta, self.fb]
			emu0   = self.emulators[i0]
			theta1 = [log10Mc*(1+self.emul_zs[i1])**nu_Mc, self.mu, self.thej, self.gamma, self.delta, self.eta, self.deta, self.fb]
			emu1   = self.emulators[i1]
			ps0 = ps_suppression_8param(theta0, emu0, return_std=False)
			ps1 = ps_suppression_8param(theta1, emu1, return_std=False)
			return ps0 + (ps1-ps0)*(z-self.emul_zs[i0])/(self.emul_zs[i1]-self.emul_zs[i0]), ks0



def nearest_element_idx(arr, a, both=True):
	if both:
		dist = np.abs(arr-a)
		dist_arg = np.argsort(dist)
		return  dist_arg[0], dist_arg[1]
	else:
		return np.abs(arr-a).argmin()


