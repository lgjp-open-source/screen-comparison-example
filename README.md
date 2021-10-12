# Description
- [TestArchitect](https://www.testarchitect.com/)'s test cases scripts and videos demo for ["AI image comparison for automation"](https://www.logigear.jp/ai_compare/)
- Use [Google Cloud Vision API](https://cloud.google.com/vision) for paragraph recognization
- Use [SIFT algorithm](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform) for image's keypoint comparison as following

![keypoint](https://user-images.githubusercontent.com/25169430/136770289-cbed4925-8c86-4e94-97bc-6f0037c5fb56.png)


# Test Cases
[testcases.md](./testcases.md)

# Prerequisites
1. Windows 64 bits
2. [Testarchitect](https://www.testarchitect.com/) 64 bits installed
3. [Python](https://www.python.org/downloads/) 3 64 bits installed
4. [Opencv-python](https://pypi.org/project/opencv-python/) installed
5. [Cloud Vision API](https://cloud.google.com/vision/docs/setup) installed
6. [Cloud Vision Python client](https://cloud.google.com/vision/docs/quickstart-client-libraries) installed

# Run
### 1. Checkout source 
   - Download the zip source at https://github.com/lgjp-open-source/screen-comparison-example and extract it
   - Or use git command: 
   ```console
   $ git clone https://github.com/lgjp-open-source/screen-comparison-example.git
   ```
### 3. Import repository 
- Follow the guide [here](https://docs.testarchitect.com/administration-guide/repository-server-management/exporting-importing-repositories/importing-repositories/) to import repository at `./repository/AI-Image-Compare.dat` 

### 4. Open TestArchitect and connect to imported repository in step 3
- Follow the guide [here](https://docs.testarchitect.com/user-guide/getting-started/working-with-repositories/connecting-to-a-repository/?hl=connect%20repository#main-container-page) to connect to `AI-Image-Compare` imported repository at step 3
- Choose  Server: `localhost:53400` and check `AI-Image-Compare`

### 5. Run test script
- Double click `AI-Image-Compare` repository to open it (empty passord)
- Open `config` action in `Actions` and set `image_location` variabe to the downloaded images folder
- Right click **AI Image Comparison** then **Execute Test...**
- Click `Automation Tool...` buuton, choose `TestArchitect Python Harness` as `Playback Tool`. Then choose `Executable(s)` as `Python` and `Script(s)` as `ta_main.py` from downloaded folder at step 1 (Read [here](https://docs.testarchitect.com/testarchitect-tutorial/part-3-extending-testarchitect/lesson-8-using-an-automation-harness/working-with-the-python-harness/running-a-python-harness-test/) for more details)
- Click **Execute** button to execute test 2 Testcases

### 6. View test results
- The results tab open automatically after script execution finished.
- Click on **View detailed results per test line** to view test results

# Step by step video
All steps are recorded in this following video:


https://user-images.githubusercontent.com/25169430/132838483-5c5f3ed4-ed1e-4269-9e73-2e0b66106dc5.mp4

   
# Advance
- Please read [here](https://docs.testarchitect.com/user-guide/projects-and-project-items/project-items/picture-checks/key-points-modification-tool/) if you want to know how to create Keypoint for Image Comparison in this project
- Video how to train keypoints for text and combo-box:

https://user-images.githubusercontent.com/25169430/132837567-f4072802-8d96-4b9e-b35c-0a17df17ae66.mp4


