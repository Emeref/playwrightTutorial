# playwrightTutorial
 This is my playwright tutorial

#### For system to works fine we have to install few packages:
 * pytest-playwritght
 * pytest-reporter-html1
 * pytest-xdist
 * pytest_dotenv

#### command to run tests:
    pytest --template=html1/index.html --report=report.html -n 3 --maxfail=1 -m smoke --browser=chromium --device="iPhone 14"  --video=retain-on-failure  --screenshot=only-on-failure

* **report**: name of report file.
* **n**: 'auto' allows to check bow many are available, and with numbers 1-auto we can select how many will 
                     not make using computer hard...
* **maxfail**: sets amount of fails after which we will stop the run
* **m**: will allow to test only TC that are marked with specific way (available markers are described in pytest.ini, 
        and each test has marker set before test definition
* **browser**: there are three options: 'chromium','firefox','webkit'. If there will be more than one selected (ex. 
              '--webkit=chromium --webkit=firefox' means that all tests will be run 2 times on selected browsers.
* **device**: allows to run tests as specific device: 'Pixel 7', 'iPhone 14' (full list under 
           https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json. 
           This runs only on chromium. 
* **video**: there are three options: off (no video saved), on(video for every test) or retain-on-failure (video only on failed tests).
            Results will be saved in 'test-results' folder, by adding --output=<name> it will create folder and save there
* **screenshot**: there are three options: off (no screenshot saved), on(screenshot for every test, on the end) or 
                   retain-on-failure (screenshot only on failed tests). Results will be saved in 'test-results' folder.