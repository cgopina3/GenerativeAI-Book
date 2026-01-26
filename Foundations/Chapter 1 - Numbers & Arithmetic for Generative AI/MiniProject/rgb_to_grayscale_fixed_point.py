# RGB to Grayscale using Fixed-Point Arithmetic (No libraries)

def rgb_to_grayscale_fixed_point(r, g, b):
    # Fixed-point coefficients scaled by 1024
    y = (306 * r + 601 * g + 117 * b) >> 10
    return y


if __name__ == "__main__":
    # Example RGB values
    rgb_pixels = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (120, 200, 150)
    ]

    for r, g, b in rgb_pixels:
        gray = rgb_to_grayscale_fixed_point(r, g, b)
        print(f"RGB({r},{g},{b}) → Grayscale: {gray}")
