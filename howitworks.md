# How to use the image comparison test case
This test case compares the baseline image with the target image using [SIFT algorithm](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform)
- **Input**: baseline image and its keypoints, target image, `percent`
- **Output**: true if baseline image similiars with target image more than  `percent` %, otherwise return false
### 1. Prerequisites 
- TestArchitect installed
- Python installed
- Basic knowledge about using TestArchitect

### 2. Create baseline picture's keypoints 
- Open baseline image (source image) with TestArchitect's [Key Points Modification tool](https://docs.testarchitect.com/user-guide/projects-and-project-items/project-items/picture-checks/key-points-modification-tool/)
- Choose suitable keypoints of baseline image. Choosing the best keypoints is based on the experience of tester. For example, we choose the keypoints in the red circle of the following picture:
![ChooseKeypoints](https://user-images.githubusercontent.com/86994495/145778702-629ba4e9-e2ab-432b-9b93-b509b9fa3f7f.png)
- Save baseline image keypoints

### 2. Input parameter for hight level action of TestArchitect tool
Open TestArchitect tool and input parameter for high level action:
- `baseline image`: source image
- `baseline keypoints`: image keypoints of source image that created in step 2
- `target image`: target image that will compare with source image
- `percent`: percent of similiar  when comparing using keypoint
![highlevelaction](https://user-images.githubusercontent.com/86994495/145789066-66500b46-7a7f-48d1-b6b5-63766527d5e3.png)

### 3. Results
- Currently, this action return `true` if two images similiar more than `percent`%; otherwise, return `false`

### 4. How it works?
- Step 1: Convert two images to greyscale with [opencv](https://opencv.org/)
![grayscale](https://user-images.githubusercontent.com/86994495/145785337-979d8a92-45c2-42cd-8116-f12c6a1a9215.png)
- Step 2: Clear identical paragraph in two images with background color. This test use [Google Vision API](https://cloud.google.com/vision) to recognize paragraphs in the two images. This step help remove noise when comparing using keypoints.
![simpler](https://user-images.githubusercontent.com/86994495/145785869-e2833411-3ccd-45a1-8255-e1338ecd57ae.png)
- Step 3: Compare source image's keypoints with in target image
![image](https://user-images.githubusercontent.com/86994495/145786956-148fdd18-c1c3-4c56-bc6c-f230428603e3.png)
