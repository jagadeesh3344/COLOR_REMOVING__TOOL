import cv2
import numpy as np

def remove_color(image, color_to_remove):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_range = np.array(color_to_remove[0])
    upper_range = np.array(color_to_remove[1])
    
    mask = cv2.inRange(hsv_image, lower_range, upper_range)
    result = cv2.bitwise_and(image, image, mask=mask)
    
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    return result

def main():
    image_path = input("Enter the path to the image: ")
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Unable to read the image.")
        return
    
    print("Choose the color to remove:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("4. Yellow")
    print("5. Orange")
    print("6. Purple")
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        color_to_remove = ([0, 100, 100], [10, 255, 255])  # Red color range in HSV
    elif choice == 2:
        color_to_remove = ([40, 100, 100], [80, 255, 255])  # Green color range in HSV
    elif choice == 3:
        color_to_remove = ([100, 100, 100], [140, 255, 255])  # Blue color range in HSV
    elif choice == 4:
        color_to_remove = ([20, 100, 100], [30, 255, 255])  # Yellow color range in HSV
    elif choice == 5:
        color_to_remove = ([10, 100, 100], [20, 255, 255])  # Orange color range in HSV
    elif choice == 6:
        color_to_remove = ([130, 100, 100], [160, 255, 255])  # Purple color range in HSV
    else:
        print("Invalid choice.")
        return
    
    removed_image = remove_color(image, color_to_remove)
    
    cv2.imshow("Original Image", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    cv2.imshow("Image with Color Removed", removed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
