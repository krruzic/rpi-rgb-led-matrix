namespace RPiRgbLEDMatrix;

/// <summary>
/// Represents a canvas whose pixels can be manipulated.
/// </summary>
public class RGBLedCanvas
{
    // This is a wrapper for canvas no need to implement IDisposable here
    // because RGBLedMatrix has ownership and takes care of disposing canvases
    internal IntPtr _canvas;

    // this is not called directly by the consumer code,
    // consumer uses factory methods in RGBLedMatrix
    internal RGBLedCanvas(IntPtr canvas)
    {
        _canvas = canvas;
        led_canvas_get_size(_canvas, out var width, out var height);
        Width = width;
        Height = height;
    }

    /// <summary>
    /// The width of the canvas in pixels.
    /// </summary>
    public int Width { get; private set; }

    /// <summary>
    /// The height of the canvas in pixels.
    /// </summary>
    public int Height { get; private set; }

    /// <summary>
    /// Sets the color of a specific pixel.
    /// </summary>
    /// <param name="x">The X coordinate of the pixel.</param>
    /// <param name="y">The Y coordinate of the pixel.</param>
    /// <param name="color">New pixel color.</param>
    public void SetPixel(int x, int y, Color color) => led_canvas_set_pixel(_canvas, x, y, color.R, color.G, color.B);

    /// <summary>
    /// Copies the colors from the specified buffer to a rectangle on the canvas.
    /// </summary>
    /// <param name="x">The X coordinate of the top-left pixel of the rectangle.</param>
    /// <param name="y">The Y coordinate of the top-left pixel of the rectangle.</param>
    /// <param name="width">Width of the rectangle.</param>
    /// <param name="height">Height of the rectangle.</param>
    /// <param name="colors">Buffer containing the colors to copy.</param>
    public void SetPixels(int x, int y, int width, int height, Span<Color> colors)
    {
        if (colors.Length < width * height)
            throw new ArgumentOutOfRangeException(nameof(colors));
        led_canvas_set_pixels(_canvas, x, y, width, height, ref colors[0]);
    }

    /// <summary>
    /// Sets the color of the entire canvas.
    /// </summary>
    /// <param name="color">New canvas color.</param>
    public void Fill(Color color) => led_canvas_fill(_canvas, color.R, color.G, color.B);

    /// <summary>
    /// Sets the color of the given section of the canvas.
    /// </summary>
    /// <param name="color">New canvas color.</param>
    public void SubFill(int x, int y, int width, int height, Color color) =>
        led_canvas_subfill(_canvas, x, y, width, height, color.R, color.G, color.B);

    /// <summary>
    /// Cleans the entire canvas.
    /// </summary>
    public void Clear() => led_canvas_clear(_canvas);
}
