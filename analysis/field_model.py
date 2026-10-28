import numpy as np
R=4.5; L=20.0
def field(J, px,py,pz, R=R,L=L, nphi=128, nz=64, theta=0.0):
    """Diametric cylinder, axis along x, centered at origin, magnetization in y-z plane at angle theta from +z (toward +y).
    Returns B (T if J in T) at point(s). Surface charge model on curved surface."""
    phi=np.linspace(0,2*np.pi,nphi,endpoint=False); w_phi=2*np.pi/nphi
    xg,wg=np.polynomial.legendre.leggauss(nz); xs=xg*L/2; wz=wg*L/2
    PH,XS=np.meshgrid(phi,xs,indexing='ij'); W=np.outer(np.full(nphi,w_phi),wz)
    # surface point: (x, R sin phi, R cos phi) ; outward normal (0,sin,cos); M dir (0,sin th, cos th)
    sig=np.cos(PH-theta)
    sx,sy,sz=XS,R*np.sin(PH),R*np.cos(PH)
    dx,dy,dz=px-sx,py-sy,pz-sz; r3=(dx*dx+dy*dy+dz*dz)**1.5
    f=J/(4*np.pi)*sig*R*W/r3
    return np.array([(f*dx).sum(),(f*dy).sum(),(f*dz).sum()])
def amps(J,h,a=0.0,y=0.0):
    """sensor at (a, y, -h) below the axis. radial amplitude (theta=0 -> m along z), tangential (theta=90)"""
    B0=field(J,a,y,-h,theta=0.0); B90=field(J,a,y,-h,theta=np.pi/2)
    return B0,B90
if __name__=='__main__':
    V=np.pi*R*R*L
    for h in (12,20,30,37,100):
        B0,B90=amps(1.0,h)
        dip=2*V/(4*np.pi*h**3)
        print(h,'Bz(th0) %.5f mT/T'%(B0[2]*1e3) ,'By(th90) %.5f'%(B90[1]*1e3),'ratio %.4f'%(B90[1]/B0[2]),'dipole radial %.5f'%(-dip*1e3), 'Bx',B0[0],B90[0])
