## 1. Verify that "筴行日付" image in Old SAP (ECC) screen exists in New SAP (Fiori) screen
   
| Compare Text Image |                        |                 |                           |
|----------------|------------------------|-----------------|---------------------------|
| Pre-conditions | - [TestArchitect](https://www.testarchitect.com/) installed <br/> - IE installed and [configured](https://docs.testarchitect.com/automation-guide/application-testing/testing-web-and-ria-applications/testing-web-applications/automated-web-testing-with-non-webdriver/preparing-web-browsers/preparing-internet-explorer-for-web-testing/advanced-settings/) to run automation | Post-conditions |  |
|                |                        |                 |                           |
| Steps          | Action                 | Data            | Expected Result           |
| 1              | Open IE and Navigate to  https://github.com/KichiFinn/Screen-Comparison-Example/blob/main/images/hana.png |              |                           |
| 2              | Scroll to hana.png and Verify that "筴行日付" exists in this picture (New SAP screen) | baseline image of Old SAP (ECC) screen contains "筴行日付" keypoint | "筴行日付" exists (>90%)  |

![text-keypoint](https://user-images.githubusercontent.com/25169430/132504309-02d8cfea-b5d7-4204-9c56-fe6530b679dd.png)


## 2. Verify that T-code combo-box in Old SAP (ECC) screen exists in New SAP (Fiori) screen

| Compare Combo-box Image |                          |                 |                        |
|----------------|--------------------------|-----------------|------------------------|
| Pre-conditions | - [TestArchitect](https://www.testarchitect.com/) installed <br/> - IE installed and [configured](https://docs.testarchitect.com/automation-guide/application-testing/testing-web-and-ria-applications/testing-web-applications/automated-web-testing-with-non-webdriver/preparing-web-browsers/preparing-internet-explorer-for-web-testing/advanced-settings/) to run automation | Post-conditions |  |
|                |                          |                 |                        |
| Steps          | Action                   | Data            | Expected Result        |
| 1              | Open IE and Navigate to  https://github.com/KichiFinn/Screen-Comparison-Example/blob/main/images/hana.png |  |
| 2              | Scroll to hana.png and Verify that T-code combo-box exists in this picture (New SAP screen) | baseline image of Old SAP (ECC) screen contains T-code combo-box | T-code combo-box exists (>90%) |

![combobox-keypoint](https://user-images.githubusercontent.com/25169430/132504354-e4a19ee2-d0ef-4bd1-935e-c6d821d0637d.png)


## 3. Verify that "筴行日付" and T-code combo-box in Old SAP (ECC) screen exists in New SAP (Fiori) screen

| Compare Text and Combo-box Image    |                          |                 |                          |
|----------------|--------------------------|-----------------|--------------------------|
| Pre-conditions | - [TestArchitect](https://www.testarchitect.com/) installed <br/> - IE installed and [configured](https://docs.testarchitect.com/automation-guide/application-testing/testing-web-and-ria-applications/testing-web-applications/automated-web-testing-with-non-webdriver/preparing-web-browsers/preparing-internet-explorer-for-web-testing/advanced-settings/) to run automation | Post-conditions |  |
|                |                          |                 |                          |
| Steps          | Action                   | Data            | Expected Result          |
| 1              | Open IE and Navigate to  https://github.com/KichiFinn/Screen-Comparison-Example/blob/main/images/hana.png |   |
| 2              | Scroll to hana.png and Verify that "筴行日付" and T-code combo-box exists in this picture (New SAP screen) | baseline image of Old SAP (ECC) screen contains "筴行日付" and T-code combo-box | "筴行日付" and T-code combo-box exists (>90%) |

![keypoint](https://user-images.githubusercontent.com/25169430/132503765-4557a810-c5f8-4af2-9b07-7566dc760e50.png)

