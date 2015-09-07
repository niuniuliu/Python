
var webdriver = require('./node_modules/selenium-webdriver')
driver = new webdriver.Builder().withCapabilities(webdriver.Capabilities.chrome()).build();

function AcceptTermsOfUse() {
    var flow = webdriver.promise.controlFlow();
    var UserName = '//*[@name="Email"]';
    var Pwd = '//*[@name="Password"]';
    var LoginButton = '//*[@id="FormLogin"]/button';
    flow.execute(function () {
        driver.get('https://devidmadmin.ctp.dev.com/IdmFirmAdminWeb/');
    });
    flow.execute(function () {
        driver.findElement(webdriver.By.xpath(TermsOfUseLink))
    });

    flow.execute(function () {
        driver.findElement(webdriver.By.xpath(UserName)).clear();
        driver.findElement(webdriver.By.xpath(UserName)).sendKeys("helenjing2012+1432196976964@gmail.com")
    });

    flow.execute(function () {
        driver.findElement(webdriver.By.xpath(Pwd)).clear();
        driver.findElement(webdriver.By.xpath(Pwd)).sendKeys("Atlas2012")
    });

    flow.execute(function () {
        driver.findElement(webdriver.By.xpath(LoginButton))
    });

    flow.execute(function () {
        // Wait home page loading, to-do: add a function to check
        self.driver.sleep(10000);
    });


    var TermsOfUseLink = '//div[@class="tos-text"]//a'
        //var winHandleBefore = self.driver.getWindowHandle();

    //Click ToU link
    flow.execute(function () {
        // self.helper.FindElementByXpath(Elements.TermsOfUseDialog.TermsOfUseLink).click();
        driver.findElement(webdriver.By.xpath(TermsOfUseLink)).click();

        //self.driver.actions().mouseMove(element).perform();

        //self.driver.sleep(5000);
        /*
         self.driver.actions().mouseMove(element).perform();
         //self.driver.actions().click(self.webdriver.Button.RIGHT).perform();
         self.driver.actions().click(self.webdriver.Button.LEFT).perform();
         */
    });
}
// var webdriver = require('selenium-webdriver')
// driver = new webdriver.Builder().withCapabilities(webdriver.Capabilities.chrome()).build();

// // url = "file:///Users/TimLiu/Desktop/baidu.html"

// url = "file:///C:/Users/tliu/Data/GitHub/zZZzzZZzz/Python/python_exercise/selenium/switchWindowHandle/baidu.html"
// driver.get(url)
// driver.sleep(1000);
// popupLinkXPath = "/html/body/a[5]";

// driver.findElement(webdriver.By.xpath(popupLinkXPath)).click()

// driver.sleep(1000);

// driver.getAllWindowHandles()
//     .then(function(y) {
//         driver.switchTo().window(y[1])
//             .then(function() {
//                 driver.getWindowHandle()
//                     .then(function(x) {
//                         console.log("switch to: " + x)
//                     })

//                 driver.findElement(webdriver.By.id('kw')).sendKeys('TimTest');
//                 driver.sleep(1000);
//                 driver.findElement(webdriver.By.id('su')).click();
//                 driver.sleep(1000);
//                 driver.close();
//             })

//         driver.sleep(1000);
//         driver.switchTo().window(y[0]);
//         // driver.switchTo().window(currentWindowHandle);

//         driver.getWindowHandle()
//             .then(function(x) {
//                 console.log("switch back to: " + x)
//             })
//     })


// driver.getWindowHandle()
//     .then(function(x) {
//         console.log("After closed popup window")
//         console.log(x)
//     })

// driver.getTitle()
//     .then(function(titleName) {
//         console.log(titleName)
//     })

// driver.sleep(1000);
// driver.get("http://www.qq.com")
// driver.getTitle()
//     .then(function(titleName) {
//         console.log(titleName)
//     })

// driver.sleep(2000)
// driver.close();