## 1. Verify that "筴行日付" and "ID" in Old SAP (ECC) screen exists in New SAP (Fiori) screen
   
| Compare Text image |                        |                 |                           |
|----------------|------------------------|-----------------|---------------------------|
| Pre-conditions | - [TestArchitect](https://www.testarchitect.com/) installed <br/> - IE installed and [configured](https://docs.testarchitect.com/automation-guide/application-testing/testing-web-and-ria-applications/testing-web-applications/automated-web-testing-with-non-webdriver/preparing-web-browsers/preparing-internet-explorer-for-web-testing/advanced-settings/) to run automation | Post-conditions |  |
|                |                        |                 |                           |
| Steps          | Action                 | Data            | Expected Result           |
| 1              | Open IE and Navigate to  https://github.com/KichiFinn/Screen-Comparison-Example/blob/main/images/hana.png |              |                           |
| 2              | Scroll to hana.png and Verify that "筴行日付" and "ID" exists in this picture (New SAP screen) | baseline image of Old SAP (ECC) screen contains "筴行日付" and "ID" keypoint | "筴行日付" and "ID" exists (>80%)  |

## 2. Verify that dialog with "ステータス" title in Old SAP (ECC) screen exists in New SAP (Fiori) screen

| Compare Dialog image |                          |                 |                        |
|----------------|--------------------------|-----------------|------------------------|
| Pre-conditions | - [TestArchitect](https://www.testarchitect.com/) installed <br/> - IE installed and [configured](https://docs.testarchitect.com/automation-guide/application-testing/testing-web-and-ria-applications/testing-web-applications/automated-web-testing-with-non-webdriver/preparing-web-browsers/preparing-internet-explorer-for-web-testing/advanced-settings/) to run automation | Post-conditions |  |
|                |                          |                 |                        |
| Steps          | Action                   | Data            | Expected Result        |
| 1              | Open IE and Navigate to  https://github.com/KichiFinn/Screen-Comparison-Example/blob/main/images/hana.png |  |
| 2              | Scroll to hana.png and Verify that dialog with "ステータス" title exists in this picture (New SAP screen) | baseline image of Old SAP (ECC) screen contains dialog with "ステータス" title | dialog with "ステータス" title exists (>80%) |

## 3. Verify that "筴行日付", "ID" and dialog with "ステータス" title in Old SAP (ECC) screen exists in New SAP (Fiori) screen

| Compare Text and Dialog image    |                          |                 |                          |
|----------------|--------------------------|-----------------|--------------------------|
| Pre-conditions | - [TestArchitect](https://www.testarchitect.com/) installed <br/> - IE installed and [configured](https://docs.testarchitect.com/automation-guide/application-testing/testing-web-and-ria-applications/testing-web-applications/automated-web-testing-with-non-webdriver/preparing-web-browsers/preparing-internet-explorer-for-web-testing/advanced-settings/) to run automation | Post-conditions |  |
|                |                          |                 |                          |
| Steps          | Action                   | Data            | Expected Result          |
| 1              | Open IE and Navigate to  https://github.com/KichiFinn/Screen-Comparison-Example/blob/main/images/hana.png |   |
| 2              | Scroll to hana.png and Verify that "筴行日付", "ID", and dialog with "ステータス" title exists in this picture (New SAP screen) | baseline image of Old SAP (ECC) screen contains "筴行日付", "ID", and dialog with "ステータス" title | dialog with "筴行日付", "ID", and  dialog with "ステータス" title exists (>80%) |
