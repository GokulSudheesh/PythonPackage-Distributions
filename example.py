from Gaussiandistribution import Gaussian
Gaussianobj1 = Gaussian(2,3)
Gaussianobj2 = Gaussian(4,5)
Gaussianobj3 = Gaussian()
Gaussianobj3 = Gaussianobj1+Gaussianobj2
print(Gaussianobj3.mean)