import cv2
import os

# initialize bounding box points and boolean
# indicating whether cropping is being performed
refPt = []
cropping = False
imagePath = "./wholeImage/"
record_file = open('record.txt', 'w')


def click_and_crop(event, x, y, flags, param):
    global refPt, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False

        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


if __name__ == '__main__':

    imageNames = os.listdir(imagePath)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)

    for image_name in imageNames:
        image = cv2.imread(os.path.join('wholeImage', image_name))
        clone = image.copy()
        while True:
            cv2.imshow("image", image)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("r"):
                image = clone.copy()
            elif key == ord(" "):
                """ recording body """
                cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
                cv2.imshow("image", image)
                record_file.write("%s\n" % image_name)
                for item in refPt:
                    record_file.write("%d %d\n" % item)
                del refPt[:]
            elif key == ord("q"):
                break

    record_file.close()
    cv2.destroyAllWindows()




