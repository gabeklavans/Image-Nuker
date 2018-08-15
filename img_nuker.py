from skimage import io
from skimage.viewer import ImageViewer
from skimage import exposure
from skimage.color import rgba2rgb

path = input("Enter path for img:")
folk = io.imread(path)

print(folk.shape)

folk = exposure.adjust_gamma(folk, gamma=0.35)
folk = exposure.rescale_intensity(folk, in_range=(160,215))
folk = exposure.rescale_intensity(folk, in_range=(50,230))

viewer = ImageViewer(folk)
viewer.show()
