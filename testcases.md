## 1. Convert images to grayscale and clear identical paragraph in images
   
| Clear Identical Paragraph |                        |                 |                           |
|----------------|------------------------|-----------------|---------------------------|
| Pre-conditions | - [Google Cloud Vision AI](https://www.testarchitect.com/) installed <br/> - [OpenCV](https://pypi.org/project/opencv-python/) installed  <br/> - Windows x64| Post-conditions |  |
|                |                        |                 |                           |
| Steps          | Action                 | Data            | Expected Result           |
| 1              | Convert images to grayscale |   input images           |           grayscale output images                |
| 2              | Clear identical paragraph in two pictures | input images  | output images |

## 2. Compare two images using keypoints

| Compare Images |                          |                 |                        |
|----------------|--------------------------|-----------------|------------------------|
| Pre-conditions | - [TestArchitect](https://www.testarchitect.com/) installed  <br/> - Windows x64 | Post-conditions |  |
|                |                          |                 |                        |
| Steps          | Action                   | Data            | Expected Result        |
| 1              | Open target images by MSPaint | target image |
| 2              | Compare baseline image with target images using keypoint | baseline image | Image's keypoints are similiar more than 90% |

![combobox-keypoint](https://user-images.githubusercontent.com/25169430/132654691-0ad2e290-8cc7-4c36-9c9c-8aa166a8807d.png)