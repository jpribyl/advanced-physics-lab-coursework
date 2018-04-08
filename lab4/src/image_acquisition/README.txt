Steps to aquire data using a Basler USB 3.0 camera

1. Plug the Basler camera into a USB 3.0 port. These ports are commonly blue and have "SS" next to them.

2. Run the pylon5 viewer app by typing in the terminal:
"/opt/pylon5/bin/PylonViewerApp"
without the quotes.

3. The camera should show up in the list of devices. Click on the camera name and the open button in the top left of the software. In order to see all of the features of the camera, switch the user level to "Guru".

4. Under the features tab, open the camera's subsection. There, open the "User Set Control" subsection. "User Set Default" needs to be set to "User Set 1". 

5. Parameters can be changed and should be saved to "User Set 1". These parameters could then be loaded at a future time.

6. Close the camera from the software.

7. Open "acquire_images.cpp" for editing.

8. Go to the lines

// Number of images to be grabbed.
static const uint32_t c_countOfImagesToGrab = x;

// Size of the image captured
static const uint32_t pixels_horizontal = 1024;
static const uint32_t pixels_vertical = 128;

c_countOfImagesToGrab should be changed to however many frames you want to collect. 
pixels_horizontal and pixels_vertical must match what is set in the software.

9. Compile the file by typing
"make" 
in the terminal without quotes.

10. To run the code, type
"./acquire_images | pigz -b 1000 -1 - > data.gz"
in the terminal without quotes. This utilizes parallel gzip to compress the data.

11. Uncompress the data by typing
"gunzip data.gz"
in the terminal without the quotes.

12. To retrieve png files of each frame, type
"ffmpeg -vcodec rawvideo -f rawvideo -pix_fmt gray16le -s 1024x128 -i data output%07d.png"
in the terminal without quotes. The "1024x128" should match the resolution set in the software and code (pixels_horizontalxpixels_vertical).
