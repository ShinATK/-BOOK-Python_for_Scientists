# Mandelbrot set
import numpy as np
from time import time

# Set the parameters
max_iter = 256			# maximum number of iteration
nx, ny = 1024, 1024		# x- and y- image resolutions
x_lo, x_hi = 2.0, 1.0 	# x bounds in complex plane
y_lo, y_hi = -1.5, 1.5 	# y bounds in complex plane
start_time = time()

# Construct the two-dimensional arrays
ix, iy = np.mgrid[0:nx, 0:ny]
x, y = np.mgrid[x_lo:x_hi:1j*nx, y_lo:y_hi:1j*ny]
c=x+1j*y
esc_parm = np.zeros((ny, nx, 3), dtype='uint8')	# holds pixel rgb data

# Flattened arrays
nxny = nx * ny
ix_f = np.reshape(ix, nxny)
iy_f = np.reshape(iy, nxny)
c_f = np.reshape(c, nxny)
z_f = c_f.copy()	# the interated variable

for iter in range(max_iter):	# do the iterations
	if not len(z_f):			# all points have escaped
		break
	# rgd values for this choice of iter
	n = iter+1
	r, g, b = n%4*64, n%8*32, n%16*16
	# Mandelbrot evolution
	z_f*=z_f
	z_f+=c_f
	escape = np.abs(z_f) > 2.0 		# points which are escaping
	# Set the rgb pixel value for the escaping points
	esc_parm[iy_f[escape], ix_f[escape], :] = r, g, b
	escape = ~escape				# points not escaping
	# Remove batch of newly escaped points from flattened arrays
	ix_f = ix_f[escape]
	iy_f = iy_f[escape]
	c_f = c_f[escape]
	z_f = z_f[escape]

print("Time taken=", time(), - start_time)

from PIL import Image

picture = Image.fromarray(esc_parm)
picture.show()
# picture.save('mandelbrot.jpg')


