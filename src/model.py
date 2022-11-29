class PQNModel:
    # available mode list
    MODE_LIST=['RSexci', 'RSinhi', 'FS', 'LTS', 'IB', 'EB', 'PB', 'Class2']

    # init
    def __init__(self, mode='RSexci'):
        self.PARAM={}
        self.Y={}
        self.state_variable_v=0
        self.state_variable_n=0
        self.state_variable_q=0
        self.state_variable_u=0
        self.set_mode(mode)

    # set mode
    def set_mode(self, mode):
        if (mode in self.MODE_LIST) is False:
            raise ValueError('mode should be RSexci, RSinhi, FS, LTS, IB, EB, PB, or Class2')
        self.mode=mode
        self.set_PARAM()
        self.set_Y()

    # set parameters of the given mode
    def set_PARAM(self):
        if self.mode=='RSexci':
            self.PARAM['dt']=0.0001
            self.PARAM['afn']=1.5625
            self.PARAM['afp']=-0.5625
            self.PARAM['bfn']=-1.125
            self.PARAM['cfn']=0
            self.PARAM['agn']=1
            self.PARAM['agp']=10.28125
            self.PARAM['bgn']=0.40625
            self.PARAM['cgn']=0
            self.PARAM['ahn']=0.28125
            self.PARAM['ahp']=9.125
            self.PARAM['bhn']=-7.1875
            self.PARAM['chn']=-2.8125
            self.PARAM['tau']=0.0064
            self.PARAM['I0']=2.375
            self.PARAM['k']=36.4375
            self.PARAM['phi']=4.75
            self.PARAM['epsq']=0.0693359375
            self.PARAM['rg']=0.0625
            self.PARAM['rh']=15.71875
            self.state_variable_v=-4906
            self.state_variable_n=27584
            self.state_variable_q=-3692
            self.BIT_WIDTH=18
            self.BIT_WIDTH_FRACTIONAL=10
            self.BIT_Y_SHIFT=20
        elif self.mode=='RSinhi':
            self.PARAM['dt']=0.0001
            self.PARAM['afn']=1.4375
            self.PARAM['afp']=-0.90625
            self.PARAM['bfn']=-1.0625
            self.PARAM['cfn']=0
            self.PARAM['agn']=0.75
            self.PARAM['agp']=14.1875
            self.PARAM['bgn']=0.625
            self.PARAM['cgn']=0
            self.PARAM['ahn']=0.0625
            self.PARAM['ahp']=13.0625
            self.PARAM['bhn']=-11.09375
            self.PARAM['chn']=-1.65625
            self.PARAM['tau']=0.0064
            self.PARAM['I0']=1.125
            self.PARAM['k']=93.6875
            self.PARAM['phi']=3.46875
            self.PARAM['epsq']=0.03515625
            self.PARAM['rg']=1.0625
            self.PARAM['rh']=0.40625
            self.state_variable_v= -4515
            self.state_variable_n= 19392
            self.state_variable_q= -1821
            self.BIT_WIDTH=18
            self.BIT_WIDTH_FRACTIONAL=10
            self.BIT_Y_SHIFT=20
        elif self.mode=='FS':
            self.PARAM['dt']=0.0001
            self.PARAM['afn']=1.9375
            self.PARAM['afp']=-1
            self.PARAM['bfn']=-1.77734375
            self.PARAM['cfn']=0
            self.PARAM['agn']=1.20703125
            self.PARAM['agp']=15.76171875
            self.PARAM['bgn']=-0.9296875
            self.PARAM['cgn']=0
            self.PARAM['ahn']=0
            self.PARAM['ahp']=3.3046875
            self.PARAM['bhn']=-10.94921875
            self.PARAM['chn']=0.74609375
            self.PARAM['tau']=0.0016
            self.PARAM['I0']=-0.8984375
            self.PARAM['k']=44.04296875
            self.PARAM['phi']=0.3203125
            self.PARAM['epsq']=0.01611328125
            self.PARAM['rg']=-0.89453125
            self.PARAM['rh']=-3.6875
            self.state_variable_v= -5423
            self.state_variable_n= 23536
            self.state_variable_q= 0
            self.BIT_WIDTH=18
            self.BIT_WIDTH_FRACTIONAL=10
            self.BIT_Y_SHIFT=20
        elif self.mode=='LTS':
            self.PARAM['dt']=0.0001
            self.PARAM['afn']=1.80859375
            self.PARAM['afp']=-0.0048828125
            self.PARAM['bfn']=-1.1787109375
            self.PARAM['cfn']=0
            self.PARAM['agn']=1.490234375
            self.PARAM['agp']=7.4296875
            self.PARAM['bgn']=-0.5908203125
            self.PARAM['cgn']=0
            self.PARAM['ahn']=-0.103515625
            self.PARAM['ahp']=0.099609375
            self.PARAM['bhn']=2.361328125
            self.PARAM['chn']=-0.048828125
            self.PARAM['tau']=0.0016
            self.PARAM['I0']=-4.6455078125
            self.PARAM['k']=16.076171875
            self.PARAM['phi']=0.4794921875
            self.PARAM['epsq']=0.006591796875
            self.PARAM['rg']=0.7490234375
            self.PARAM['rh']=-0.619140625
            self.PARAM['eta0']=1.7509765625
            self.PARAM['eta1']=1
            self.PARAM['ru']=-6.5185546875
            self.PARAM['alpu']=0.974609375
            self.PARAM['epsu']=0.009765625
            self.PARAM['v0']=0
            self.state_variable_v= -4941
            self.state_variable_n= 27331
            self.state_variable_q= -7540
            self.state_variable_u= -6733
            self.BIT_WIDTH=18
            self.BIT_WIDTH_FRACTIONAL=10
            self.BIT_Y_SHIFT=20
        elif self.mode=='IB':
            self.PARAM['dt']=0.0001
            self.PARAM['afn']=1.814453125
            self.PARAM['afp']=-0.00390625
            self.PARAM['bfn']=-0.759765625
            self.PARAM['cfn']=0
            self.PARAM['agn']=1.427734375
            self.PARAM['agp']=1.18359375
            self.PARAM['bgn']=-0.046875
            self.PARAM['cgn']=0
            self.PARAM['ahn']=-0.208984375
            self.PARAM['ahp']=-0.4658203125
            self.PARAM['bhn']=1.8828125
            self.PARAM['chn']=0.236328125
            self.PARAM['tau']=0.0008
            self.PARAM['I0']=-6.1103515625
            self.PARAM['k']=1.35546875
            self.PARAM['phi']=0.4462890625
            self.PARAM['epsq']=0.00360107421875
            self.PARAM['rg']=-1.201171875
            self.PARAM['rh']=-0.6953125
            self.PARAM['eta0']=1.328125
            self.PARAM['eta1']=1
            self.PARAM['ru']=-31.6728515625
            self.PARAM['alpu']=0.125
            self.PARAM['epsu']=0.01654052734375
            self.PARAM['v0']=0
            self.state_variable_v= -4566
            self.state_variable_n= 28448
            self.state_variable_q= -9338
            self.state_variable_u= -38287
            self.BIT_WIDTH=18
            self.BIT_WIDTH_FRACTIONAL=10
            self.BIT_Y_SHIFT=20
        elif self.mode=='EB':
            self.PARAM['dt']=0.0001
            self.PARAM['afn']=1.470703125
            self.PARAM['afp']=-0.1181640625
            self.PARAM['bfn']=-1.0224609375
            self.PARAM['cfn']=0
            self.PARAM['agn']=-1.92578125
            self.PARAM['agp']=11.0087890625
            self.PARAM['bgn']=0.6708984375
            self.PARAM['cgn']=0
            self.PARAM['ahn']=6.5380859375
            self.PARAM['ahp']=-9.513671875
            self.PARAM['bhn']=-1.607421875
            self.PARAM['chn']=12.787109375
            self.PARAM['tau']=0.0064
            self.PARAM['I0']=-11.89453125
            self.PARAM['k']=6.5234375
            self.PARAM['phi']=0.7861328125
            self.PARAM['epsq']=0.0098876953125
            self.PARAM['rg']=2.71875
            self.PARAM['rh']=1.2421875
            self.state_variable_v= -1782
            self.state_variable_n= -11519
            self.state_variable_q= 1
            self.BIT_WIDTH=18
            self.BIT_WIDTH_FRACTIONAL=10
            self.BIT_Y_SHIFT=20
        elif self.mode=='PB':
            self.PARAM['dt']=0.001
            self.PARAM['afn']=1.9814453125
            self.PARAM['afp']=-0.4521484375
            self.PARAM['bfn']=-0.9169921875
            self.PARAM['cfn']=0
            self.PARAM['agn']=1.25
            self.PARAM['agp']=16
            self.PARAM['bgn']=-0.2265625
            self.PARAM['cgn']=0
            self.PARAM['ahn']=-8.248046875
            self.PARAM['ahp']=14.658203125
            self.PARAM['bhn']=-2.259765625
            self.PARAM['chn']=15.8720703125
            self.PARAM['tau']=0.064
            self.PARAM['I0']=-0.4609375
            self.PARAM['k']=29.998046875
            self.PARAM['phi']=3.12890625
            self.PARAM['epsq']=0.00494384765625
            self.PARAM['rg']=2.1953125
            self.PARAM['rh']=-0.943359375
            self.PARAM['alpu']=0.201171875
            self.PARAM['epsu']=0.3043212890625
            self.PARAM['v0']=0.92578125
            self.state_variable_v= -3785
            self.state_variable_n= 18189
            self.state_variable_q= -19784
            self.state_variable_u= -16704
            self.BIT_WIDTH=18
            self.BIT_WIDTH_FRACTIONAL=10
            self.BIT_Y_SHIFT=20
        elif self.mode=='Class2':
            self.PARAM['dt']=0.0001
            self.PARAM['afn']=4
            self.PARAM['afp']=-4
            self.PARAM['bfn']=-2
            self.PARAM['cfn']=0
            self.PARAM['agn']=-3
            self.PARAM['agp']=3
            self.PARAM['bgn']=-2
            self.PARAM['cgn']=-16
            self.PARAM['tau']=0.0064
            self.PARAM['I0']=-16
            self.PARAM['k']=8
            self.PARAM['phi']=0.09375
            self.PARAM['rg']=-3
            self.state_variable_v= -1152487
            self.state_variable_n= 3403328
            self.BIT_WIDTH=28
            self.BIT_WIDTH_FRACTIONAL=20
            self.BIT_Y_SHIFT=20
        self.PARAM['bfp']=self.PARAM['afn']*self.PARAM['bfn']/self.PARAM['afp']
        self.PARAM['cfp']=self.PARAM['afn']*self.PARAM['bfn']**2+self.PARAM['cfn']-self.PARAM['afp']*self.PARAM['bfp']**2
        self.PARAM['bgp']=self.PARAM['rg']-self.PARAM['agn']*(self.PARAM['rg']-self.PARAM['bgn'])/self.PARAM['agp']
        self.PARAM['cgp']=self.PARAM['agn']*(self.PARAM['rg']-self.PARAM['bgn'])**2+self.PARAM['cgn']-self.PARAM['agp']*(self.PARAM['rg']-self.PARAM['bgp'])**2
        if self.mode!='Class2':
            self.PARAM['bhp']=self.PARAM['rh']-self.PARAM['ahn']*(self.PARAM['rh']-self.PARAM['bhn'])/self.PARAM['ahp']
            self.PARAM['chp']=self.PARAM['ahn']*(self.PARAM['rh']-self.PARAM['bhn'])**2+self.PARAM['chn']-self.PARAM['ahp']*(self.PARAM['rh']-self.PARAM['bhp'])**2

    # set coefficients Y
    def set_Y(self):
        f0=self.PARAM['dt']/self.PARAM['tau']*self.PARAM['phi']
        g0=self.PARAM['dt']/self.PARAM['tau']
        self.Y['v_vv_S']=int(f0*self.PARAM['afn']*2**self.BIT_Y_SHIFT)
        self.Y['v_vv_L']=int(f0*self.PARAM['afp']*2**self.BIT_Y_SHIFT)
        self.Y['v_v_S']=int(f0*(-2)*self.PARAM['afn']*self.PARAM['bfn']*2**self.BIT_Y_SHIFT)
        self.Y['v_v_L']=int(f0*(-2)*self.PARAM['afp']*self.PARAM['bfp']*2**self.BIT_Y_SHIFT)
        self.Y['v_c_S']=int((f0*(self.PARAM['afn']*self.PARAM['bfn']*self.PARAM['bfn']+self.PARAM['cfn']+self.PARAM['I0'])*2**self.BIT_WIDTH_FRACTIONAL))
        self.Y['v_c_L']=int((f0*(self.PARAM['afp']*self.PARAM['bfp']*self.PARAM['bfp']+self.PARAM['cfp']+self.PARAM['I0'])*2**self.BIT_WIDTH_FRACTIONAL))
        self.Y['v_n']=int(-f0*(2**self.BIT_Y_SHIFT))
        self.Y['v_q']=int(-f0*(2**self.BIT_Y_SHIFT))
        self.Y['v_I']=int(f0*self.PARAM['k']*2**self.BIT_Y_SHIFT)
        self.Y['n_vv_S']=int(g0*self.PARAM['agn']*2**self.BIT_Y_SHIFT)
        self.Y['n_vv_L']=int(g0*self.PARAM['agp']*2**self.BIT_Y_SHIFT)
        self.Y['n_v_S']=int(g0*(-2)*self.PARAM['agn']*self.PARAM['bgn']*2**self.BIT_Y_SHIFT)
        self.Y['n_v_L']=int(g0*(-2)*self.PARAM['agp']*self.PARAM['bgp']*2**self.BIT_Y_SHIFT)
        self.Y['n_n']=int(-g0*(2**self.BIT_Y_SHIFT))
        self.Y['n_c_S']=int((g0*(self.PARAM['agn']*self.PARAM['bgn']*self.PARAM['bgn']+self.PARAM['cgn'])*2**self.BIT_WIDTH_FRACTIONAL))
        self.Y['n_c_L']=int((g0*(self.PARAM['agp']*self.PARAM['bgp']*self.PARAM['bgp']+self.PARAM['cgp'])*2**self.BIT_WIDTH_FRACTIONAL))
        self.Y['rg']=int(self.PARAM['rg']*(2**self.BIT_WIDTH_FRACTIONAL))
        if (self.mode in ['RSexci', 'RSinhi', 'FS', 'LTS', 'IB', 'EB', 'PB']) is True:
            h0=self.PARAM['dt']/self.PARAM['tau']*self.PARAM['epsq']
            self.Y['q_vv_S']=int(h0*self.PARAM['ahn']*2**self.BIT_Y_SHIFT)
            self.Y['q_vv_L']=int(h0*self.PARAM['ahp']*2**self.BIT_Y_SHIFT)
            self.Y['q_v_S']=int(h0*(-2)*self.PARAM['ahn']*self.PARAM['bhn']*2**self.BIT_Y_SHIFT)
            self.Y['q_v_L']=int(h0*(-2)*self.PARAM['ahp']*self.PARAM['bhp']*2**self.BIT_Y_SHIFT)
            self.Y['q_q']=int(-h0*(2**self.BIT_Y_SHIFT))
            self.Y['q_c_S']=int((h0*(self.PARAM['ahn']*self.PARAM['bhn']*self.PARAM['bhn']+self.PARAM['chn'])*2**self.BIT_WIDTH_FRACTIONAL))
            self.Y['q_c_L']=int((h0*(self.PARAM['ahp']*self.PARAM['bhp']*self.PARAM['bhp']+self.PARAM['chp'])*2**self.BIT_WIDTH_FRACTIONAL))
            self.Y['rh']=int(self.PARAM['rh']*(2**self.BIT_WIDTH_FRACTIONAL))
            if (self.mode in ['LTS', 'IB']) is True:
                i0=self.PARAM['dt']/self.PARAM['tau']*self.PARAM['epsu']
                self.Y['u_v']=int(i0*2**self.BIT_Y_SHIFT)
                self.Y['u_u']=int(i0*(-self.PARAM['alpu'])*2**self.BIT_Y_SHIFT)
                self.Y['u_c']=int(i0*(-self.PARAM['v0'])*2**self.BIT_WIDTH_FRACTIONAL)
                self.Y['n_uS']=int(self.PARAM['eta0']*2**self.BIT_Y_SHIFT)
                self.Y['n_uL']=int(self.PARAM['eta1']*2**self.BIT_Y_SHIFT)
                self.Y['ru']=int(self.PARAM['ru']*2**self.BIT_WIDTH_FRACTIONAL)
            if (self.mode in ['PB']) is True:
                i0=self.PARAM['dt']/self.PARAM['tau']*self.PARAM['epsu']
                self.Y['u_v']=int(i0*2**self.BIT_Y_SHIFT)
                self.Y['u_u']=int(i0*(-self.PARAM['alpu'])*2**self.BIT_Y_SHIFT)
                self.Y['u_c']=int(i0*(-self.PARAM['v0'])*2**self.BIT_WIDTH_FRACTIONAL)
                self.Y['v_u']=int(-f0*(2**self.BIT_Y_SHIFT))

    # calculate Δv for the RSexhi, RSinhi, FS, LTS, IB, and EB modes
    def dv0(self,I_float):
        B=self.BIT_Y_SHIFT
        I=int(I_float*2**self.BIT_WIDTH_FRACTIONAL)
        v=self.state_variable_v
        n=self.state_variable_n
        q=self.state_variable_q
        vv=int(v*v >> self.BIT_WIDTH_FRACTIONAL)
        if v<0:
            v0=(self.Y['v_vv_S']*vv >> B)+(self.Y['v_v_S']*v >> B)+self.Y['v_c_S']+(self.Y['v_n']*n >> B)+(self.Y['v_q']*q >> B)+(self.Y['v_I']*I >> B)
        else:
            v0=(self.Y['v_vv_L']*vv >> B)+(self.Y['v_v_L']*v >> B)+self.Y['v_c_L']+(self.Y['v_n']*n >> B)+(self.Y['v_q']*q >> B)+(self.Y['v_I']*I >> B)
        return v0

    # calculate Δv for the PB mode
    def dv1(self,I_float):
        B=self.BIT_Y_SHIFT
        I=int(I_float*2**self.BIT_WIDTH_FRACTIONAL)
        v=self.state_variable_v
        n=self.state_variable_n
        q=self.state_variable_q
        u=self.state_variable_u
        vv=int(v*v >> self.BIT_WIDTH_FRACTIONAL)
        if v<0:
            v0=(self.Y['v_vv_S']*vv >> B)+(self.Y['v_v_S']*v >> B)+self.Y['v_c_S']+(self.Y['v_n']*n >> B)+(self.Y['v_q']*q >> B)-(self.Y['v_u']*u >> B)+(self.Y['v_I']*I >> B)
        else:
            v0=(self.Y['v_vv_L']*vv >> B)+(self.Y['v_v_L']*v >> B)+self.Y['v_c_L']+(self.Y['v_n']*n >> B)+(self.Y['v_q']*q >> B)-(self.Y['v_u']*u >> B)+(self.Y['v_I']*I >> B)
        return v0

    # calculate Δv for the Class2 mode
    def dv2(self,I_float):
        B=self.BIT_Y_SHIFT
        I=int(I_float*2**self.BIT_WIDTH_FRACTIONAL)
        v=self.state_variable_v
        n=self.state_variable_n
        vv=int(v*v >> self.BIT_WIDTH_FRACTIONAL)
        if v<0:
            v0=(self.Y['v_vv_S']*vv >> B)+(self.Y['v_v_S']*v >> B)+self.Y['v_c_S']+(self.Y['v_n']*n >> B)+(self.Y['v_I']*I >> B)
        else:
            v0=(self.Y['v_vv_L']*vv >> B)+(self.Y['v_v_L']*v >> B)+self.Y['v_c_L']+(self.Y['v_n']*n >> B)+(self.Y['v_I']*I >> B)
        return v0

    # calculate Δn for the RSexhi, RSinhi, FS, EB and Class2 modes
    def dn0(self):
        B=self.BIT_Y_SHIFT
        v=self.state_variable_v
        n=self.state_variable_n
        vv=int(v*v >> self.BIT_WIDTH_FRACTIONAL)
        if v<self.Y['rg']:
            n0=(self.Y['n_vv_S']*vv >> B)+(self.Y['n_v_S']*v >> B)+self.Y['n_c_S']+(self.Y['n_n']*n >> B)
        else:
            n0=(self.Y['n_vv_L']*vv >> B)+(self.Y['n_v_L']*v >> B)+self.Y['n_c_L']+(self.Y['n_n']*n >> B)
        return n0

    # calculate Δn for the LTS and IB modes
    def dn1(self):
        B=self.BIT_Y_SHIFT
        v=self.state_variable_v
        n=self.state_variable_n
        u=self.state_variable_u
        vv=int(v*v >> self.BIT_WIDTH_FRACTIONAL)
        if v<self.Y['rg']:
            n0=(self.Y['n_vv_S']*vv >> B)+(self.Y['n_v_S']*v >> B)+self.Y['n_c_S']+(self.Y['n_n']*n >> B)
        else:
            n0=(self.Y['n_vv_L']*vv >> B)+(self.Y['n_v_L']*v >> B)+self.Y['n_c_L']+(self.Y['n_n']*n >> B)
        if u<self.Y['ru']:
            n0=n0*self.Y['n_uS'] >> B
        else:
            n0=n0*self.Y['n_uL'] >> B
        return n0

    # calculate Δq for the RSexhi, RSinhi, FS, LTS, IB, EB and PB modes
    def dq0(self):
        B=self.BIT_Y_SHIFT
        v=self.state_variable_v
        q=self.state_variable_q
        vv=int(v*v >> self.BIT_WIDTH_FRACTIONAL)
        if v<self.Y['rh']:
            q0=(self.Y['q_vv_S']*vv >> B)+(self.Y['q_v_S']*v >> B)+self.Y['q_c_S']+(self.Y['q_q']*q >> B)
        else:
            q0=(self.Y['q_vv_L']*vv >> B)+(self.Y['q_v_L']*v >> B)+self.Y['q_c_L']+(self.Y['q_q']*q >> B)
        return q0

    # calculate Δu for the LTS, IB, and PB modes
    def du0(self):
        B=self.BIT_Y_SHIFT
        v=self.state_variable_v
        u=self.state_variable_u
        vv=int(v*v >> self.BIT_WIDTH_FRACTIONAL)
        u0=(self.Y['u_v']*v >> B)+(self.Y['u_u']*u >> B) + self.Y['u_c']
        return u0

    # update all state variables
    def update(self,I_float):
        if (self.mode in ['RSexci', 'RSinhi', 'FS', 'EB']) is True:
            dv=self.dv0(I_float)
            dn=self.dn0()
            dq=self.dq0()
            self.state_variable_v+=dv
            self.state_variable_n+=dn
            self.state_variable_q+=dq
        elif (self.mode in ['LTS', 'IB']) is True:
            dv=self.dv0(I_float)
            dn=self.dn1()
            dq=self.dq0()
            du=self.du0()
            self.state_variable_v+=dv
            self.state_variable_n+=dn
            self.state_variable_q+=dq
            self.state_variable_u+=du
        elif self.mode == 'PB':
            dv=self.dv1(I_float)
            dn=self.dn0()
            dq=self.dq0()
            du=self.du0()
            self.state_variable_v+=dv
            self.state_variable_n+=dn
            self.state_variable_q+=dq
            self.state_variable_u+=du
        if self.mode == 'Class2':
            dv=self.dv2(I_float)
            dn=self.dn0()
            self.state_variable_v+=dv
            self.state_variable_n+=dn

    # get membrane potential
    def get_membrane_potential(self):
        return self.state_variable_v/2**self.BIT_WIDTH_FRACTIONAL
