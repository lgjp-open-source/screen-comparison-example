# Introduction
- An demo of AI image comparison which mention at [https://www.logigear.jp/ai_compare](https://www.logigear.jp/ai_compare)
- Using [Google Cloud Vision API](https://cloud.google.com/vision) for Optical Character Recognition (OCR).
- Using [OpenCV Python](https://pypi.org/project/opencv-python) for image processing.
- Using [TestArchitect]() for running [SIFT algorithm](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform) (image's keypoint comparison) as following

![keypoint](https://user-images.githubusercontent.com/25169430/136770289-cbed4925-8c86-4e94-97bc-6f0037c5fb56.png)


# Test Cases
[testcases.md](./testcases.md)

# Prerequisites
Before you begin building and running this demo, you must have the following prerequisites installed on your system:
1. Windows 64 bits
2. [Testarchitect](https://www.testarchitect.com) 64 bits
   - Register free trial and download installation at https://www.testarchitect.com/free-download
3. [Python 3](https://www.python.org/downloads) 64 bits
   - Download Python 3 installation at https://www.python.org/downloads
4. [Opencv-python](https://pypi.org/project/opencv-python)
   - After installing Python, open terminal and enter the following command
   ```console
   > pip install opencv-python
   ```
5. [Google Cloud Vision API](https://cloud.google.com/vision/docs/setup)
   - Follow the instruction [here](https://cloud.google.com/docs/authentication/getting-started#windows) to create a service account, download JSON key and add it to environment variable
   - Open a terminal and enter the following command to install Python client library
   ```console
   > pip install --upgrade google-cloud-vision
   ```

# Run
### 1. Checkout source 
   - Download the zip source at https://github.com/lgjp-open-source/screen-comparison-example; then extract it
   - Or use git command: 
   ```console
   > git clone https://github.com/lgjp-open-source/screen-comparison-example.git
   ```
### 2. Import TestArchitect repository 
- We already implement all test scripts, test cases and export to a file at `./repository/AI-Image-Compare.dat`. Follow the guide [here](https://docs.testarchitect.com/administration-guide/repository-server-management/exporting-importing-repositories/importing-repositories/) to import it to TestArchitect.

### 3. Open TestArchitect and connect to imported repository in step 3
- Follow the guide [here](https://docs.testarchitect.com/user-guide/getting-started/working-with-repositories/connecting-to-a-repository/?hl=connect%20repository#main-container-page) to connect to `AI-Image-Compare` repository which was imported at step 2
- Choose  Server: `localhost:53400` and check `AI-Image-Compare` checkbox then press `OK`.

### 4. Run test script
- Double click `AI-Image-Compare` repository to open it (empty passord)
- Open `config` action in `Actions` and set `image_location` variabe to the downloaded `images` folder
- Right click **AI Image Comparison** then **Execute Test...**
- Click `Automation Tool...` button, choose `TestArchitect Python Harness` as `Playback Tool`. Then choose `Executable(s)` as `Python` and `Script(s)` as `ta_main.py` from downloaded folder at step 1 (Read [here](https://docs.testarchitect.com/testarchitect-tutorial/part-3-extending-testarchitect/lesson-8-using-an-automation-harness/working-with-the-python-harness/running-a-python-harness-test/) for more details about running TestArchitect Python Harness)
- Click **Execute** button to execute tests

### 5. View test results
- The results tab open automatically in TestArchitect after script execution finished.
- Click on **View detailed results per test line** to view test details.

# Step by step video
All steps are recorded in this following video:


https://user-images.githubusercontent.com/25169430/136925313-be942108-a985-41b7-a15a-84bc784a7f3f.mp4

   
# Advance
- Please read [here](https://docs.testarchitect.com/user-guide/projects-and-project-items/project-items/picture-checks/key-points-modification-tool/) if you want to know how to create Keypoint for Image Comparison in this project
