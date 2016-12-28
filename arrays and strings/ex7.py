def rotate_image(image):
    size = len(image)
    if size == 0:
        return image
    rotated = [[] for i in range(size)]
    for i in range(size):
        for j in range(size):
            rotated[size - 1 - j].append(image[i][j])
    return rotated

image = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

rotated = rotate_image(image)
print 'image:'
for i in range(len(image)):
    print image[i]

print '\nrotated:'
for i in range(len(rotated)):
    print rotated[i]
