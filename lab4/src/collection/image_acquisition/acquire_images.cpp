// ParametrizeCamera_Configurations.cpp
/*
    Note: Before getting started, Basler recommends reading the Programmer's Guide topic
    in the pylon C++ API documentation that gets installed with pylon.
    If you are upgrading to a higher major version of pylon, Basler also
    strongly recommends reading the Migration topic in the pylon C++ API documentation.


    The instant camera allows to install event handlers for configuration purposes
    and for handling the grab results. This is very useful for handling standard
    camera setups and image processing tasks.

    This sample shows how to use configuration event handlers by applying the standard
    configurations and registering sample configuration event handlers.

    Configuration event handlers are derived from the CConfigurationEventHandler base class.
    CConfigurationEventHandler provides virtual methods that can be overridden. If the
    configuration event handler is registered these methods are called when the state of the
    instant camera objects changes, e.g.
     when the camera object is opened or closed.

    The standard configuration event handlers override the OnOpened method. The overridden method
    parametrizes the camera.

    Device specific camera classes, e.g. for GigE cameras, provide specialized
    event handler base classes, e.g. CBaslerGigEConfigurationEventHandler.
*/

// Include files to use the PYLON API.
#include <pylon/PylonIncludes.h>

// Setting for using Basler USB cameras.
#include <pylon/usb/BaslerUsbInstantCamera.h>
typedef Pylon::CBaslerUsbInstantCamera Camera_t;
using namespace Basler_UsbCameraParams;


// Include files used by samples.
#include "./include/include/ImageEventPrinter.h"
#include "./include/include/ConfigurationEventPrinter.h"
#include "./include/include/PixelFormatAndAoiConfiguration.h"

#include "sys/time.h"

// Namespace for using pylon objects.
using namespace Pylon;

// Namespace for using cout.
using namespace std;

// Number of images to be grabbed.
static const uint32_t c_countOfImagesToGrab = 10000;

// Size of the image captured
static const uint32_t pixels_horizontal = 32;
static const uint32_t pixels_vertical = 32;

int main(int argc, char* argv[]) {

  // The exit code of the sample application.
  int exitCode = 0;

  // Before using any pylon methods, the pylon runtime must be initialized.
  PylonInitialize();

  try {

    // Create an instant camera object with the first camera device found.
    CBaslerUsbInstantCamera camera(CTlFactory::GetInstance().CreateFirstDevice());

    // This smart pointer will receive the grab result data.
    CGrabResultPtr ptrGrabResult;

    // Register the standard configuration event handler for setting up the camera for continuous acquisition.
    // By setting the registration mode to RegistrationMode_ReplaceAll, the new configuration handler replaces the
    // default configuration handler that has been automatically registered when creating the
    // instant camera object.
    // The handler is automatically deleted when deregistered or when the registry is cleared if Cleanup_Delete is specified.
    camera.RegisterConfiguration(new CAcquireContinuousConfiguration, RegistrationMode_ReplaceAll, Cleanup_Delete);

    // The camera's Open() method calls the configuration handler's OnOpened() method that
    // applies the required parameter modifications.
    camera.Open();

    // The registered configuration event handler has done its parametrization now.
    // Additional parameters could be set here.
    camera.UserSetSelector.SetValue(UserSetSelector_UserSet1);
    camera.UserSetLoad.Execute();

    // Grab some images for demonstration.
    camera.StartGrabbing(GrabStrategy_LatestImages);

    int counter = 0;
    struct timeval start, end;
    gettimeofday(&start, NULL);
    int timestamp = (int)start.tv_sec;

    int frame_number = 1;
    int frames_dropped = 0;

    while(camera.IsGrabbing()) {

      camera.RetrieveResult(5000, ptrGrabResult, TimeoutHandling_ThrowException);
		  const uint16_t *pImageBuffer = (uint16_t *) ptrGrabResult->GetBuffer();
	    fwrite(pImageBuffer, pixels_horizontal * pixels_vertical * sizeof(uint16_t), 1, stdout);

      cerr << "Frame Number: ";
      cerr << frame_number;
      cerr << "; Skipped frames :";
      cerr << ptrGrabResult->GetNumberOfSkippedImages() << endl;

      frames_dropped += ptrGrabResult->GetNumberOfSkippedImages();
      frame_number++;

      if(frame_number == c_countOfImagesToGrab + 1) {
        break;
      }

    }

    cerr << "Total number of dropped frames: ";
    cerr << frames_dropped << endl;

    // Close the camera.
    camera.Close();

    exit(0);

  }

  catch (const GenericException &e) {

    // Error handling.
    cerr << "An exception occurred." << endl
    << e.GetDescription() << endl;
    exitCode = 1;

  }

  // Comment the following two lines to disable waiting on exit
  cerr << endl << "Press Enter to exit." << endl;
  while(cin.get() != '\n');

  // Releases all pylon resources.
  PylonTerminate();

  return exitCode;

}
