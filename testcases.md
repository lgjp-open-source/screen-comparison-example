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

![keypoint](https://user-images.githubusercontent.com/25169430/136770289-cbed4925-8c86-4e94-97bc-6f0037c5fb56.png)
