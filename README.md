# Description
- [TestArchitect](https://www.testarchitect.com/)'s test cases scripts and videos demo for ["AI image comparison for automation"](https://www.logigear.jp/ai_compare/)
- Use [SIFT algorithm](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform) as following

![keypoint](https://user-images.githubusercontent.com/25169430/132656930-60ec2b5c-0720-4b16-a204-58310eb6aff3.png)

# Test Cases
[testcases.md](./testcases.md)

# Run
### 1. Checkout source 
   - Download the zip source at https://github.com/lgjp-open-source/screen-comparison-example and extract it
   - Or use git command: 
   ```console
   $ git clone https://github.com/lgjp-open-source/screen-comparison-example.git
   ```

### 2. Configure IE for automation testing
- Follow the guide [here](https://docs.testarchitect.com/automation-guide/application-testing/testing-web-and-ria-applications/testing-web-applications/automated-web-testing-with-non-webdriver/preparing-web-browsers/preparing-internet-explorer-for-web-testing/advanced-settings/) to configure IE for automation tesing with TestArchitect
- If you want to run on other browsers, read [here](https://docs.testarchitect.com/automation-guide/application-testing/testing-web-and-ria-applications/)

### 3. Import repository 
- Follow the guide [here](https://docs.testarchitect.com/administration-guide/repository-server-management/exporting-importing-repositories/importing-repositories/) to import repository at `./repository/AI-Image-Compare.dat` 

### 4. Open TestArchitect and connect to imported repository in step 3
- Follow the guide [here](https://docs.testarchitect.com/user-guide/getting-started/working-with-repositories/connecting-to-a-repository/?hl=connect%20repository#main-container-page) to connect to `AI-Image-Compare` imported repository at step 3
- Choose  Server: `localhost:53400` and check `AI-Image-Compare`

### 5. Run test script
- Double click `AI-Image-Compare` repository to open it (empty passord)
- Right click **AI Image Comparison** then **Execute Test...**
- Click **Execute** button to execute test

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


